"""
This code demonstrates how to use the os.popen() function to execute a system command and read its output. In this case, it prompts the user for a host or IP address to ping, constructs the appropriate ping command, and then executes it using os.popen(). The output of the command is read and printed to the console. The ping command is constructed with the '-c 1' option, which tells it to send only one ping request to the specified host. This can be useful for quickly checking if a host is reachable without sending multiple requests.

"""
import os

host = input('Host / IP Address to ping:> ')
command = (f'ping -n 1 {host}')
response = os.popen(command).read()

print(response)