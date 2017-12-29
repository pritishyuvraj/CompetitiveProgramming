#Question: TopCoder Statistics (Top Coder Statistics)
#Name: FairWorkload
#Link: https://community.topcoder.com/stat?c=problem_statement&pm=1901&rd=4650

#Solution: O(log N)
#Author: Pritish Yuvraj

class FairWorkload:
	def __init__(self):
		pass 

	def getMostWork(self, folders, workers):
		print folders, self.binarySearch(folders, workers)

	def binarySearch(self, folders, workers):
		low = max(folders)
		high = sum(folders)

		while low < high:
			mid = low + (high - low) /2 
			req_workers = 1
			current_load = 0
			for i in folders:
				if current_load + i <= mid:
					current_load += i 
				else:
					req_workers += 1 
					current_load = i 
			if req_workers <= workers:
				high = mid 
			else:
				low = mid + 1 
		return low 

if __name__ == '__main__':
	fwl = FairWorkload()
	fwl.getMostWork([10, 20, 30, 40, 50, 60, 70, 80, 90 ], 3)
	fwl.getMostWork([10, 20, 30, 40, 50, 60, 70, 80, 90], 5)
	fwl.getMostWork([568, 712, 412, 231, 241, 393, 865, 287, 128, 457, 238, 98, 980, 23, 782], 4)
	fwl.getMostWork([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1000],2)
	fwl.getMostWork([950, 650, 250, 250, 350, 100, 650, 150, 150, 700], 6)