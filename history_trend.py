import collections
import statistics 
import csv_reader
import csv_writer
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
		"""
		prepare data foundation for further analysis
		1. days in up and downs
		2. prices in each up and down bucket
		"""
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
		
	def get_trend_info(self):
		self.up_down_trend()
		#self.uptrend_days = collections.Counter(self.up_trend)
		return self.up_trend, self.down_trend, self.up_price, self.down_price

	def get_price_delta(self):
		up_trend, down_trend, up_price, down_price = self.get_trend_info()
		print(up_price)
		price_delta = []
		price_deltas = {}
		for key, prices in up_price.items():
			gap = (prices[-1]-prices[0])/prices[0]
			len_day = len(prices)
			if len_day in price_deltas:
				price_delta = price_deltas[len_day]
				price_delta.append(gap)
			else:
				price_delta.append(gap)
				price_deltas[len_day] = price_delta
			price_delta = []
		for len_day, price_delta in price_deltas.items():
			print("days in period: ", len_day)
			print("min, max: ", min(price_delta), max(price_delta))
			print("avg: ", (max(price_delta)-min(price_delta))/len_day)

	def draw_trend_hist(self, data):
		up_trend, down_trend, up_price, down_price = self.get_trend_info()

		days = []
		numbers = []
		#up trend

		#use frequenet data directly
		plt.hist(up_trend)
		#plt.xticks(days)

		plt.title("Up Days")
		plt.xlabel("Days")
		plt.ylabel("Numbers")
		#plt.show()
		plt.savefig('imgs/up_days.png')
		plt.close()

		#down trend
		plt.hist(down_trend)
		#plt.xticks(days)

		plt.title("Down Days")
		plt.xlabel("Days")
		plt.ylabel("Numbers")
		#plt.show()
		plt.savefig('imgs/down_days.png')

	def write_csv(self):
		data = []
		data.append(["up", "down"])

		data.append([len(self.up_trend), len(self.down_trend)])

		#convert itrerable to string
		print( " ".join(map(str, data[1])))

		csv_writer.array_csv("", data)

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
	dp_t.draw_trend_hist([])
	dp_t.get_price_delta()
	#print trend results
	#dp_t.print_trend()
	#dp_t.write_csv()	

	

	#dp_t.draw_hist([])

	#plt.savefig('imgs/up_days.png')
	#print(up_days, up_price)
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
