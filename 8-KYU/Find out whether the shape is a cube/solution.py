'''
challenge URL : https://www.codewars.com/kata/58d248c7012397a81800005c
'''
def cube_checker(volume, side):
    if side <= 0:
      return False 
    elif side>0:
      if (pow(side,3) == volume):
         return True
      else : 
         return False 