'''
challenge URL : https://www.codewars.com/kata/57a5015d72292ddeb8000b31
'''

def is_palindrome(string):
    string = str(string)
    l = string[::-1]
    if l == string: 
      return True
    else : 
      return False 