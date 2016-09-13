import numpy as np
import time
import urllib
from bs4 import BeautifulSoup as bs
import requests
import pickle
import re
from swused import get_products

def variate(company):
 company1 = company
 #company1 = company1.replace("-1","")
 company1 = company1.replace("-","")
 return company1
def get_data(company):
 #print company
 company1 = company
 #print company
 company1 = company1.replace("-1","")
 #company1 = company1.replace("-","")
 #print company1

 #print company
 #re.sub('^[0-9 ]+','',company)
 url = 'https://mattermark.com/companies/'+company1+'.com'
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
 

 with open('abc.txt') as k:
  companies = k.read().splitlines()
 #print "companies \n"
 num_comp=len(companies)
 count = 0

 companies_dict = {}
 
 
 for i in range(0,120):
  companies_dict[companies[i]]={}
  companies_dict[companies[i]]['products']={}
  #companies_dict[companies[i]]['products']= get_products(companies[i])
  #companies[str(i)]['name']={}
  #companies[str(i)]['tags']={} 
  #companies[str(i)]['quickfacts']={}
 count1=0
 #print companies_dict
 
 f=open('not_processed.txt','w')
 for i in range(0,120):
   
  #if not(get_data(companies[i])==0):
  #time.sleep(0.5)
  a={}
  a=get_data(companies[i])
  time.sleep(0.8)
  if not(a == 0):
   count1=count1 + 1
   companies_dict[companies[i]]=a
   companies_dict[companies[i]]['products']=get_products(companies[i])
   print companies[i]
   
  else:
   #count = count + 1
   
   f.write(companies[i]+'\n')
 
 f.close()
 
 with open('not_processed.txt','r') as k:
  secndtry = k.read().splitlines()
 count = 0
 f = open('not_processed2.txt','w')
 
 for i in range(0,len(secndtry)):
  companies_dict[secndtry[i]]={} 
  companies_dict[secndtry[i]]['products']={}
 
 for i in range(0,len(secndtry)):
  mod_name = variate(secndtry[i])
  a={}
  a=get_data(mod_name)
  time.sleep(0.8)
  if not(a == 0):
   #count1=count1 + 1
   
   companies_dict[secndtry[i]]['products']=get_products(secndtry[i])
   companies_dict[secndtry[i]]=a
   count1 = count1+1
   print secndtry[i]

  else:
   count = count + 1

   f.write(secndtry[i]+'\n')
 
 f.close()


 with open ('adroll_customers.txt','wb') as f:  
  pickle.dump(companies_dict,f)

 with open('adroll_customers.txt', 'rb') as g:
  b = pickle.loads(g.read())
 #print "Data stored in adroll_customers.txt as a dictionary with the keys 'tags','products' and 'quickfacts'"
 
 #number of companies that couldnt be processed
 print count
 print count1

