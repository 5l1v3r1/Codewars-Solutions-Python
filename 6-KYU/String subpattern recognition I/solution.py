'''
challenge URL : https://www.codewars.com/kata/5a49f074b3bfa89b4c00002b
'''

import re
def has_subpattern(string):
    return bool(re.match(r'(.+)\1+$', string))