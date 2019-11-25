'''
challenge URL : https://www.codewars.com/kata/54eea36b7f914221eb000e2f
'''
def sort_it(list_, n):
      def enesima(s):
    return s[n-1]
  lista = list_.split(', ')
  return ', '.join(sorted( lista, key=enesima))