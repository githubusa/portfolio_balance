import collections
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


	def min_dp(self):
		return min(self.dp)

	def max_dp(self):
		return max(self.dp)

	def up_down_trend(self):
		print("trend")
		sim = self.dp
		print(sim)
		print(len(sim))

		up = []
		down = []
		trend_mark =""
		#information to record
		item = [0]
		for i in range(1, len(sim)):
			if trend_mark == "":
				if sim[i] > sim[i-1]:
					trend_mark = "up"
					# days in the trend
					item[0] = item[0] +1 
				if sim[i] < sim[i-1]:
					trend_mark = "down"
					# days in the trend
					item[0] = item[0] +1 
			if trend_mark == "up":
				#include equal in the up trend
				if sim[i] >= sim[i-1]:
					trend_mark = "up"
					# days in the trend
					item[0] = item[0] +1 
				if sim[i] < sim[i-1]:
					#trend turning point
					trend_mark = ""
					up.append(item)
					item = [0]
			if trend_mark == "down":
				if sim[i] > sim[i-1]:
					#trend turning point
					trend_mark = ""
					down.append(item)
					item = [0]
				if sim[i] <= sim[i-1]:
					trend_mark = "down"
					# days in the trend
					item[0] = item[0] +1 
		#process last group 
		if trend_mark == "up":
			up.append(item)
		if trend_mark == "down":
			down.append(item)
		
		#to final arrays
		for it in up:
			self.up_trend.append(it[0])
		for it in down:
			self.down_trend.append(it[0])
		

	def print_trend(self):
		"""visulization of the trend"""
		self.up_down_trend()
		print("up trend", self.up_trend)
		print("down trend", self.down_trend)
		counter=collections.Counter(self.up_trend)
		print("up trend", counter)
		counter=collections.Counter(self.down_trend)
		print("down trend", counter)
		

	def test_trend(self):
		sim = [1,1,2,3,1,2,1,2,4,6,6,5,3,2,2]
		print(len(sim))

		up = []
		down = []
		trend_mark =""
		#information to record
		item = [0]
		for i in range(1, len(sim)):
			if trend_mark == "":
				if sim[i] > sim[i-1]:
					trend_mark = "up"
					# days in the trend
					item[0] = item[0] +1 
				if sim[i] < sim[i-1]:
					trend_mark = "down"
					# days in the trend
					item[0] = item[0] +1 
			if trend_mark == "up":
				#include equal in the up trend
				if sim[i] >= sim[i-1]:
					trend_mark = "up"
					# days in the trend
					item[0] = item[0] +1 
				if sim[i] < sim[i-1]:
					#trend turning point
					trend_mark = ""
					up.append(item)
					item = [0]
			if trend_mark == "down":
				if sim[i] > sim[i-1]:
					#trend turning point
					trend_mark = ""
					down.append(item)
					item = [0]
				if sim[i] <= sim[i-1]:
					trend_mark = "down"
					# days in the trend
					item[0] = item[0] +1 
		#process last group 
		if trend_mark == "up":
			up.append(item)
		if trend_mark == "down":
			down.append(item)
		print(up)
		print(down)

def main():
	data = csv_reader.csv_array("")
	# daily price array
	dp = data.get_dp()
	lp = data.get_lp()
	hp = data.get_hp()

	dp_t = dp_trend(dp)
	print(dp_trend.min_dp(dp_t))
	print(dp_trend.max_dp(dp_t))
	
	#plt.plot(dp)
	#plt.show()

	#correlate lp and dp
	lp_dp_corr = np.corrcoef(lp, dp)[0]

	for item in lp_dp_corr:
		print(item)

	hp_dp_corr = np.corrcoef(hp, dp)[0]
	for item in hp_dp_corr:
		print(item)

	
	dp_t.print_trend()		


if __name__ == "__main__":
	main()
