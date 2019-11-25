'''
challenge URL : https://www.codewars.com/kata/54da5a58ea159efa38000836
'''

from collections import Counter 
def find_it(seq):
  #a = [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]  
  p  = dict(Counter(seq))
  for i,j in p.items():
     if j%2!=0 :
        return i