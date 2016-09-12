from bs4 import BeautifulSoup as bs
import requests


def get_products(company):
 response = requests.post('https://siftery.com/company/'+company)
 data = response.json()

 return data['response']['products'].keys()



