###
###This script scrapes the customers' names and stores it in abc.txt

import requests
import numpy as np
def get_comp(request):
 data = request.json()
 companies = data['content']['companies']
 f = open('abc.txt','a')
 for values in companies:
  f.write(str(values)+'\n')
 f.close()

if __name__ == '__main__':
 credentials = {
  'email':'4a59hh+qjd37yvstiik@sharklasers.com',
  'password':'password',
 }
 s = requests.Session()
 url = 'https://siftery.com/product-json/adroll?page='
 if (9712%30>0):
  num = range(1,((9712/30) + 1))
  print "here"
 else:
  num = range(1,9712/30)
 
 r = s.post('https://siftery.com/users/login', data=credentials)
 
 print(9712/30)
 print(np.size(num))
 print(num)
# print url+str(num[0])
 for i in num:
  r = s.post(url + str(i))
  
  
  get_comp(r)  
  
  
  
#with open('abc.txt') as f:
 #lines = f.read().splitlines()
 
#print lines

#p = "CUSTOMERS"

#f = open('abc.txt','w')
#f.write(page.content)
#m = re.search(p,html)
#if m:
# print "ok"
# print(m.group(1))
