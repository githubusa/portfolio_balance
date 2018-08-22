import requests
import os
import errno
import datetime

class data_retrieval(object):
	"""docstring for data_retrieval"""
	def __init__(self, url, symbol):
		super (data_retrieval, self).__init__()
		self.url = url
		self.symbol = symbol
		
		#self.url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=VGT&apikey=PQCE1NMXXIWQ7ZG0&datatype=csv'
		response = requests.get(self.url)
		text = response.text
		print(text)

		date = datetime.datetime.today().strftime('%Y-%m-%d')
		print(date)
		filename = os.getcwd()+'/data/'+ self.symbol+date+'.csv'

		if not os.path.exists(os.path.dirname(filename)):
			try:
				os.makedirs(os.path.dirname(filename))
			except OSError as exc: # Guard against race condition
				if exc.errno != errno.EEXIST:
					raise

		with open(filename, "w+") as file:
			file.write(text)
			file.close()

def main():
	#dr = data_retrieval("", "VGT")
	filename = os.getcwd() + '/data/symbols'
	with open(filename, "r") as file:
		symbols = file.readlines()
	for i in range(len(symbols)):
		symbols[i] = symbols[i].rstrip()
		url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+symbols[i]+'&apikey=PQCE1NMXXIWQ7ZG0&datatype=csv'
		symbol = symbols[i]
		dr = data_retrieval(url, symbol)
	

if __name__ == '__main__':
	main()