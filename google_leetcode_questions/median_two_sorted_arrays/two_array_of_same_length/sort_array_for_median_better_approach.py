# https://leetcode.com/problems/median-of-two-sorted-arrays/description/

# Approach 1 assuming two arrays are of equal length
# Solution -> O(log N)

# https://www.geeksforgeeks.org/median-of-two-sorted-arrays/

import math 

class find_median:
	def __init__(self):
		pass 

	def median(self, array):
		if len(array) % 2 == 0:
			# Even length of the array 
			return (array[len(array)/2] + array[len(array)/2 - 1]) / 2.0
		else:
			# Odd length array 
			return array[len(array)/2]

	def recursive(self, array1, array2):
		print array1, array2
		print "median -> ", self.median(array1) ,self.median(array2) 

		if self.median(array1) == self.median(array2):
			return self.median(array1)

		if len(array1) == len(array2) == 2:
			self.cal_median(array1, array2)
			return

		if self.median(array1) > self.median(array2):
			print "greater",array1[0:int(len(array1)/2.0)], array2[int(math.ceil(len(array2)/2.0) -1):]
			self.recursive(array1[0:int((len(array1)/2.0))+1], array2[int(math.ceil(len(array2)/2.0) -1):])

		else:
			print ("Smaller", array1[int(math.ceil(len(array1)/2.0)-1):], array2[0:int(len(array2)/2.0)], int(math.ceil(len(array1)/2.0)-1)), len(array1)/2,math.ceil(len(array2)/2.0), int(math.ceil(len(array2)/2.0))
			self.recursive(array1[int(math.ceil(len(array1)/2.0)-1):], array2[0:int(len(array2)/2.0)+1])


	def cal_median(self, array1, array2):
		print "Final array -> ", array1, array2
		median = (max(array1[0], array2[0]) + min(array1[1], array2[1])) / 2.0
		print "Median is -> ", median

if __name__ == "__main__":
	# input_array1 = [1, 12, 15, 26, 38]
	# input_array2 = [2, 13, 17, 30, 45]

	input_array1 = [1, 2, 3, 4, 5, 6]
	input_array2 = [2, 3, 4, 5, 6, 7]

	input_array1 = [1, 2, 3, 4, 5, 6]
	input_array2 = [10, 20, 30, 40, 50, 60]		

	fm = find_median()
	fm.recursive(input_array1, input_array2)