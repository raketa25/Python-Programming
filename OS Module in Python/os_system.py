"""
This code demonstrates the use of the os.system() function in Python to execute a shell command. The command being executed is "touch os-test.txt", which creates an empty file named "os-test.txt" in the current directory. The result of the command execution is printed, which typically returns 0 if the command was successful.

This code also includes a function called ping() that takes a host and an optional count parameter. It constructs a ping command based on the operating system and executes it using os.system(). The function allows you to ping a specified host a certain number of times, which can be useful for network diagnostics.
"""
import os
# import platform

# def ping(host, count=4):
#     if platform.system().lower() == "windows":
#         param = "-n"
#     else:
#         param = "-c"
#     command = f"ping {param} {count} {host}"
#     return os.system(command)

# # Usage
# ping("rtbf.be", count=4)


# command = "touch os-test.txt"
command = "ping google.com"
# command = "ping -n 4 rtbf.be"      # Windows command = "ping -c 4 rtbf.be"       

os.system(command)

result = os.system(command)

print(result)