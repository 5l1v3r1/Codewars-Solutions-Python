'''
challenge URL : https://www.codewars.com/kata/52756e5ad454534f220001ef
'''

def lcs(x, y):
      res=[]
  i=0
  for item in y:
     if item in x[i:]:
        res+=[item]
        i=x.index(item)+1
  return "".join(res)