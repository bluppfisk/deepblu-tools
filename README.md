# deepblu-tools
Deepblu API tools

A set of tools to get the most out of [Deepblu](https://deepblu.com), export your dive logs into ODDF format, automatically like posts, and copy another user's followers.

## backupdives.py
Retrieves dive logs from Deepblu and exports them in [ODDF](http://oddf.org) format.

## autoliker.py
Logs you in with a set of accounts defined in **LOGINS** and automatically likes every post, beginning with the most recent one, until **MAX_LIKES** is reached or an earlier like is found.

## autofollow.js
Console JS script to copy automatically add a series of Deepblu users in **userIds** to the following list of a logged-in account with token **authToken**.