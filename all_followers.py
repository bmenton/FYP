import tweepy
import csv
import sqlite3

key = "YYBqazKNLaV2pZrBiXm0ns3r9"
secret = "2cG7PItBL1ufZ84MOBiEz6HrnwcRG8CQET2zvYe4xSsPwZbYc8"
token = "3015797271-eNJsCqmGKCKeBiiX2LzyWFejzd3ZMdVwgDO5k1s"
token_secret = "QHbFRxJOzD3V5D0ovIlmsoPQg9oux6GfnFXtx0OfUIYFU"

auth = tweepy.OAuthHandler(key, secret)
auth.set_access_token(token, token_secret)
client = tweepy.API(auth)


con = sqlite3.connect('politics.db')
cur = con.cursor()



cur.execute('''CREATE TABLE IF NOT EXISTS all_followers(
	ids int,
	follower_id int)
;''')

temp = cur.execute("SELECT * FROM details")
all = temp.fetchall()

for hup in all:
	user = client.get_user(hup[3])
	for friend in user.friends():
		to_db = [(hup[3], friend.id)]
		cur.executemany("INSERT INTO all_followers (ids, follower_id) VALUES (?, ?);", to_db)
		con.commit()
con.close()
	