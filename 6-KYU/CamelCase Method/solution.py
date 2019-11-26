'''
challenge URL : https://www.codewars.com/kata/587731fda577b3d1b0001196
'''

def camel_case(string):
    s = string 
    t = s.split()
    l = []
    new_string = ""
    for i in range(len(t)):
       new = t[i][0].upper()
       l.append(new)
    for i in range(len(t)): 
       new_string = new_string + l[i] + t[i][1:]
    return new_string