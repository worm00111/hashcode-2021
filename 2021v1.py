import numpy as np
from collections import OrderedDict
from tqdm import tqdm
from typing import List
import os
import warnings
warnings.filterwarnings('ignore')

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

class Car():
	def __init__(self, P, path_list):
		self.P = P
		self.path_list = path_list

def evaluate_path_distance(car: Car, streets: OrderedDict):
	total_street_length = 0
	for street in car.path_list:
		# Find out the length of a street
		total_street_length += streets[street]["L"]

	return total_street_length + car.P - 1 # Take away 1, because we don't care about the last intersection


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
	
	# Create a list of cars
	cars = []
	index = 0
	for line_ix2 in range(S+1, S+V+1):
		# P = #number of streets to travel, car_path_list = #list of street names to travel
		car_list = list(map(str, lines[line_ix2].strip().split()))
		P = int(car_list[0])
		car_path_list = car_list[1:]
		cars.append(Car(P, car_path_list))
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

	# Run the algorithm every second
	for i in range(0, D):
		print("second = " + str(i))
		# Sort cars based on distance they need to travel
		cars = sorted(cars, key=lambda car: evaluate_path_distance(car, streets))

	# BASIC algortithm and output
	with open('{}.out'.format(FILE), 'w+') as ofp:
		ofp.write('{}\n'.format(len(intersections)))
		for intersection_key, intersection_value in intersections.items():
			ofp.write('{}\n'.format(intersection_value.id))
			ofp.write('1\n')
			ofp.write('{} {}\n'.format(intersection_value.streets_in[0], 1))

	print(FILE)

	def old_algorithm():
		for i in range(0,10): # Dummy for loop. Remove this if using the algorithm
			shortestCar = 0
			sum_of_time = 0
			street_name = ""
			# For every car
			for car_key, car_value in cars.items():
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
			start = cars[shortestCar].car_path_list[0]
			for i in range(1, cars[car_path_list]):
				for intersection_key, intersection_value in intersections.items():
					if start in intersection_value.streets_in:
						firstIntersection = intersection_value


			length = 0
			current_street = cars[shortestCar].car_path_list[1]
			# Get the length of the second road
			while (not current_street == null):
				for i, street in enumerate(firstIntersection.streets_out):
					if street == current_street:
						for street_key, street_value in streets.items():
							length = street_key["street"].L