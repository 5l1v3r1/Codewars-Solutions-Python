'''
challenge URL : https://www.codewars.com/kata/52f787eb172a8b4ae1000a34
'''

def zeros(num):
    count = 0
    i = 5
    if num < 0:
        return False
    while num//i > 0:
        count = count + num//i
        i = i * 5
    return count