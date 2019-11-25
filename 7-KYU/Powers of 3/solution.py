'''
challenge URL : https://www.codewars.com/kata/57be674b93687de78c0001d9
'''

def largestPower(N):
    for i in range(0,100):
        l = pow(3,i)
        if l>=N:
          return i-1