import json
import requests
import sys
import random

# def get_courses():

	
# 	r = requests.get('https://hackbulgaria.com/api/students/', verify = False)
# 	content = r.json()

# 	i = 1
# 	courses = {}
# 	for student in content:
# 		for course in student['courses']:
# 			if course['name'] not in courses.values():
# 				courses[i] = course['name']
# 				i += 1 
# 	return courses

# def list_courses(courses):
# 	index = 1
# 	for key in courses:
# 		value = courses[key]
# 		print('[{}] {} '.format(key, value))


# courses = get_courses()
# list_courses(courses) 

r = requests.get('https://hackbulgaria.com/api/students/', verify = False)
all_contents = r.json()

def get_courses(content):
	output_set = set()
	for student in content:
		courses = student['courses']
		for course in courses:
			output_set.add(course['name'])
	return list(output_set)

def list_courses(set):
	for i, item in enumerate(set):
		print('[{}] {} '.format(i, item))


def match_teams(course_id, team_size, group_time):

	"""course_id = sys.argv[0]
	team_size = sys.argv[1]
	group_time = sys.argv[2] """

	global all_contents
	output = []

	courses = get_courses(all_contents)
	name_of_course = courses[course_id]
	for student in all_contents:
		for elem in student['courses']:
			if elem["name"] == name_of_course and elem["group"] == group_time:
				output.append(student["name"])
	random.shuffle(output)

	for i in range(1, len(output)+1):
		print (output[i-1])
		if i % team_size == 0 :
			print ("=========")




print (match_teams(1,2,2))

