# https://www.codechef.com/ZCOPRAC/problems/ZCO14002
# Author: Pritish Yuvraj

# Still in progress

class supw_soln:
	def __init__(self, n, list_of_mins):
		self.n = n 
		self.list_of_mins = list_of_mins
		self.select_timings = []

		# print self.n, self.list_of_mins
		self.window()
		print sum(self.select_timings)

	def window(self):
		start_index = 0
		while start_index < self.n:

			temp_list = self.list_of_mins[start_index:start_index+3]

			# Minimum element in temp list 
			min_element = min(temp_list)

			# Index of the minimum element in temp list
			min_element_index = temp_list.index(min_element)

			self.select_timings.append(min_element)
			start_index += 3

			# print "start_index", start_index, min_element_index, temp_list, self.list_of_mins




if __name__ == '__main__':
	n = int(raw_input(""))
	list_of_mins = [int(x) for x in raw_input("").split()]
	supw = supw_soln(n, list_of_mins)