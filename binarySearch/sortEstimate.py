#TopCoder
#Question: https://community.topcoder.com/stat?c=problem_statement&pm=3561&rd=6519
#Question Name: Sort Estimate SortEstimate sortEstimate

#Solution: Time Complexity: O(log N), Space Complexity: O(1)
#Author: Pritish Yuvraj
import math 

class SortEstimate:
	def __init__(self):
		pass 

	def howMany(self, c, time):
		#Format is: c*n*log(n) <= time 
		n = self.binarSearch()
		return n 

	def binarySearch(self, c, time):
		constant = float(time)/float(c)
		#temp_array = range(1, int(constant))
		low = 0
		#high = len(temp_array)
		high = int(constant)
		while low < high:
			mid = low +  (high - low)/2
			if self.equality_condition(mid, constant):
				#True 
				high = mid 
			else:
				low = mid + 1 
		if self.equality_condition(low, constant):
			return low
		else:
			return -1 

	def equality_condition(self, n, constant):
		if n*math.log(n, 2) >= constant:
			return True
		else:
			return False

if __name__ == '__main__':
	bs = SortEstimate()
	print bs.binarySearch(1, 8)
	print bs.binarySearch(2, 16)
	print bs.binarySearch(37, 12392342)
	print bs.binarySearch(1, 2000000000)