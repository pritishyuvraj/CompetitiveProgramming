#TopCoder Question
#Question ID: UnionOfIntervals
#Link: https://community.topcoder.com/stat?c=problem_statement&pm=4823&rd=8074

#Solution: O(n) {Assuming the intervals passed are sorted or O (n log n)}
#Author: Pritish Yuvraj
class UnionOfIntervals:
	def __init__(self):
		self.stack = []
		self.intervals = []
		self.top = -1 
		self.cumulativeFrequency = {}

	def nthElement(self, lowerBound, upperBound, n):
		#lowerBound: Array
		#UpperBound: Array
		#n:  int
		for i, j in zip(lowerBound, upperBound):
			self.intervals.append([i, j])
		self.intervals.sort()
		print "Unsorted Intervals-> ", self.intervals
		sorted_intervals = self.merge()
		print "Sorted & Merged Intervals -> ", sorted_intervals
		print "Cumulative Frequence -> ", self.cumulativeFrequency
		index = self.binarySearch(sorted_intervals, n)
		if index != -1:
			print "Element found", sorted_intervals[index], n
			pos = self.position(sorted_intervals, index, n)
			print "Position is -> ", pos, "\n\n" 
			return pos 
		else:
			print "ELement not found", sorted_intervals, n, "\n\n"

	def merge(self):
		for index, i in enumerate(self.intervals):
			if index == 0:
				self.stack.append(i)
				self.top += 1 
			else:
				temp = self.stack[self.top]
				if temp[1] > i[0] and temp[1] < i[1]:
					temp[1] = i[1]
					self.stack.pop()
					self.stack.append(temp)
				elif temp[1] < i[0]:
					self.stack.append(i)
					self.top += 1
		count = 0
		for index, i in enumerate(self.stack):
			self.cumulativeFrequency[index] = count + i[1] - i[0] + 1
			count += i[1] - i[0] + 1
		return self.stack

	def binarySearch(self, array, n):
		low = 0
		high = len(array) - 1	
		mid = 0
		while low < high:
			mid = low + (high - low)/2
			#print "print", low, mid, high, array
			if self.condition(array[mid], n):
				#True
				high = mid 
			else:
				low = mid + 1
			#print "Exit", low, mid, high
		if self.condition(array[low], n):
			#True 
			return low 
		else:
			return -1 

	def condition(self, array, n):
		if n>=array[0] and n<=array[1]:
			return True
		else:
			return False	

	def position(self, sorted_intervals, index, n):
		if index ==0:
			return n - sorted_intervals[0][0] 
		else:
			return self.cumulativeFrequency[index -1] + n- sorted_intervals[index][0]

if __name__ == '__main__':
	UOI = UnionOfIntervals()			
	UOI.nthElement([2, 1, 5], [4, 3, 7], 3)
	UOI = UnionOfIntervals()
	UOI.nthElement([1, 3], [5, 7], 4)
	UOI = UnionOfIntervals()
	UOI.nthElement([1, 4], [3, 5], 3)
	UOI = UnionOfIntervals()
	UOI.nthElement([-1500000000, -1], [0, 1500000000], 91)