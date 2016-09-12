from bs4 import BeautifulSoup as bs
import requests


def get_products(company):
 response = requests.post('https://siftery.com/company/'+company)
 data = response.json()
 #companies = data['content']['companies']

 print (data['response']['products'].keys()[1])



