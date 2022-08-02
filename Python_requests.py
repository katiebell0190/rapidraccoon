#AUTHENTICATION
#AUTHORIZATION VS AUTHENTICATION
#1.BASIC
#import requests
# URL = 'HTTPS://cat-fact.herokuapp.com/facts'
# response = requests.get(URL)
# print(response.json())

# URL = 'HTTPS://cat-fact.herokuapp.com/facts'
# response = requests.get(URL)
# for id,item in enumerate(response.json()):
#     print(id+1,item['text'])


#2. API BASED 
    # more secure than previous example

# from wsgiref import headers
# import requests
# import dotenv
# import os 

# #loading values from.env
# dotenv.load_dotenv(dotenv.find_dotenv()) #shold be in every code you write from now in if you have secrets#
# API_KEY = os.getenv('X-RapidAPI-Key')

# url = "https://community-open-weather-map.p.rapidapi.com/weather"

# querystring = {"q":"Los Angeles,usa","callback":"test","id":"2172797","units":"imperial","mode":"xml"}

# headers = {
# 	"X-RapidAPI-Key": API_KEY,
# 	"X-RapidAPI-Host": "community-open-weather-map.p.rapidapi.com"
# }

# response = requests.request("GET", url, headers=headers, params=querystring)

# print(response.text)

#3. TOKEN

# dotenv.load_dotenv(dotenv.find_dotenv())
# token = os.getenv('token')
# channel_id = '959537950914404372'
# message = 'katie bell waz'

# def sendmessage(token,channel_id,message):
# 	URL = 'https://discord.com/api/v8/channels/{}/messages'.format(channel_id)
# 	data = {'content':message}
# 	headers = {'authorization': token}

# 	r = requests.post(URL,data=data, headers=headers)
# 	print(r.status_code)
# sendmessage(token,channel_id,message)

#querystring = {"secret":"GXPTBCTI4DX4UFJB","issuer":"AcmeCorp","account":"JohnDoe"}

#4. OAUTH

# import requests
# #GENERATE SECRET
# dotenv.load_dotenv(dotenv.find_dotenv())
# API_KEY = os.getenv('X-RapidAPI-Key')


# def genereate_secret():
# 	URL = "https://google-authenticator.p.rapidapi.com/new/"
# 	headers = {
# 		"X-RapidAPI-Key": API_KEY,
# 		"X-RapidAPI-Host": "google-authenticator.p.rapidapi.com"
# 	}

# 	response = requests.request("GET", URL, headers=headers, params=headers)
# 	return response.text[17:].strip()
# secret = genereate_secret()
# print(secret)

#ENROLL

# def enroll():
# 	url = "https://google-authenticator.p.rapidapi.com/enroll/"
# 	querystring = {"secret":secret,"issuer":"AcmeCorp","account":"JohnDoe"}
# 	headers = {
# 		"X-RapidAPI-Key": API_KEY,
# 		"X-RapidAPI-Host": "google-authenticator.p.rapidapi.com"	
# 	}
# 	response = requests.request("GET", url, headers=headers, params=querystring)

# 	print(response.text)
# enroll()


# def validate(code):
# 	url = "https://google-authenticator.p.rapidapi.com/validate/"
# 	querystring = {"code":code, "secret":secret}
# 	headers = {
# 		"X-RapidAPI-Key": API_KEY,
# 		"X-RapidAPI-Host": "google-authenticator.p.rapidapi.com"	
# 	}
# 	response = requests.request("GET", url, headers=headers, params=querystring)
# 	if code:
# 		print(response.text)
# 	else:
# 		print('Invalid code.')
# validate(code=input('Enter code: '))


#SESSIONS 
##Send cookies to the server & check if they are there

#SET COOKIES 
from re import S
import requests

# URL = 'https://httpbin.org/cookies/set'
# params = {
# 	'username': 'admin',
# 	'location': 'Los Angeles'
# }
# set_cookie = requests.get(URL,params=params)
# print('tracker: {}'.format(set_cookie.text))



#USING SESSIONS
	#how to read/write files to disk - what is the syntax 
	#now it isn't a request it is a Session
with requests.Session() as s:
	#SET COOKIES
	URL = 'https://httpbin.org/cookies/set'
	params = {
		'username': 'admin',
		'location': 'Los Angeles'
	}
	set_cookie = s.get(URL,params=params)
	print('tracker: {}'.format(set_cookie.text))

#FETCH COOKIES
get_cookies = S.get('https://httpbin.org/cookies')
print('tracker: {}'.format(get_cookies.text))

