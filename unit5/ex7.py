import requests
import json

api_key = 'eo1CqVWXLl0r32VnrxWvQjl9EnaQ_sI1GarSgJX6dtdIZ97ite5b1UNtt9KesBYLWMKXyRiSp-29RLk6s5mE0Zmuja5yn6Qmm0kKuuTPB167isWKPVZLXYekdWC7XHYx'

headers = {'Authorization': 'Bearer %s' %api_key}

url = 'https://api.yelp.com/v3/businesses/I3_QvspB0SsqiUTN18-TlQ/reviews'

params = {'term':'seafood','location':'New York City'}

#Making a GET request to the yelp API

req = requests.get(url, params = params, headers = headers )
print(json.loads(req.text))