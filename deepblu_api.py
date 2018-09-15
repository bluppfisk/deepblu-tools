import requests
import json

CHUNKSIZE = 100  # Don't load everything at once
DEEPBLU_API = "https://prodcdn.tritondive.co/apis/"
DEEPBLU_LOGIN_API = DEEPBLU_API + "user/v0/login"
# DEEPBLU_DIVES_API = DEEPBLU_API + "discover/v0/post/search?postType=divelog&userId=" # Old Deepblu posts API
DEEPBLU_DIVES_API = DEEPBLU_API + "discover/v0/post/{}/diveLog?limit={}&skip={}"
DEEPBLU_DRAFT_DIVES_API = DEEPBLU_API + "divelog/v0/getRawLogs?hide=0&type=1&limit={}&skip={}"
DEEPBLU_PROFILE_API = DEEPBLU_API + "user/v0/profile/"


###
# Deepblu API class
# 
class DeepbluAPI(object):
    ###
    # Load divelogs from Deepblu API
    # 
    @staticmethod
    def loadDivesFromAPI(deepbluUser, type):
        headers = {
            "content-type": "application/json; charset=utf-8",
            "authorization": deepbluUser.authCode,
            "accept-language": "en"
        }

        skip = 0
        posts = []
        result_index_name = 'posts' if type == 'published' else 'logs'

        print("Loading first {} {} logs from Deepblu API...".format(CHUNKSIZE, type))

        ###
        # This will load chunks from the API until there are no more logs or
        # until the API call fails, in which case we'll set skip to -1
        # 
        while skip >= 0:
            if type == "published":
                url = DEEPBLU_DIVES_API.format(deepbluUser.userId, CHUNKSIZE, skip)
            else:
                url = DEEPBLU_DRAFT_DIVES_API.format(CHUNKSIZE, skip)
            res = requests.get(url, headers=headers)
            response = json.loads(res.text)
            if response.get('statusCode') == 200:  # result!
                if len(response.get('result', {}).get(result_index_name)) > 0:
                    if skip > 0:
                        print("Loading next {} {} logs...".format(CHUNKSIZE, type))

                    new_posts = response.get('result', {}).get(result_index_name)
                    if type == 'published':
                        posts += new_posts
                    else:
                        for post in new_posts:
                            new_post = {'diveLog': post, 'medias': {}}
                            posts.append(new_post)

                    skip += CHUNKSIZE # next chunk
                else:
                    # we're done here
                    print("Found all the {} logs!".format(type))
                    skip = -1

            else:
                # API call failed
                if deepbluUser.loggedIn:
                    print(str(response.get('statusCode')) + ",API Error. God knows what happened at Deepblu.")
                else:
                    print(str(response.get('statusCode')) + ",Incorrect user + password combination or user id.")
                exit()
                skip = -1
                return False

        return posts
