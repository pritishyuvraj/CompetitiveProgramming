class binarySearch:
	def __init__(self, length, findElement):
		self.array = range(1, length)
		self.findElement = findElement
	
	def binarySearchFunc(self):
		low = 0
		high = len(self.array)
		while low < high:
			mid = low + (high - low)/2
			if self.array[mid] >= self.findElement:
				high = mid 
			else:
				low = mid + 1 
		if self.array[low] <= self.findElement:
			print self.array, low, self.array[low]
			return low 
		else:
			return -1 

if __name__ == '__main__':
	bs = binarySearch(10, 3)
	print bs.binarySearchFunc()
