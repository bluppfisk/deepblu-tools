# Class to interact with the Deepblu API

import requests
import json

from deepblu_user import DeepbluUser

CHUNKSIZE = 100  # Don't load everything at once
DEEPBLU_API = "https://prodcdn.tritondive.co/apis/"
DEEPBLU_LOGIN_API = DEEPBLU_API + "user/v0/login"
DEEPBLU_DIVES_API = DEEPBLU_API + "discover/v0/post/{}/diveLog?limit={}&skip={}"
DEEPBLU_DRAFT_DIVES_API = (
    DEEPBLU_API + "divelog/v0/getRawLogs?hide=0&type=1&limit={}&skip={}"
)
DEEPBLU_PROFILE_API = DEEPBLU_API + "user/v0/profile/"


class DeepbluAPI:
    # Login user
    @staticmethod
    def login(email, password):
        deepblu_user = DeepbluUser()
        headers = {
            "content-type": "application/json; charset=utf-8",
            "accept-language": "en",
        }
        data = {"email": email, "password": password}
        print("Connecting to Deepblu...")
        res = requests.post(DEEPBLU_LOGIN_API, data=json.dumps(data), headers=headers)
        response = json.loads(res.text)

        if response.get("statusCode") == 200:
            userData = response.get("result", {}).get("userInfo", {})
            deepblu_user.set_data_from_json(userData)

            deepblu_user.auth_code = response.get("result", {}).get("accessToken")
            deepblu_user.logged_in = True
            print("Logged in as " + email + "!")
        else:
            print(
                "Could not log in "
                + email
                + ", error code: "
                + str(response.get("statusCode"))
            )
            deepblu_user.logged_in = False
            deepblu_user.auth_code = None
            deepblu_user.user_id = email

        return deepblu_user

    # Loads divelogs from Deepblu API
    @staticmethod
    def load_dives_from_api(deepblu_user: DeepbluUser, type: str):
        headers = {
            "content-type": "application/json; charset=utf-8",
            "authorization": deepblu_user.auth_code,
            "accept-language": "en",
        }

        skip = 0
        posts = []
        result_index_name = "posts" if type == "published" else "logs"

        print("Loading first {} {} logs from Deepblu API...".format(CHUNKSIZE, type))

        # This will load chunks from the API until there are no more logs or
        # until the API call returns no results, in which case we'll set skip to -1
        while skip >= 0:
            if type == "published":
                url = DEEPBLU_DIVES_API.format(deepblu_user.user_id, CHUNKSIZE, skip)
            else:
                url = DEEPBLU_DRAFT_DIVES_API.format(CHUNKSIZE, skip)
            res = requests.get(url, headers=headers)
            response = json.loads(res.text)
            if response.get("statusCode") == 200:  # result!
                if len(response.get("result", {}).get(result_index_name)) > 0:
                    if skip > 0:
                        print("Loading next {} {} logs...".format(CHUNKSIZE, type))

                    new_posts = response.get("result", {}).get(result_index_name)
                    if type == "published":
                        posts += new_posts
                    else:
                        for post in new_posts:
                            new_post = {"diveLog": post, "medias": {}}
                            posts.append(new_post)

                    skip += CHUNKSIZE  # next chunk
                else:
                    # we're done here
                    print("Found all the {} logs!".format(type))
                    skip = -1

            else:
                # API call yielded no results
                if deepblu_user.logged_in:
                    print(
                        str(response.get("statusCode"))
                        + ",API Error. God knows what happened at Deepblu."
                    )
                else:
                    print(
                        str(response.get("statusCode"))
                        + ",Incorrect user + password combination or user id."
                    )
                exit()
                skip = -1
                return False

        return posts
