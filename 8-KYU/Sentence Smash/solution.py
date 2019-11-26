'''
challenge URL : https://www.codewars.com/kata/53dc23c68a0c93699800041d
'''

def smash(words):
    s = ""
    for i in range(len(words)):
      s = s + words[i] + ' '
    return s.strip()