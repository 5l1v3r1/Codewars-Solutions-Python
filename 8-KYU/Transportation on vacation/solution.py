'''
challenge URL : https://www.codewars.com/kata/568d0dd208ee69389d000016
'''

def rental_car_cost(d):
    t = d*40
    if d>=7:
       t = t - 50
    elif d>=3 and d<=7:
       t = t-20
    return t