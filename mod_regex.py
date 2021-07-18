import re
from typing import Text

text = '''
This is a beautiful data
1212112
hello world
'''
pattern = re.compile(r'\d')     # \d matches only numbers

pattern = re.compile(r'\D')     # \D matches only characters

match = pattern.findall(text)

print(match)

'''
\d  -> find digit
\D  -> find everthing execpt digit
\w  -> find word
\W  -> find everthing except character
\s  -> find white space
\S  -> find everthing except white space 
.   -> matches everything 
\.  -> matches . in string
*   -> matches everything
'''