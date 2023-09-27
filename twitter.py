

import tweepy

api_key = "16rsyUFihzbOgOSpUJsOfolZn"
api_secret_key = "kTfxIorBsIMDTD6sWZQuVVm82GZSKVKkS2G8IjASEakS6fJ1wN"
access_token = "1374391655491497986-msOzvkYQ9PJtgBApqrVyd0M3Md6tVt"
access_token_secret = "30adQZD9CCyeUPwb7WAR0zd6AxdhZKifXdt4aen6zdByK"


# new tweepy api object
auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


# get desired user id
user = api.get_user(screen_name="elonmusk")
user_id = user.id


tweets = api.user_timeline(user_id = user_id, count = 10)


for tweet in tweets:
    print(tweet.text)