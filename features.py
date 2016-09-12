import urllib
from bs4 import BeautifulSoup as bs
import requests

def get_data(company):
 url = 'https://mattermark.com/companies/'+company+'.com'
 soup = bs(requests.get(url).content,'html5lib')
 L=soup.find_all("div",class_="pill")
 tags = {}
 for i in L:
  tags[i] = {}

 tags = []
 k = 0
 for i in L:
  tags.append(str(i.get_text()))
  k = k + 1
 k = 0

 print tags

 M = soup.find_all("div" , class_ = "qf-cell col-xs-6 col-md-4")
 N = soup.find_all("div", class_ = "data-label")
 facts = []
 factkey=[]
 for i in M:
  facts.append( str(i.p.get_text()))
 count = 0
 for i in N:
  if (count<9):
   factkey.append(str(i.get_text()))
   count = count + 1
  else:
   break
 
 facts[2] = facts[2][:-12]
 return factkey,facts


f = open('abc.txt' , 'r')
with open('abc.txt') as k:
 companies = k.read().splitlines()
#print "companies \n"
get_data(companies[1])

