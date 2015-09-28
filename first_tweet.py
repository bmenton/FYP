import tweepy

key = "YYBqazKNLaV2pZrBiXm0ns3r9"
secret = "2cG7PItBL1ufZ84MOBiEz6HrnwcRG8CQET2zvYe4xSsPwZbYc8"
token = "3015797271-eNJsCqmGKCKeBiiX2LzyWFejzd3ZMdVwgDO5k1s"
token_secret = "QHbFRxJOzD3V5D0ovIlmsoPQg9oux6GfnFXtx0OfUIYFU"

auth = tweepy.OAuthHandler(key, secret)
auth.set_access_token(token, token_secret)
client = tweepy.API(auth)
tweet = "#Python Rocks!"
client.update_status(status = tweet)