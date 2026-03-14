"""
Everything in python actually works with modules.

This lesson is deicated to address exactly that.

- The famous python modules are : math, random, datetime, os, sys, time, re, json, csv, requests, numpy, pandas, matplotlib and many more.

- Modules installation : pip install module_name

- Importing modules : import module_name

- Important web page to look at : https://pypi.org/

- Install PIP3 on Ubuntu: sudo apt install python3-pip

- Important note : pip vs pip3 is the same thing, but pip3 is used to specify that you want to install packages for Python 3.x, while pip can refer to either Python 2.x or Python 3.x depending on your system configuration.

- Example of using pip3 in Ubuntu: pip3 install numpy, pip3 install openai, pip3 install matplotlib, pip3 install openCV-python

Also, you can use pip to install packages in a virtual environment, which is a self-contained Python environment that allows you to manage dependencies for different projects separately. To create a virtual environment, you can use the following command:

python3 -m venv myenv

This will create a new virtual environment called "myenv". To activate the virtual environment, you can use the following command:

source myenv/bin/activate

Once the virtual environment is activated, you can use pip to install packages as usual, and they will be installed in the virtual environment rather than globally on your system. To deactivate the virtual environment, you can use the following command:

deactivate  

- pip3 install module_name vs apt install app_name : pip3 is used to install Python packages, while apt is used to install system packages on Ubuntu. They serve different purposes and are not interchangeable. Also Django is a Python web framework, so you would use pip3 to install it, not apt.

- Uninstalling modules : pip uninstall module_name

- SECURITY WARNING : Be cautious when installing packages from untrusted sources, as they may contain malicious code. Always verify the source and read reviews before installing any package.

NOTE: Insfrastructure as code (IaC) is a practice in which infrastructure is provisioned and managed using code and automation tools. This allows for more efficient and consistent management of infrastructure resources, as well as easier collaboration and version control. Popular IaC tools include Terraform, Ansible, and CloudFormation.
So Architecture is really important in software development, and it can be achieved through the use of modules and packages in Python. By organizing code into modules and packages, developers can create reusable and maintainable code that can be easily shared and collaborated on with other developers. This can lead to faster development times, improved code quality, and better overall software architecture. Understand what Architecture means in software development is crucial for any developer, and it can be achieved through the use of modules and packages in Python. By organizing code into modules and packages, developers can create reusable and maintainable code that can be easily shared and collaborated on with other developers. This can lead to faster development times, improved code quality, and better overall software architecture.

- Build your own architecture for your business for security and scalability : By designing a modular architecture for your business, you can ensure that your systems are secure and scalable. This can involve breaking down your systems into smaller, more manageable components that can be easily maintained and updated. Additionally, by implementing security best practices such as encryption, access controls, and regular security audits, you can help protect your business from cyber threats and ensure the safety of your data and customers.

- Design your own system architecture for your business : By designing a modular architecture for your business, you can ensure that your systems are secure and scalable. This can involve breaking down your systems into smaller, more manageable components that can be easily maintained and updated. Additionally, by implementing security best practices such as encryption, access controls, and regular security audits, you can help protect your business from cyber threats and ensure the safety of your data and customers.

Build your own module : You can create your own module by simply creating a Python file with a .py extension and defining functions, classes, or variables in it. For example, you can create a file called my_module.py and define a function called greet() in it:
# my_module.py
def greet(name):
    return f'Hello, {name}!'
Then, you can import this module in another Python file and use the greet() function:
# main.py
import my_module
name = 'Alice'
greeting = my_module.greet(name)
print(greeting)  # Output: Hello, Alice!    
"""

from random import *                                         # Importing all functions from the random module. 
# from random import randint
import random

number = random.randint(0, 100)
print(f'Random number between 0 and 100: {number}')
print("\n")

# Using aliases for modules
# import random as rnd
# number = rnd.randint(0, 100)
# print(f'Random number between 0 and 100 using alias: {number}')
# print("\n")

# Solving a simple problem using random module : create a self updating clock
import os
import datetime
import time

while True:
    os.system('clear')
    timestamp = datetime.datetime.now()
    print(f'The current time is {timestamp}')
    time.sleep(1)                                           # waiting time before update


"""
- Namespace : A namespace is a container that holds a set of identifiers (names) and their corresponding objects. In Python, modules create their own namespaces, which means that the names defined in a module are not accessible outside of that module unless they are explicitly imported.

- Variables names : Careful not to use the same variable names in different modules, as this can lead to confusion and errors. It's a good practice to use descriptive variable names that are unique to each module.

- Files Names : Careful not to use the same file names for different modules, as this can lead to confusion and errors. It's a good practice to use descriptive file names that are unique to each module.
"""
