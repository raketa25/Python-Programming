"""
This is a simple script that uses the os module to ping hosts and IP addresses. The user is prompted to enter a list of hosts and IP addresses, which are then pinged in an infinite loop. The results of the ping command are printed to the console, indicating whether each address is up or down. The script also includes error handling to catch any exceptions that may occur during the execution of the ping command.
Note: This script is designed to run on Unix-like operating systems (e.g., Linux, macOS) due to the use of the 'ping' command and its options. If you are using a different operating system, you may need to modify the command accordingly.

"""
import os
import time

sites = input('Hosts and IP Addresses to test:> ')

sites = sites.split(' ')
# print(sites)

while True:
    os.system('clear')
    for address in sites:
        try:
            command = (f'ping -c 1 {address}')
            # response = os.popen(command).read()
            response = os.popen(f'{command} 2> /dev/null').read()
            print(response)
            if '1 packets received' in response:
                print(f'{address} is UP!')
            else:
                print(f'{address} is DOWN!')
        except:
            print(f'{address} COMMAND FAILED!')

    time.sleep(2)
