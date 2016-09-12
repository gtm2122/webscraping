import numpy as np
import urllib
from bs4 import BeautifulSoup as bs
import requests
import pickle
import re
from swused import get_products
def get_data(company):
 #print company
 company.replace("-","")
 #re.sub('^[0-9 ]+','',company)
 url = 'https://mattermark.com/companies/'+company+'.com'
 soup = bs(requests.get(url).content,'html5lib')
 L=soup.find_all("div",class_="pill")

 tags = []
 k = 0
 for i in L:
  #print i.get_text()
  tags.append(str(i.get_text()))
  k = k + 1
 k = 0
 
 M = soup.find_all("div" , class_ = "qf-cell col-xs-6 col-md-4")
 N = soup.find_all("div", class_ = "data-label")
 facts = []
 factkey=[]
 for i in M:
  #print i.p.get_text()
  try :
   facts.append(str(i.p.get_text()))
  except UnicodeEncodeError:
   facts.append('NA')
  #if (len(i.p.get_text()) ==0):
   #facts.append('NA')
  
 count = 0
 for i in N:
  if (count<9):
   factkey.append(str(i.get_text()))
   count = count + 1
  else:
   break
 if(len(facts)==9):
  facts[2] = facts[2][:-12]
  #re.sub(' ',facts[2])
  comp_dict = {}
  comp_dict['quickfacts']={}
  comp_dict['tags']={}
  comp_dict['products']={}
  comp_dict['products'] = (get_products(company))
  #print comp_dict
  #print "HEREHRER"
  for i in range(0,9):
   #print factkey
   #print facts
   #print i
   comp_dict['quickfacts'][factkey[i]] = facts[i]
   #print comp_dict
  
  comp_dict["tags"]=tags
  #print comp_dict.keys()
  return comp_dict
 else:
  return 0

if __name__ == "__main__":
 
 f = open('abc.txt' , 'r')

 with open('abc.txt') as k:
  companies = k.read().splitlines()
 #print "companies \n"
 num_comp=len(companies)
 count = 0

 companies_dict = {}


 for i in range(0,120):
  companies_dict[companies[i]]={}
  companies_dict[companies[i]]['products']={}
  #companies[str(i)]['name']={}
  #companies[str(i)]['tags']={} 
  #companies[str(i)]['quickfacts']={}
 
 #print companies_dict

 for i in range(0,120):
  if not(get_data(companies[i])==0):
   companies_dict[companies[i]]=(get_data(companies[i]))
  else:
   count = count + 1

 with open ('adroll_customers.txt','wb') as f:  
  pickle.dump(companies_dict,f)

 with open('adroll_customers.txt', 'rb') as g:
  b = pickle.loads(g.read())
 print "Data stored in adroll_customers.txt as a dictionary with the keys 'tags','products' and 'quickfacts'"

 #number of companies that couldnt be processed
 print count
