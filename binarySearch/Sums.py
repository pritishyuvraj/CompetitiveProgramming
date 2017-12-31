#Question: Special Sums
#Question From: CodeChef
#Link: https://www.codechef.com/INOIPRAC/problems/INOI1501
#Problem ID: INOI1501

#Author: Pritish Yuvraj
#Solution: O(N^3) {Needs Improvement, I know!!}
class specialSums:
	def __init__(self):
		pass

	def maximize(self, n, a, b):
		max_sum = 0
		for i in xrange(n):
			for j in xrange(n):
				temp_score = self.cal_score(i, j, a, b, n)
				#print i, j, temp_score
				if temp_score > max_sum:
					max_sum = temp_score
		return max_sum

	def cal_score(self, i, j, a, b, N):
		#i = i-1
		#j = j-1
		if i == j: return a[i]
		totalSum = a[i] + a[j]
		if i < j:
			for k in xrange(i, j+1):
				if k != i and k!= j:
					totalSum += b[k] 
		else: 
			for k in xrange(0, j):
				totalSum += b[k] 
			for k in xrange(i+1, N):
				totalSum += b[k]
		return totalSum

if __name__ == '__main__':
	n = int(raw_input())
	a = [int(x) for x in raw_input().split()]
	b = [int(x) for x in raw_input().split()]
	sp = specialSums()
	print sp.maximize(n, a, b)
