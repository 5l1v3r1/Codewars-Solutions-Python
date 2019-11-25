'''
challenge URL : https://www.codewars.com/kata/5a00e05cc374cb34d100000d
'''

def reverse_seq(n):
    l = []
    for i in range(1,n+1):
        l.append(i)
    return l[::-1]