"""
This is a sets of 
"""
# Functions reviewed and optimized for performance and readability.
def calculate_factorial(n):    
    """Calculate the factorial of a non-negative integer n."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def fibonacci_sequence(n):
    """Generate a list containing the Fibonacci sequence up to n terms."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    sequence = [0, 1]
    for _ in range(2, n):
        next_value = sequence[-1] + sequence[-2]
        sequence.append(next_value)
    return sequence

def gcd(a, b):
    """Compute the greatest common divisor (GCD) of two integers a and b."""
    while b:
        a, b = b, a % b
    return abs(a)

def lcm(a, b):
    """Compute the least common multiple (LCM) of two integers a and b."""
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)

def reverse_string(s):
    """Return the reverse of the input string s."""
    return s[::-1]  

def is_palindrome(s):
    """Check if the input string s is a palindrome."""
    cleaned_s = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned_s == cleaned_s[::-1]

def sum_of_squares(n):
    """Calculate the sum of squares of the first n natural numbers."""
    if n < 1:
        return 0
    return sum(i * i for i in range(1, n + 1))

def prime_factors(n):
    """Return a list of prime factors of the given integer n."""
    factors = []
    # Check for number of 2s that divide n
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    # n must be odd at this point, so we can skip even numbers
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 2:
        factors.append(n)
    return factors


def my_function():
    print("Hello")
    print("Bye.")

my_function()
calculate_factorial(5)
is_prime(29)    
fibonacci_sequence(10)
gcd(48, 18)
lcm(12, 15)
reverse_string("Hello")
is_palindrome("A man, a plan, a canal: Panama")
sum_of_squares(5)
prime_factors(56)
