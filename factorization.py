import random
'''
    Done By: Nahom Senay
    Id: GSR/4848/17
    Course: Advanced Problem Solving
    Title: Analysis on Different Factoring Algorithms
'''

def euclid_gcd(num1, num2):
    '''
        Takes two numbers num1 and num2 to calculate the greatest common 
        divisor.
        Arguments:
            num1: int
            num2: int
        Returns:
            int
    '''
    while num2:
        num1, num2 = num2, num1 % num2
    return num1

def quad_modulo(x,c,n):
    '''
        A pure helper function that calculates the quadratic modulo result which takes in three
        integers and squares the first number adds it to the second number and calculates the 
        modulo to n ===> f(x) = ((x^2 + c)mod n)
        arguments:
            x: int
            c: int
            n: int
        returns
            int
    '''
    return (x*x + c) % n



def pollards_rho(n):
    '''
        This function implements the pollard's rho method of finding a factor for a number.
        It depends on random number generated from 2, to the number provided and leveraging
        quadratic modulo function and the greatest common divisor to find the factor of the number.
        arguments:
        n: int
        return type:
        int
    '''
    # Return a non-trivial factor of n or n if none is found.
    if n % 2 == 0:
        return 2
    
    x = random.randrange(2, n)
    y = x
    c = random.randrange(1, n)
    d = 1
    while d == 1:
        x = quad_modulo(x,c,n)
        # "Tortoise and hare" iteration
        y = quad_modulo(quad_modulo(y,c,n),c,n)
        d = euclid_gcd(abs(x - y), n)
        if d == n:
            # failure, try again with a different parameter
            return pollards_rho(n)
    return d

def brute_factorize(lower_bound, n):
    '''
        This function uses brute force mechanism to find a factor between the lower bound
        and the number: n given as an argument.
        arguments:
            lower_bound:int
            n:int

    '''
    
    for i in range(lower_bound,n//2):
        if n%i == 0:
            return i
    return -1

# Example usage:
n = 10403  # 101 * 103
factor = pollards_rho(n)
print(f"One factor of {n} is {factor}")
print(brute_factorize(1345739))
