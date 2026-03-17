"""
This code demonstrates how to use regular expressions in Python to extract IP addresses from a string. We are using the `re` module to define a pattern that matches the format of an IP address, which consists of four groups of 1 to 3 digits separated by dots. The `re.findall()` function is used to find all occurrences of the pattern in the input string, and we print the first IP address found in the response from the ping command.

"""
import os
import re

site = 'rtbf.be'
command = f"ping -c 1 {site}"
response = os.popen(command).read()

print(response)
print('\n')

pattern = r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}'
ip_result = re.findall(pattern, response)
print(f'{site} IP Address is {ip_result[0]}')