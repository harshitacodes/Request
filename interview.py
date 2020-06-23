import requests
import json
import random

url = "http://saral.navgurukul.org/api/courses"

def get_saral_url(link):
	res = requests.get(link)
	return res.text
response_text = get_saral_url(url)

dictionary_data = json.loads(response_text)
coursesList = (dictionary_data['availableCourses'])
 

def logo_list():
    index =0
    courses_list = []
    while index < len(coursesList):
        logo = coursesList[index]['name']
        courses_list.append(logo)
        index = index + 1
    return courses_list
data = logo_list()

i = 0
while i < len(data):
    d = random.choice(data)
    print(d)
    i = i + 1
