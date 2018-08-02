import csv
import os

class array_csv(object):
	
	"""docstring for ClassName"""
	def __init__(self, stock, array):
		super(csv_array, self).__init__()
		#stock symbol
		self.stock = stock

		self.result = array
	
		#handle new file
		filename = os.getcwd()+'/data/VGT' +'_result.csv'

		if not os.path.exists(os.path.dirname(filename)):
			try:
				os.makedirs(os.path.dirname(filename))
			except OSError as exc: # Guard against race condition
				if exc.errno != errno.EEXIST:
					raise
		
		with open(filename, newline='') as csvfile:
			 fieldnames = self.result[0]
			 writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
			 writer.writeheader()
			 for i in range(1, len(self.result)):
			 	writer.writerow(self.result[i])
    

def main():
	"""
	test csv writer
	"""
	data[0] =["min", "max"]

	result = [1, 2]

	#convert itrerable to string
	data[1] = " ".join(map(str, result))


	for item in lp:
		print(item)
	

if __name__ == "__main__" :
	main()