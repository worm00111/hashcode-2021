import numpy as np
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
	def __init__(self):
		self.streets_in = []
		self.intersection_in []
		
		self.streets_out = []
		self.intersection_out []

	def add_street_in(self, street_name):
		self.streets_in.append(street_name)

	def add_end_intersection(self, end_intersection: Intersection):
		self.end_intersection = end_intersection

# Input
for FILE in os.listdir('.'):
	# Skip non-input files and d (since that's too slow)
	if not FILE.endswith('.txt') or FILE.startswith('d'):
		continue

	# Read in content of file
	with open(FILE, 'r') as ifp:
	    lines = ifp.readlines()

	# Convert content to data structures
	# #Simulation time #Intersections #Streets #Cars #Score for car
	D, I, S, V, F = list(map(int, lines[0].strip().split()))
	
	streets = {}
	# Read in streets. Key = street id value = {start_interserction, end_intersection, name, seconds}
	for line_ix in range(1, S):
		# #start_intersection, #end_intersection, #seconds
		B, E, name, L =  list(map(str, lines[line_ix].strip().split()))
		streets[name] = {"B": int(B), "E": int(E), "L": int(L)}
	
	car_map = {}
	index = 0
	for line_ix2 in range(S+1, S+V+1):
		# #number of streets to travel, #list of street names to travel
		car_list = list(map(str, lines[line_ix2].strip().split()))
		P = int(car_list[0])
		car_path_list = car_list[1:]
		car_map[index] = {"P": P, "car_path_list": car_path_list}
		index = index + 1

	breakpoint()

intersections = {}
# Create intersection map. ALGORITHM #1
for street in streets:
	if not street.E in intersections:
		intersections[street.value.E] = Intersection(?)

	intersections[street.E].add_street_in(street.key)



intersections = {}


# Create intersection map. ALGORITHM #2
for street in streets:
	if not street.B in intersections:
		ins = Intersection()
		intersections[street.value.B] = ins
		intersections[street.value.B].ins.add_street_out(street.value.E)

	if not street.E in intersections:
		ins = Intersection()
		intersections[street.value.E] = ins
		intersections[street.value.E].ins.add_street_in(street.value.B)

	if
	

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