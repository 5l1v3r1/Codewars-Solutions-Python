'''
challenge URL : https://www.codewars.com/kata/5769b3802ae6f8e4890009d2
'''

def remove_every_other(my_list):
    l = []
    for i in range(len(my_list)):
       if i % 2 == 0:
           l.append(my_list[i])
    return l