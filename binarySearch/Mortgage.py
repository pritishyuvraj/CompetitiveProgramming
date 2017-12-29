#Question: TopCoder Statistics (Top Coder Statistics)
#Name: Mortgage
#Link: https://community.topcoder.com/stat?c=problem_statement&pm=2427&rd=4765

#Solution: O(N log n)
#Author: Pritish Yuvraj
import math 

class Mortgage:
	def __init__(self):
		pass 

	def monthlyPayment(self, loan, interest, term, x = None):
		print "\n\nloan ->", loan
		print "interest ->", interest/10.0
		print "term (in months) ->", term*12 
		#print self.check(loan, float(interest)/10.0, term, x)
		print self.binarySearch(loan, float(interest)/10.0, term)
	
	def binarySearch(self, loan, interest, term):
		low = 0
		high = loan
		while low < high:
			mid = low + (high - low)/2
			if self.check(loan, interest, term, mid):
				#True case 
				high = mid 
			else:
				#False Case 
				low = mid + 1 
		if self.check(loan, interest, term, low):
			return low 
		else:
			return -1 

	def check(self, loan, interest, term, x):
		#print "start-> ", loan, x
		for i in xrange(term*12 - 1):
			loan = loan - x 
			#print "step -> ", i, loan, x, (1 + (float(interest)/float(12*100)))
			loan = math.ceil(loan * (1 + (float(interest)/float(12*100))))
			#print "step -> ", i, loan
			if loan <= 0: return True 
		if loan <= x: 
			return True 
		return False 

if __name__ == '__main__':
	mt = Mortgage()
	mt.monthlyPayment(1000, 50, 1, 86)
	mt.monthlyPayment(1000000, 1000000, 1000, 988143)
	mt.monthlyPayment(2000000000, 6000, 1, 671844808)
	mt.monthlyPayment(1000000, 129, 30, 10868)
	mt.monthlyPayment(1999999999, 1000000, 1, 1976284585)

