###
###This script scrapes the customers' names and stores it in abc.txt

import requests
import numpy as np
def get_comp(request):
 data = request.json()
 companies = data['content']['companies']
 url = 'https://siftery.com/company/'
 f = open('abc.txt','a')
 g = open('domain.txt','a')
 count = 0 
 for values in companies:
  f.write(str(values)+'\n')
  r = requests.post(url + values,'html5lib')
  domain = r.json()
  #print (str(domain['response']['company']['domain']).replace('http://www.','')+'\n')
  g.write(str(domain['response']['company']['domain']).replace('http://www.','')+'\n')
  count = count + 1 
  print count
  print str(domain['response']['company']['domain']).replace('http://www.','')
 f.close()
 g.close()

if __name__ == '__main__':
 credentials = {
  'email':'4a59hh+qjd37yvstiik@sharklasers.com',
  'password':'password',
 }
 s = requests.Session()
 url = 'https://siftery.com/product-json/adroll?page='
 '''
 if (9712%30>0):
  num = range(1,((9712/30) + 1))
  print "here"
 else:
  num = range(1,9712/30)
 '''
 r = s.post('https://siftery.com/users/login', data=credentials)
 
 #print(9712/30)
 #print(np.size(num))
 #print(num)
 num1 = range(1,5)
 print num1
# print url+str(num[0])
 for i in num1:
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
