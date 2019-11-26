'''
challenge URL : https://www.codewars.com/kata/5b077ebdaf15be5c7f000077
'''

def count_sheep(n):
      s = ""
  for i in range(1,n+1):
       s = s + str(i) + " " + "sheep..."
  return s 