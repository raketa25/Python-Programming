"""
This code defines a function `price_stat` that takes a list of prices as input and calculates the highest price, lowest price, and average price. The function returns these three values as a tuple. The code then creates a list of prices, calls the `price_stat` function with this list, and prints the results in a formatted string.
"""
def price_stat(price):
    high = max(price)
    low = min(price)
    average = sum(price) / len(price)
    return high, low, average

price = [11.20, 55.60, 27.33, 25.66]

response = price_stat(price)

print(response)

print(f'max: {response[0]} min: {response[1]} avg: {response [2]}')