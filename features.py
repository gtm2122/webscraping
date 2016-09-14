import numpy as np
import time
import urllib
from bs4 import BeautifulSoup as bs
import requests
import pickle
import re
from swused import get_products

def get_data(company):
 #print company
 
 company1 = company
 url = 'https://mattermark.com/companies/'+company1
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
 with open('domain.txt') as l:
  domains = l.read().splitlines()
 
 num_comp=len(companies)
 count = 0

 companies_dict = {}
 
 
 for i in range(0,120):
  companies_dict[companies[i]]={}
  companies_dict[companies[i]]['products']={}
  count1=0
 #print companies_dict
 
 f=open('not_processed.txt','w')
 for i in range(0,120):
   
  #if not(get_data(companies[i])==0):
  time.sleep(0.8)
  a={}
  a=get_data(domains[i])
  time.sleep(0.8)
  if(a):
   count1=count1 + 1
   companies_dict[companies[i]]=a
   companies_dict[companies[i]]['products']=get_products(companies[i])

  if (not(a) and not(companies[i][-1] == 'm' and companies[i][-2] == 'o' and companies[i][-1] == 'c')):
   b = domains[i]
   print b
   pos = b.find('.')
   print pos
   c=['.','c','o','m']
   b = list(b)
   #c[pos+1] = 'c'
   #c[pos+2] = 'o'
   #c[pos+3] = 'm'
   b = b[0:pos]
   print b
   b.append(c[0])
   b.append(c[1])
   b.append(c[2])
   b.append(c[3])
   print b
   b = ''.join(b)
   print b,type(b)
   #b = "".join(b)
   #b = b.join(c)
   print "careful!"
   print(b)
   a = get_data(b)
   
  if (a):
   count1=count1 + 1
   companies_dict[companies[i]]=a
   companies_dict[companies[i]]['products']=get_products(companies[i])

  
  else :
    count = count + 1
    print "not processed -->",companies[i]
    f.write(companies[i]+'\n')
 f.close()
 
 with open ('adroll_customers.txt','wb') as f:  
  pickle.dump(companies_dict,f)

 with open('adroll_customers.txt', 'rb') as g:
  b = pickle.loads(g.read())
 #print "Data stored in adroll_customers.txt as a dictionary with the keys 'tags','products' and 'quickfacts'"
 
 #number of companies that couldnt be processed
 print "not processed = ", count
 print "processed = ",count1

