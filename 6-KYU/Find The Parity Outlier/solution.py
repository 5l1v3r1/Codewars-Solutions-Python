'''
challenge URL : https://www.codewars.com/kata/5526fc09a1bbd946250002dc
'''


def find_outlier(integers):
    ec = 0 
    for i in range(3):
       if integers[i] % 2 ==0:
          ec = ec + 1 
    if ec > 1 :
      for i in range(len(integers)):
          if integers[i] % 2 !=0:
             result = integers[i]
    else:
      for i in range(len(integers)):
          if integers[i]%2==0:
            result = integers[i]
    return result