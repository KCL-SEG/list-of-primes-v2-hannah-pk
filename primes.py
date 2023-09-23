"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError("The number of primes should be 1 or greater")
    list = []
    y = 1
    while len(list) < 10:
        y +=1
        if is_prime(y,list):
            list.append(y)
    return list

def is_prime(number,primes):
    for item in primes:
        if number % item == 0:
            return False
    return True
