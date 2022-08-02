import requests

url = "https://covid-19-usa-data-by-zt.p.rapidapi.com/GetUSStateWiseData"

headers = {
	"X-RapidAPI-Key": "e655d94f7dmsh4202c0cded831b9p11bdc0jsnf8c1f5b1b9bc",
	"X-RapidAPI-Host": "covid-19-usa-data-by-zt.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.text)