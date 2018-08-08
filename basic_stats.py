import csv_reader
import statistics 
import matplotlib.pyplot as plt
import numpy as np




class dp_stats(object):
	"""docstring for dp_stats"""
	def __init__(self, dp):
		super(dp_stats, self).__init__()
		self.dp = dp
		self.mean = 0
		# num of observation / sigma (1/value)
		self.harmonic_mean = 0
		self.median = 0 

		#standard div
		self.stdev = 0
		self.variance = 0

	def get_mean(self):
		self.mean = statistics.mean(self.dp)
		return self.mean

	def get_harmonic_mean(self):
		self.harmonic_mean = statistics.harmonic_mean(self.dp)
		return self.harmonic_mean

	def get_median(self):
		self.median = statistics.median(self.dp)
		return self.median

	def get_stdev(self):
		self.stdev = statistics.pstdev(self.dp)
		return self.stdev

	def get_variance(self):
		self.variance = statistics.pvariance(self.dp)
		return self.variance

def main():
	data = csv_reader.csv_array("")
	# daily price array
	dp = data.get_dp()
	dp_s = dp_stats(dp)
	print("mean")
	print(dp_s.get_mean())
	print("harmonic mean")
	print(dp_s.get_harmonic_mean())
	print("median")
	print(dp_s.get_median())

	print("stdev")
	print(dp_s.get_stdev())

	print("variance")
	print(dp_s.get_variance())

if __name__ == '__main__':
	main()

