import csv, sqlite3

con = sqlite3.connect('politics.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS details(
	twitter_name text,
	full_name text,
	location text,
	twitter_id int PRIMARY KEY)
;''')
	
with open('datacsv.csv','rb') as fin:

    dr = csv.DictReader(fin)
    to_db = [(i['twitter_name'], i['full_name'], i['location'], i['twitter_id']) for i in dr]

cur.executemany("INSERT INTO details (twitter_name, full_name, location, twitter_id) VALUES (?, ?, ?, ?);", to_db)
con.commit()