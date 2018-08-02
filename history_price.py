import csv_reader
import matplotlib.pyplot as plt
import numpy as np



class dp_trend(object):
	"""docstring for dp_trend"""
	def __init__(self, dp):
		super(dp_trend, self).__init__()
		self.dp = dp

	def min_dp(self):
		return min(self.dp)

	def max_dp(self):
		return max(self.dp)



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


if __name__ == "__main__":
	main()
