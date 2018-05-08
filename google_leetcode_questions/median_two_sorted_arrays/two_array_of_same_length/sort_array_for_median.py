# https://leetcode.com/problems/median-of-two-sorted-arrays/description/

# Approach 1 assuming two arrays are of equal length

# https://www.geeksforgeeks.org/median-of-two-sorted-arrays/

class find_median:
	def __init__(self, array1, array2):
		self.array1 = array1
		self.array2 = array2

	def merge(self, array1, array2):
		i = 0 
		j = 0 
		temp_array = []
		count = -1

		while i < len(array1) and j < len(array2):
			if array1[i] < array2[j]:
				temp_array.append(array1[i])
				temp = array1[i]
				i += 1 
				count += 1 
			else:
				temp_array.append(array2[j])
				temp = array2[j]
				j += 1 
				count += 1
			if count == len(array1) - 1:
				# Case for extracting n - 1
				self.extracting_n_1(temp)
				
			if count == len(array1):
				# Case for extracting n 
				self.extracting_n(temp)

		if i < len(array1):
			for index_i in xrange(i, len(array1)):
				temp_array.append(array1[index_i])
				count += 1 
				if count == len(array1):
				# Case for extracting n 
					self.extracting_n(array1[index_i]) 

		if j < len(array2):
			for index_j in xrange(j, len(array2)):
				temp_array.append(array2[index_j])
				count += 1 
				if count == len(array1):
				# Case for extracting n 
					self.extracting_n(array2[index_j])

		return temp_array

	def extracting_n_1(self, element):
		self.n_1_element = element

	def extracting_n(self, element):
		self.n_element = element

if __name__ == "__main__":
	input_array1 = [1, 12, 15, 26, 38]
	input_array2 = [2, 13, 17, 30, 45]

	# input_array1 = [1, 2, 3, 4, 5, 6]
	# input_array2 = [2, 3, 4, 5, 6, 7]

	# input_array1 = [1, 2, 3, 4, 5, 6]
	# input_array2 = [10, 20, 30, 40, 50, 60]
	fm = find_median(input_array1, input_array2)
	print fm.merge(input_array1, input_array2)
	print fm.n_1_element, fm.n_element
	print "Median -> ", (fm.n_1_element + fm.n_element)/2.0
