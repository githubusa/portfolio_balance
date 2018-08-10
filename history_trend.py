import collections
import statistics 
import csv_reader
import matplotlib.pyplot as plt
import numpy as np



class dp_trend(object):
	"""docstring for dp_trend"""
	def __init__(self, dp):
		super(dp_trend, self).__init__()
		self.dp = dp
		self.up_trend = []
		self.down_trend = []
		self.up_price = {}
		self.down_price = {}


	def min_dp(self):
		return min(self.dp)

	def max_dp(self):
		return max(self.dp)

	def up_down_trend(self):
		print("trend")
		sim = self.dp
		
		up = []
		up_price = {}
		down = []
		down_price = {}

		trend_mark =""
		
		#price in the trend
		price = []

		#information to record, days in trend
		item = [0]
		price.append(sim[0])
		
		for i in range(1, len(sim)):
			if trend_mark == "":
				if sim[i] > sim[i-1]:
					trend_mark = "up"
					
				if sim[i] < sim[i-1]:
					trend_mark = "down"
					
				item[0] = 1

			if trend_mark == "up":
				#include equal in the up trend
				if sim[i] >= sim[i-1]:
					trend_mark = "up"
					# days in the trend
					item[0] = item[0] +1
					# price in the bucket
					price.append(sim[i])
				if sim[i] < sim[i-1]:
					#trend turning point
					trend_mark = ""
					up.append(item)
					idx = len(up) -1
					up_price[idx] = price
					item = [0]
					price = []
					price.append(sim[i])
				continue				
			if trend_mark == "down":
				if sim[i] > sim[i-1]:
					#trend turning point
					trend_mark = ""
					down.append(item)
					idx = len(down) -1
					down_price[idx] = price
					item = [0]
					price = []
					price.append(sim[i])
				if sim[i] <= sim[i-1]:
					trend_mark = "down"
					# days in the trend
					item[0] = item[0] +1 
					# price in the bucket
					price.append(sim[i])
		#process last group 
		if trend_mark == "up":
			up.append(item)
			idx = len(up) -1
			up_price[idx] = price
		if trend_mark == "down":
			down.append(item)
			idx = len(down) -1
			down_price[idx] = price


		#reset 
		item =[0]
		price = []

		# convert up down to up_trend and down_trend
		for itm in up:
			self.up_trend.append(itm[0])
		for itm in down:
			self.down_trend.append(itm[0])
	
		self.up_price = up_price
		self.down_price = down_price

		

	def print_trend(self):
		"""visulization of the trend"""
		self.up_down_trend()
		print("up trend", self.up_trend)
		print("down trend", self.down_trend)
	
		print("up_price", self.up_price)
		print("down_price", self.down_price)

		counter=collections.Counter(self.up_trend)
		print("up trend", counter)
		counter=collections.Counter(self.down_trend)
		print("down trend", counter)
		

	def test_trend(self):
		sim = [1,1,2,3,1,2,1,2,4,6,6,5,3,2,2,1,2,1,0.5,0.4,0.3,0.2]
		#sim = [3,2,1,0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1, 1,2,3,4]
		#sim = [3,2]
		print(len(sim))

		up = []
		up_price = {}
		down = []
		down_price = {}

		trend_mark =""
		
		#price in the trend
		price = []

		#information to record, days in trend
		item = [0]
		price.append(sim[0])
		
		for i in range(1, len(sim)):
			if trend_mark == "":
				if sim[i] > sim[i-1]:
					trend_mark = "up"
					
				if sim[i] < sim[i-1]:
					trend_mark = "down"
					
				item[0] = 1

			if trend_mark == "up":
				#include equal in the up trend
				if sim[i] >= sim[i-1]:
					trend_mark = "up"
					# days in the trend
					item[0] = item[0] +1
					# price in the bucket
					price.append(sim[i])
				if sim[i] < sim[i-1]:
					#trend turning point
					trend_mark = ""
					up.append(item)
					idx = len(up) -1
					up_price[idx] = price
					item = [0]
					price = []
					price.append(sim[i])
				continue				
			if trend_mark == "down":
				if sim[i] > sim[i-1]:
					#trend turning point
					trend_mark = ""
					down.append(item)
					idx = len(down) -1
					down_price[idx] = price
					item = [0]
					price = []
					price.append(sim[i])
				if sim[i] <= sim[i-1]:
					trend_mark = "down"
					# days in the trend
					item[0] = item[0] +1 
					# price in the bucket
					price.append(sim[i])
		#process last group 
		if trend_mark == "up":
			up.append(item)
			idx = len(up) -1
			up_price[idx] = price
		if trend_mark == "down":
			down.append(item)
			idx = len(down) -1
			down_price[idx] = price


		#reset 
		item =[0]
		price = []

		print(up)
		print(down)
		print(up_price)
		print(down_price)

def main():
	data = csv_reader.csv_array("")
	# daily price array
	dp = data.get_dp()
	lp = data.get_lp()
	hp = data.get_hp()

	dp_t = dp_trend(dp)
	#print trend results
	dp_t.print_trend()	
	"""
	print("dp mean")
	print(statistics.mean(dp))

	
	print(dp_trend.min_dp(dp_t))
	print(dp_trend.max_dp(dp_t))

	#dp_t.test_trend()
	
	#plt.plot(dp)
	#plt.show()

	#correlate lp and dp

	lp_dp_corr = np.corrcoef(lp, dp)[0]

	for item in lp_dp_corr:
		print(item)

	hp_dp_corr = np.corrcoef(hp, dp)[0]
	for item in hp_dp_corr:
		print(item)

	"""	
		



if __name__ == "__main__":
	main()
