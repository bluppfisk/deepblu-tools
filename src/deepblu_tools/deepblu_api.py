import json

import requests

from deepblu_tools.models import deepblu as dm


CHUNKSIZE = 100  # Don't load everything at once
DEEPBLU_API = "https://prodcdn.tritondive.co/apis/"
DEEPBLU_LOGIN_API = DEEPBLU_API + "user/v0/login"
DEEPBLU_DIVES_API = DEEPBLU_API + "discover/v0/post/{}/diveLog?limit={}&skip={}"
DEEPBLU_DRAFT_DIVES_API = (
    DEEPBLU_API + "divelog/v0/getRawLogs?hide=0&type=1&limit={}&skip={}"
)
DEEPBLU_PROFILE_API = DEEPBLU_API + "user/v0/profile/"


def login(email: str, password: str) -> dm.DeepbluUser:
    deepblu_user = dm.DeepbluUser()
    headers = {
        "content-type": "application/json; charset=utf-8",
        "accept-language": "en",
    }
    data = {"email": email, "password": password}

    res = requests.post(DEEPBLU_LOGIN_API, data=json.dumps(data), headers=headers)
    if res.status_code == 200:
        response = res.json()
        userData = response.get("result").get("userInfo")
        deepblu_user.update(userData)

        deepblu_user.auth_code = response.get("result", {}).get("accessToken")
        deepblu_user.logged_in = True
    elif (
        res.status_code == 499  # invalid login
        or res.status_code == 400  # might be a user id instead of email
    ):
        deepblu_user.user_id = email
        deepblu_user.auth_code = ""
    else:
        res.raise_for_status()

    return deepblu_user


def load_dives(deepblu_user: dm.DeepbluUser, post_type: str) -> list:
    headers = {
        "content-type": "application/json; charset=utf-8",
        "authorization": deepblu_user.auth_code,
        "accept-language": "en",
    }

    skip = 0
    posts = []
    key = "posts" if post_type == "published" else "logs"

    print(f"Loading first {CHUNKSIZE} {post_type} logs from Deepblu API...")

    # This will load chunks from the API until there are no more logs or
    # until the API call returns no results, in which case we'll set skip to -1
    while True:
        if post_type == "published":
            url = DEEPBLU_DIVES_API.format(deepblu_user.user_id, CHUNKSIZE, skip)
        else:
            url = DEEPBLU_DRAFT_DIVES_API.format(CHUNKSIZE, skip)

        res = requests.get(url, headers=headers)
        res.raise_for_status()

        response = res.json()

        if len(response.get("result", {}).get(key)) > 0:
            if skip > 0:
                print(f"Loading next {CHUNKSIZE} {post_type} logs...")

            new_posts = response.get("result", {}).get(key)
            if post_type == "published":
                posts += new_posts
            else:
                for post in new_posts:
                    new_post = {"diveLog": post, "medias": {}}
                    posts.append(new_post)

            skip += CHUNKSIZE  # next chunk
        else:
            print(f"Found all the {post_type} logs!")
            break

    return posts
