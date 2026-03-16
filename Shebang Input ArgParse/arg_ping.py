"""
- This script is a simple ping utility that continuously pings a specified host and displays the results in the terminal. It uses the `argparse` library to handle command-line arguments, allowing the user to specify the host they want to ping. The script runs indefinitely, pinging the host every second and clearing the terminal before displaying the new results. If an error occurs during the ping command execution, it will display 'FAIL' instead of the response.
- To run this script, save it to a file named `arg_ping.py`, make it executable, and then execute it from the terminal, providing the host you want to ping as an argument.
Example usage:
$ chmod +x arg_ping.py
$ ./arg_ping.py google.com  
"""
#!/usr/bin/env python3

import argparse
import os
from time import sleep

parser = argparse.ArgumentParser(description="Ping a Host")
parser.add_argument('host', help='Enter an IP or Host Name', type=str)
args = parser.parse_args()

while True:
  try:
    command = f'ping -c 1 {args.host}'
    response = os.popen(command)
    response = response.read()
  except:
    response = 'FAIL'

  os.system('clear')
  print(command)
  print(response)
  sleep(1)