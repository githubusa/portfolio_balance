import csv
import os

class array_csv(object):
	
	"""docstring for ClassName"""
	def __init__(self, stock, array):
		super(array_csv, self).__init__()
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
		
		with open(filename, "w+", newline='') as csvfile:
			 writer = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
			 for i in range(0, len(self.result)):
			 	writer.writerow(self.result[i])
    

def main():
	"""
	test csv writer
	"""
	data = []
	data.append(["min", "max"])

	data.append([1, 2])

	#convert itrerable to string
	print( " ".join(map(str, data[1])))

	

	array_csv("", data)
	

if __name__ == "__main__" :
	main()