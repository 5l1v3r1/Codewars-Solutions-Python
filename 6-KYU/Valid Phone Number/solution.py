'''
challenge URL : https://www.codewars.com/kata/525f47c79f2f25a4db000025 
'''


import re
def validPhoneNumber(phoneNumber):
     m = re.search('^\(\d{3}\)\s\d{3}-\d{4}$',phoneNumber)
     if m is None:
       return False
     elif m.group(0):
       return True
     else:
       return False