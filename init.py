import json
import os

records = json.loads(open(os.path.expanduser('~/projects/frappe/records.json')).read())

from frappeclient import FrappeClient

host = ''
user = ''
password = ''

conn = FrappeClient(host)
conn.login(user, password)


for record in records:
	try:
		print(conn.insert(record))
	except Exception as e:
		print('Failed ' + record['doctype'])
		print(str(e))
	# print('Failed ' + str(e))
