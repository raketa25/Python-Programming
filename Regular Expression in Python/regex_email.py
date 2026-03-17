"""
This code uses the `re` module to find all email addresses in a given string. The regular expression pattern used is `[A-Za-z0-9]+@[A-Za-9]+\.[A-Za-z]+`, which matches sequences of letters and numbers followed by an '@' symbol, then more letters and numbers, a dot, and finally more letters. The `re.findall()` function returns a list of all matches found in the input string.

"""
import re

message = 'petrovich@example.com Jack zpm25@raketa.com Chloe picture@domain.com'

result = re.findall(r'[A-Za-z0-9]+@[A-Za-9]+\.[A-Za-z]+', message)

print(result)