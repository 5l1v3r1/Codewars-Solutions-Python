'''
challenge URL : https://www.codewars.com/kata/59706036f6e5d1e22d000016
'''

import re 
from string import ascii_lowercase
def words_to_marks(s):
  b = ascii_lowercase
  r = re.findall("\w{1}",b)
  l = []
  for i in range(len(s)):
    l.append(r.index(s[i]) + 1)
  return sum(l)