import csv
import os

class csv_array(object):
	low_price = []
	"""docstring for ClassName"""
	def __init__(self, stock):
		super(csv_array, self).__init__()
		#stock symbol
		self.stock = stock

		#daily lowest price
		self.low_price = []

		#daily highest price
		self.high_price = []

		#close price
		self.day_price = []

		#open price (off market trading)
		self.open_price = []
	

	
		with open('data/VGT.csv', newline='') as csvfile:
			csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
			# skip the header
			csvreader.__next__()
			for row in csvreader:
				#open price
				self.open_price.append(float(row[1]))
				#low price
				self.low_price.append(float(row[3]))
				#high price
				self.high_price.append(float(row[2]))
				#day price
				self.day_price.append(float(row[4]))

	def get_op(self):
		return self.open_price

	def get_lp(self):
		return self.low_price

	def get_hp(self):
		return self.high_price

	def get_dp(self):
		return self.day_price

def main():
	"""
	test csv reader
	"""
	data = csv_array("")
	lp = data.get_lp()

	for item in lp:
		print(item)
	

if __name__ == "__main__" :
	main()