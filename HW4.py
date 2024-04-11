#File: HW4.py
#Author: Max Allen
#UT EID: mca2773
#Course: CS303E
#I will be writing a function that prints out twin primes.

#Part 1
def is_prime(num):
    """
    Returns true if the number is prime

    Parameters
    ----------
    num: int
        the number we are investigating

    Returns
    -------
    primer: boolean
        returns true if num is prime
        returns false if not
    """
    primer = True
    for i in range(2, num):
        if(num % i == 0):
            primer = False
    if(num == 0 or num == 1):
        primer = False
    return primer

#Part 3
def twin_primes():
    """
    Prints out all prime pairs that differ by two exactly

    Parameters
    ----------
    N/A

    Returns
    -------
    N/A
    
    """
    for i in range(2, 1001):
        if(is_prime(i)):
            if(is_prime(i-2)):
               print(f"{i-2},{i}")

# I need to test whether or not my is_prime function works correctly
# Afterwords I call my function to print out every twin prime
def main():
    print(is_prime(6))
    print(is_prime(23))
    print(is_prime(2))
    twin_primes()

#Callspace
#main()

