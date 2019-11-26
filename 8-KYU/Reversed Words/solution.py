'''
challenge URL : https://www.codewars.com/kata/51c8991dee245d7ddf00000e
'''

def reverseWords(str):
    s = str.split()
    sum = ""
    l = s[::-1]
    for i in range(len(l)):
      sum = sum + l[i] + ' ' 
    return sum.strip()