'''
challenge URL : https://www.codewars.com/kata/56b1f01c247c01db92000076
'''

def double_char(s):
    d = ""
    for i in range(len(s)):
       d = d + s[i] + s[i]
    return d