"""
In this code, we are using regular expressions to extract IP addresses from a given string. We have three different patterns to match the IP addresses, and we use the `re.findall()` function to find all occurrences of the pattern in the input string.

1. The first pattern `[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{0,3}` matches sequences of 1 to 3 digits followed by a dot, repeated three times, and then followed by 0 to 3 digits. This pattern may not be very strict and can match invalid IP addresses.

2. The second pattern `\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}` is similar to the first one but uses `\d` to match digits, which is a shorthand character class for `[0-9]`.

3. The third pattern `\b(?:\d{1,3}.){3}\d{1,3}\b` is more precise. It uses a non-capturing group `(?:...)` to match three occurrences of 1 to 3 digits followed by a dot, and then matches 1 to 3 digits at the end. The `\b` at the beginning and end ensures that we are matching whole words, which helps to avoid matching parts of larger numbers or strings that are not valid IP addresses.

"""
import re

ip_message = 'the ip address is 192.168.1.1 and 10.1.10.1'

pattern = r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{0,3}'
ip_result = re.findall(pattern, ip_message)
print(ip_result)

pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'              
ip_result = re.findall(pattern, ip_message)
print(ip_result)

pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'                     # this is the best pattern to match IP addresses
ip_result = re.findall(pattern, ip_message)
print(ip_result)