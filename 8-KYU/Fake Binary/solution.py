'''
challenge URL  : https://www.codewars.com/kata/57eae65a4321032ce000002d
'''

import re
def fake_bin(x):
  str1 = ""
  x = str(x)
  r = re.findall("\d{1}",x)
  for i in range(len(r)):
    if int(r[i]) >= 5 : 
      r[i] = "1" 
    else : 
      r[i] = "0"
  return str1.join(r) 