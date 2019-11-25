'''
challenge URL  : https://www.codewars.com/kata/515de9ae9dcfc28eb6000001 
'''

import re
def solution(s):
    if len(s)%2==0:
       r = re.findall("\w{2}",s)
       return r
    else:
       new_r = re.findall("\w{2}",s[:-1])
       new_r.append(s[len(s)-1] + "_")
       return new_r