"""
This code defines a function `my_math` that takes two parameters, `num1` and `num2`, and returns their sum. The function is then called with the variables `price1` and `price2`, which are set to 885.120 and 90.450, respectively. Finally, the total price is printed to the console, formatted to three decimal places.
"""
def my_math(num1, num2):
    answer = num1 + num2
    return answer

price1 = 885.120
price2 = 90.450

response = my_math(price1, price2)

print(f'The total price is {response:.3f}')