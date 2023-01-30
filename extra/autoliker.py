# Requires Python 3 and the python-requests package

import json
import time

import requests

MAX_LIKES = 50  # increments of 10

LOGINS = {
    "email@address.com": "password",  # add as many accounts as you like
}

DEEPBLUAPI = "https://prodcdn.tritondive.co/apis/discover/v0/post/"

DEEPBLULOGIN = "https://prodcdn.tritondive.co/apis/user/v0/login"

LIKEPATH = "/like"
FEEDPATH = "liveFeed?limit=10&publishTime="


class DeepbluPost(object):
    def __init__(self, post, email, authCode):
        self.post = post
        self.authCode = authCode
        self.email = email

    def like(self):
        url = DEEPBLUAPI + self.post + LIKEPATH
        headers = {
            "content-type": "application/json; charset=utf-8",
            "authorization": self.authCode,
            "accept-language": "en",
        }
        try:
            res = requests.post(url, headers=headers)
        except Exception as e:
            print(e)

        response = json.loads(res.text)
        if response["statusCode"] == 200:
            if int(response["result"]["doILike"]) == 1:
                print("Post " + self.post + " liked by " + self.email + "!")
        else:
            print(
                "Account "
                + self.email
                + "may not be authorized, error code: "
                + str(response["statusCode"])
            )


class AutoLiker(object):
    def login(self, email, password):
        headers = {
            "content-type": "application/json; charset=utf-8",
            "accept-language": "en",
        }
        data = {"email": email, "password": password}
        res = requests.post(DEEPBLULOGIN, data=json.dumps(data), headers=headers)
        response = json.loads(res.text)

        if response["statusCode"] == 200:
            authCode = response["result"]["accessToken"]
            print("Obtained token for " + email + "!")
        else:
            print(
                "Account "
                + email
                + " could not log in, error code: "
                + str(response["statusCode"])
            )
            authCode = None

        return authCode

    def get_posts(self, authCode, startTime):
        url = DEEPBLUAPI + FEEDPATH + str(startTime)
        headers = {
            "content-type": "application/json; charset=utf-8",
            "authorization": authCode,
            "accept-language": "en",
        }
        try:
            res = requests.get(url, headers=headers)
        except Exception as e:
            print(e)

        response = json.loads(res.text)
        posts = response["result"]["posts"]
        return posts

    def get_unliked_posts(self):
        self.unlikedPosts = []
        for email, password in LOGINS.items():
            startTime = int(time.time())
            authCode = self.login(email, password)
            if authCode is None:
                continue

            while startTime is not False and len(self.unlikedPosts) < MAX_LIKES:
                posts = self.get_posts(authCode, startTime)
                for post in posts:
                    if int(post["isLiked"]) == 1:
                        startTime = False
                        break

                    print("Found unliked post: " + str(post["postId"]))
                    self.unlikedPosts.append(
                        DeepbluPost(post["postId"], email, authCode)
                    )
                    startTime = post["createTime"]

    def run(self):
        self.get_unliked_posts()
        if len(self.unlikedPosts) == 0:
            quit("No unliked posts found! All done.")
        else:
            print("Found " + str(len(self.unlikedPosts)) + " unliked posts! Liking...")

            for unlikedPost in self.unlikedPosts:
                unlikedPost.like()


autoLiker = AutoLiker()
autoLiker.run()
