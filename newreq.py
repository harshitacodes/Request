import os.path 
from os import path
import requests
import json

print("---------------- welcome to the saral courses ---------------")


print("\n")
# this is the url where api will hit the request
get_saral_url = "http://saral.navgurukul.org/api/courses"
# print(get_saral_url)
def courses_api(url):
	response = requests.get(url)
	return(response.text)


if path.exists("courses.json"):
	with open("courses.json","r") as data:
		# coverting the data into string from _io.TextIoWrapper
		read_file = json.load(data)
		# data is converting from string to dictionary  
		dictionary_type = json.loads(read_file)
else:
	response_text = courses_api(get_saral_url)
	with open("courses.json","w") as file:
		json.dump(response_text,file)
		 # while dumping the data from file in response_text it might change the type string
		dictionary_type = json.loads(response_text)
#  this main list contain the data in dictionary format
courses_list = (dictionary_type['availableCourses'])
# print(type(courses_list))


def courses_name():
	i = 0
	# loop will run in courses list
	while i < len(courses_list):
		cousre_name = courses_list[i]['name']
		courses_id = courses_list[i]['id']
		print(i+1,"-",cousre_name,courses_id)
		i = i + 1
courses_name()


def courseId():
	id_list = []
	course_name = []
	j = 0
	while j < len(courses_list):
		id_list.append(courses_list[j]['id'])
		course_name.append(courses_list[j]['name'])
		j = j + 1
	user_id = int(input("enter the course id: "))-1
	course_id = id_list[user_id]
	print("course id is",course_id)
	print(course_name[user_id])


	callApi = "https://saral.navgurukul.org/api/courses" + "/" +str(id_list[user_id])+ "/" + "exercises"


	if path.exists("coExercise/course"+(str(user_id))+".json"):
		with open("coExercise/course"+(str(user_id))+".json","r") as data_file:
			readfile = json.load(data_file)	
			dic_type = json.loads(readfile)
	else:
		restext = courses_api(callApi)
		with open("coExercise/course"+(str(user_id))+".json","w") as filedata:
			json.dump(restext,filedata)                        
			dic_type = json.loads(restext)
	return ([dic_type['data'],id_list[user_id]])


idlistdata = courseId()
id_listdata = (idlistdata[0])
user_id = (idlistdata[1])

    
def parentchildExercise(list_data):
	parent_index = 0
	while parent_index < len(list_data):
		parent_Exercise = list_data[parent_index]['name']
		childExerciseslist = list_data[parent_index]['childExercises']
		print(parent_index+1,parent_Exercise)
		child_index = 0
		while child_index < len(childExerciseslist):
			if "parent_exercise_id" in childExerciseslist[child_index]:
				print(5*" ", child_index+1,"-", childExerciseslist[child_index]['name'])
			child_index = child_index + 1
		parent_index = parent_index + 1
parentchildExercise(id_listdata)	

exercise = int(input("enter the exercise no: "))-1

def id_single_data():
	exercise_index = 0
	Slug_list = []
	while exercise_index < len(id_listdata):
		parent_Exercise = id_listdata[exercise]['name']
		parent_slug = id_listdata[exercise]['slug']
		Slug_list.append(parent_slug)
		childExerciseslist = id_listdata [exercise]['childExercises']
		print(exercise_index,parent_Exercise)
		child_index2 = 0
		while child_index2 < len(childExerciseslist):
			if "parent_exercise_id" in childExerciseslist[child_index2]:
				child_slug = childExerciseslist[child_index2]['slug']
				Slug_list.append(child_slug)
				print(5*" ",child_index2+1,"-", childExerciseslist[child_index2]['name'])
			child_index2 = child_index2 + 1
		break
		exercise_index = exercise_index + 1
	return [Slug_list]
selected_data = id_single_data()
slug_list = selected_data[0]

content = int(input("enter the exercise no to get the content: "))
print("##########-----Welcome to the content-------###############""\n")

def third_api():
	third_api = "http://saral.navgurukul.org/api/courses/" + str(user_id) + "/" + "exercise/getBySlug?slug=" + str(slug_list[content])
	
	if path.exists("childSlug/course"+(str(user_id))+".json"):
		with open("childSlug/course"+(str(user_id))+".json","r") as f:
			file_read = json.load(f)
			dic_t = json.loads(file_read)
	else:
		r_text = courses_api(third_api)
		with open("childSlug/course"+(str(user_id))+".json","w") as d:
			json.dump(r_text,d)
			dic_t = json.loads(r_text)
	print(dic_t['content'])
third_api()