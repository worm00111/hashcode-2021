import numpy as np
from collections import OrderedDict
from tqdm import tqdm
import os
import warnings
warnings.filterwarnings('ignore')

"""
class Library():
	def __init__(self, total_n_books, signup_time, n_books_day, books):
		self.total_n_books = total_n_books
		self.signup_time = signup_time
		self.n_books_day = n_books_day
		self.books = books
"""

class Intersection():
	def __init__(self, id):
		self.id = id

		self.streets_in = []
		self.intersections_in = []
		
		self.streets_out = []
		self.intersections_out = []

	def add_street_in(self, street_name):
		self.streets_in.append(street_name)

	def add_street_out(self, street_name):
		self.streets_out.append(street_name)

	def add_intersection_in(self, start_intersection):
		self.intersections_in.append(start_intersection)

	def add_intersection_out(self, end_intersection):
		self.intersections_out.append(end_intersection)

# Input
for FILE in os.listdir('.'):
	# Skip non-input files and d (since that's too slow)
	if not FILE.endswith('.txt'):
		continue

	# Read in content of file
	with open(FILE, 'r') as ifp:
	    lines = ifp.readlines()

	# Convert content to data structures
	# #Simulation time #Intersections #Streets #Cars #Score for car
	D, I, S, V, F = list(map(int, lines[0].strip().split()))
	
	streets = OrderedDict()
	# Read in streets. Key = street id value = {start_interserction, end_intersection, name, seconds}
	for line_ix in range(1, S+1):
		# #start_intersection, #end_intersection, #seconds
		B, E, name, L =  list(map(str, lines[line_ix].strip().split()))
		streets[name] = {"B": int(B), "E": int(E), "L": int(L)}
	
	car_map = {}
	index = 0
	for line_ix2 in range(S+1, S+V+1):
		# P = #number of streets to travel, car_path_list = #list of street names to travel
		car_list = list(map(str, lines[line_ix2].strip().split()))
		P = int(car_list[0])
		car_path_list = car_list[1:]
		car_map[index] = {"P": P, "car_path_list": car_path_list}
		index = index + 1

	# Create intersection map
	intersections = OrderedDict()
	for street_key, street_value in streets.items():
		if not street_value['B'] in intersections:
			ins = Intersection(street_value['B'])
			intersections[street_value['B']] = ins
		

		if not street_value['E'] in intersections:
			ins = Intersection(street_value['E'])
			intersections[street_value['E']] = ins

		# Add out intersections and streets
		intersections[street_value['B']].add_intersection_out(intersections[street_value['E']])
		intersections[street_value['B']].add_street_out(street_key)

		# Add in intersections and streets
		intersections[street_value['E']].add_intersection_in(intersections[street_value['B']])
		intersections[street_value['E']].add_street_in(street_key)

	shortestCar = 0
	sum_of_time = 0
	street_name = ""
	# For every car
	for car_key, car_value in car_map.items():
		# For every street the car has to take
		for i in range(1, P):
			sum_of_time = 0
			# For every street
			for street_key, street_value in streets.items():
				# Get the street name
				street_name = car_path_list[i]
				# add 
				sum_of_time = sum_of_time + street_value["L"]

			if(sum_of_time < D):
				shortestCar = car_key
				break

	if(sum_of_time < D):
		break
	

	results = []
	roadTimes = {}
	firstIntersection = intersections[0]

	# Find the first intersection
	start = car_map[shortestCar].car_path_list[0]
	for i in range(1, car_map[car_path_list]):
		for intersection_key, intersection_value in intersections.items():
			if start in intersection_value.streets_in:
				firstIntersection = intersection_value


	length = 0
	current_street = car_map[shortestCar].car_path_list[1]
	# Get the length of the second road
	while (#not at the end of the path):
		for i, street in enumerate(firstIntersection.streets_out):
			if street == current_street:
				for street_key, street_value in streets.items():
					length = street_key["street"].L
				
			
		

	# BASIC algortithm and output
	with open('{}.out'.format(FILE), 'w+') as ofp:
		ofp.write('{}\n'.format(len(intersections)))
		for intersection_key, intersection_value in intersections.items():
			ofp.write('{}\n'.format(intersection_value.id))
			ofp.write('1\n')
			ofp.write('{} {}\n'.format(intersection_value.streets_in[0], 1))

	print(FILE)

"""
	# Getting the best remaining books from a library
	def get_best_books(library, assigned_books, curr_time):
		# How much time do we have remaining?
		time = D - library.signup_time - curr_time

		# Sort yet unscanned books by their scores 
		sorted_books = sorted(library.books - assigned_books, 
				      key=lambda b: -book_scores[b])

		# Take the maximum number of books that we can still scan
		return list(sorted_books)[:time*library.n_books_day]


	# Key that we will for our max function
	def score(library, assigned_books, curr_time, assigned_libraries):
		if library in assigned_libraries:
			return float('-inf')

		# Get best books in remaining time
		possible_books = get_best_books(library, assigned_books, curr_time)

		# Score is sum of book scores divided by signup time
		score = sum([book_scores[k] for k in possible_books])
		score /= library.signup_time

		return score

	# Data structures to keep track of what has been done
	assigned_books = set()
	curr_time = 0
	assigned_libraries = set()

	# Data structures to store our results
	asm_books = []
	asm_libraries = []

	# Iteratively take the best possible library and schedule it
	for _ in tqdm(range(L)):
		scores = [score(x, assigned_books, curr_time, assigned_libraries)
			  for x in libraries]
		best_library = np.argmax(scores)
		best_books = get_best_books(libraries[best_library], 
					    assigned_books, curr_time)

		# Break if we pass the deadline or already assigned the library
		if best_library in assigned_libraries:
			break

		curr_time += libraries[best_library].signup_time
		if curr_time >= D:
			break

		asm_books.append(best_books)
		asm_libraries.append(best_library)

		assigned_books = assigned_books.union(set(best_books))
		assigned_libraries.add(libraries[best_library])

	# Write away results & calculate local score
	total_score = 0
	with open('{}.out'.format(FILE), 'w+') as ofp:
		ofp.write('{}\n'.format(len(asm_libraries)))
		for i, l in enumerate(asm_libraries):
			ofp.write('{} {}\n'.format(l, len(asm_books[i])))
			ofp.write('{}\n'.format(' '.join(map(str, asm_books[i]))))
			total_score += sum([book_scores[x] for x in asm_books[i]])

	print(FILE, total_score)
	"""