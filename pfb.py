import requests
import os
import errno

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=VGT&apikey=PQCE1NMXXIWQ7ZG0&datatype=csv'
response = requests.get(url)
text = response.text
print(text)

filename = os.getcwd()+'/data/VGT'

if not os.path.exists(os.path.dirname(filename)):
	try:
		os.makedirs(os.path.dirname(filename))
	except OSError as exc: # Guard against race condition
		if exc.errno != errno.EEXIST:
			raise

with open(filename, "w+") as file:
	file.write(text)
	file.close()

