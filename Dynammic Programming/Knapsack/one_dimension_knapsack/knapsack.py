# Input:
# python knapsack.py "pepsi:55, detergent:30,chips:25,cereal:15" 4 100
from pprint import pprint 
import sys 
class knapsack:
	def __init__(self, arguments):
		dictionary, n, total_weight = self.parse_arguments(arguments)
		temp_dic = {}
		current_weight = 0;
		self.most_optimal_sol = []
		self.all_sol = []
		self.generate_all_pairs_bfs(dictionary, total_weight, temp_dic, current_weight)
		self.most_optimal_sol = self.clean_for_output(self.most_optimal_sol)
		self.all_sol = self.clean_for_output(self.all_sol)
		print "\n\nMost optimal solution"
		pprint(self.most_optimal_sol)
		print "\n\nAll Solution"
		pprint(self.all_sol)

	def parse_arguments(self, arguments):
		dic_in = arguments[1]
		n = arguments[2]
		total_weight = arguments[3]
		dic = {key:int(pair) for key, pair in [x.strip().split(':') for x in dic_in.strip().split(',')]}
		print dic 
		return dic, n, int(total_weight)

	def generate_all_pairs_bfs(self, dictionary, total_weight, temp_dic, current_weight):
		current_weight = sum(temp_dic.values())
		# print temp_dic, current_weight
		if current_weight <= total_weight:
			# print "All solution", temp_dic, current_weight, total_weight, current_weight<total_weight

			if current_weight == total_weight:
				# print "Most optimal solution", temp_dic
				self.most_optimal_sol.append(temp_dic.keys())
			else:
				self.all_sol.append(temp_dic.keys())
			for food_name in dictionary:
				if food_name not in temp_dic:
					temp_dic[food_name] = dictionary[food_name] 
					# current_weight += dictionary[food_name]
					self.generate_all_pairs_bfs(dictionary, total_weight, temp_dic, current_weight)
					del temp_dic[food_name]
					# current_weight -= dictionary[food_name]

	def clean_for_output(self, array):
		temp_array = []
		for soln in array:
			soln.sort()
			soln = list(set(soln))
			if soln not in temp_array and len(soln) > 0:
				temp_array.append(soln)
		return temp_array

if __name__ == '__main__':
	print sys.argv
	knap = knapsack(sys.argv)