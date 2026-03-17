def get_name():
    while True:
        name = input("Enter your name:> ")
        if name.isalpha():
            return name
        else:
            print("Only Letters are allowed for names")

def get_age():
    while True:
        age = input("Enter your age:> ")
        try:
            age = int(age)
            return age
        except:
            print("Only numbers are allowed for age")

def get_phone():
    while True:
        phone = input("Enter your phone number:> ")
        phone = phone.replace('-', '')
        if len(phone) == 9 or len(phone) == 10:
            try:
                phone = int(phone)
                return phone
            except:
                print("Phone Numbers must be Numeric digits")
        else:
            print("Phone numbers must be 9 - 10 digits long")

def get_email():
    while True:
        email = input("Enter your email:> ")
        if '@' in email and '.' in email:
            return email
        else:
            print("Please enter a valid email address")

def get_password():
    while True:
        password = input("Enter your password:> ")
        if len(password) >= 8:
            return password
        else:
            print("Password must be at least 8 characters long")

# Example usage:
# if __name__ == "__main__":
#     name = get_name()
#     age = get_age()
#     phone = get_phone()
#     email = get_email()
#     password = get_password()

#     print(f"Name: {name}")
#     print(f"Age: {age}")
#     print(f"Phone: {phone}")
#     print(f"Email: {email}")
#     print(f"Password: {'*' * len(password)}")  # Mask the password when displaying

user_name = get_name()

user_age = get_age()

user_phone = get_phone()

user_email = get_email()

user_password = get_password()

print('============== User Informations ==============')
print(f"Name: {user_name}")
print(f"Age: {user_age}")
print(f"Phone: {user_phone}")
print(f"Email: {user_email}")
# print(f"Password: {'*' * len(user_password)}")  # Mask the password when displaying
