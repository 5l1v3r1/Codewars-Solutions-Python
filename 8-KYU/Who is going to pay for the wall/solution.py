'''
challenge URL : https://www.codewars.com/kata/58bf9bd943fadb2a980000a7
'''
def who_is_paying(name):
    l = []
    if len(name) <=2 : 
       l.append(name)
       return l
    else : 
        l.append(name)
        l.append(name[0:2])
        return l 