import requests

api_url = "https://covid-19-data.p.rapidapi.com/report/country/name"
country = input("What Country do you want to see? ")
date = input("Please input the date YYYY-MM-DD = ")

querystring = {"date-format":"YYYY-MM-DD","format":"json"}
querystring["date"] = date 
querystring["name"] = country

headers = {
    'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
    'x-rapidapi-key': "37445013d6msh7d3a4609c289d76p1822d1jsn9b0afe20de80"
    }

response = requests.request("GET", api_url, headers=headers, params=querystring)
print()
print()
print()
print(response.text)
print()
print()
print()
print()