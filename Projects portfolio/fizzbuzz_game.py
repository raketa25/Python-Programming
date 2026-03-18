for number in range(12, 101):
    if number % 3 == 0 & number % 5 == 0:
        print("FIzzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

