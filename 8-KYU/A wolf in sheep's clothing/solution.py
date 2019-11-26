'''
challenge URL : https://www.codewars.com/kata/5c8bfa44b9d1192e1ebd3d15           
'''

def warn_the_sheep(queue):
    l = len(queue)
    if queue[l-1] == "wolf":
      return "Pls go away and stop eating my sheep"
    else : 
        for i in range(len(queue)):
           if queue[i] == "wolf":
              a = len(queue) - (i+1)
              return 'Oi! Sheep number ' + str(a) + '! You are about to be eaten by a wolf!'