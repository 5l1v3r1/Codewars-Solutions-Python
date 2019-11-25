'''
challenge URL : https://www.codewars.com/kata/578aa45ee9fd15ff4600090d
'''

def sort_array(source_array):
     odd = []
     for i in range(len(source_array)):
         if (source_array[i] %2 != 0):
             odd.append(source_array[i])
     odd.sort()
     l = len(odd)
     k =0
     for i in range(len(source_array)):
         if (source_array[i] %2!=0):
             source_array[i] = odd[k]
             k = k + 1 
     return source_array 