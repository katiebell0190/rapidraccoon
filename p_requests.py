#HTTP REQUEST
#GET - requests and retrieves data from a server
#HEAD - the message body is not included
#POST - sends data to server

from wsgiref import headers
import requests
import json


#try:
#     r = requests.get('https://google.com/python')
#     r.raise_for_status()
# except requests.exceptions.HTTPError as http_error:
#     print(http_error)
# else:
#     print(r.status_code)

#r = requests.get('https://python.org/static/community_logos/python-logo-master-v3-TM.png')
# with open('python_logo.png','wb') as write_file:
#     write_file.write(r.content)
#     print('[+] File downlaoded successfully!')

# domain = 'https://google.com'

# r= requests.get(domain)
# print(r.url)
# print(r.encoding)
# print(r.elapsed) #amount of time it took to load
# print(r.cookies) #webtracker used to record user behavior

# domain = 'https://google.com'

#HEADERS 
# r = requests.get(domain)
# for i in r.headers.items():
#     print(i)

#API - Application Programming Interface

# API_KEY = '7d10f71a-a044-43cb-9403-6dca093a73a4' #capital letters = a constanct - API keys can be revoked this increases security
# URL = 'https://pro-api.coinmarketcap.com/v1/crpytocurrency/quotes/latest'
# parameter = {
#     'convert': 'USD',
#     'symbol':'BTC',
#     'CMC_PRO_API_KEY': API_KEY
# }
# response = requests.get(URL,params=parameter)
# data = json.loads(response.text)
# print(data['data']['BTC']['quote']['USD']['price'])

#Return price 1 oz of gold, 1 oz of silver 


# URL = 'https://metals-api.com/api/latest'
# base_currency = 'USD'
# symbol1 = 'XAU'
# symbol2 = 'XAG'
# endpoint = 'latest'
# access_key = 'd2yvgtb1097fgq9d62d5if41qy65a54qti23rtdf5du5vymt5bel62p3h0qz'

# response = requests.get(
#     'https://metals-api.com/api/'+endpoint+'?access_key='+access_key+'&base='+base_currency+'&symbols='+symbol1)
# resp2 = requests.get(
#     'https://metals-api.com/api/'+endpoint+'?access_key='+access_key+'&base='+base_currency+'&symbols='+symbol2)
# # data =json.loads(response.text)
# # print(response)
# # #paramter = {}

# print(f"Gold: ${round(1/(response.json()['rates']['XAU']),2)}") #How do I format these to round ? 
# print(1/(resp2.json()['rates']['XAG']))

# URL = 'https://httpbin.org/post'
# response = requests.post(URL)
# print(response.status_code)
# print(response.ok)
# #to send data it has to be in the form of a dictionary

# URL = 'https://httpbin.org/post'
# params = {'Jello':'World'}
# response = requests.post(URL,params=params)
# print(response.text)

# import datetime

# URL = 'https://httpbin.org/post'
# params = {'Time': f"{datetime.datetime.now()}"}
# response = requests.post(URL,params=params)
# print(type(response.text))
# print(type(response.json()))

#PARAMETER (data in args)
# URL = 'https://httpbin.org/post'
# params = {'username':'jsmith',
#             'password':'abc123'
#             }
# response = requests.post(URL,params=params)
# print(response.text)

#DATA (data in form)
# URL = 'https://httpbin.org/post'
# payload = {'username':'jsmith',
#             'password':'abc123'
#             }
# response = requests.post(URL,data=payload)
# print(response.text)

#HEADERS
URL = 'https://httpbin.org/post'
header = {'content-type':'multipart/form-data'}
response = requests.post(URL,headers=header)
#print(response.request.headers)
#print(response.headers)
print(response.headers['content-type'])

#RAPID API
#Go to website we couldn't access and play with it
#Go to the metals one and return some other metals
#Get familiar
