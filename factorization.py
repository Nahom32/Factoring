import random
import time
import math
import matplotlib.pyplot as plt
'''
    Done By: Nahom Senay
    Id: GSR/4848/17
    Course: Advanced Problem Solving
    Title: Analysis on Different Factoring Algorithms
'''
def is_square(n):
    """Return True if n is a perfect square."""
    x = math.isqrt(n)
    return x * x == n



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
    
    while True:
        x = random.randrange(2, n)
        y = x
        c = random.randrange(1, n)
        d = 1
        while d == 1:
            x = quad_modulo(x,c,n)
            y = quad_modulo(quad_modulo(y,c,n),c,n)
            d = euclid_gcd(abs(x - y), n)
        if d != n:
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


def fermat_factor(n):
    """
    Fermat's factorization method.
    Assumes n is an odd composite number.
    Finds a and b such that n = (a+b) * (a-b),
    where a is the smallest integer >= sqrt(n) for which a^2 - n is a perfect square.
    Returns a tuple (factor1, factor2).
    """
    a = math.isqrt(n)
    if a * a < n:
        a += 1
    b2 = a * a - n
    while not is_square(b2):
        a += 1
        b2 = a * a - n
    b = math.isqrt(b2)
    return (a - b, a + b)

def profile_algorithms(composites):
    pollard_times = []
    brute_times = []
    n_values = []
    
    for n in composites:
        n_values.append(n)
        
        # Measure Pollard's Rho time
        start = time.perf_counter()
        factor1 = pollards_rho(n)
        end = time.perf_counter()
        t_pollard = end - start
        pollard_times.append(t_pollard)
        
        # Measure brute-force (trial division) time
        start = time.perf_counter()
        factor2 = brute_factorize(11,n)
        end = time.perf_counter()
        t_brute = end - start
        brute_times.append(t_brute)
        
        print(f"n = {n}: Pollard's Rho found factor {factor1} in {t_pollard:.6f} s; "
            f"Trial division found factor {factor2} in {t_brute:.6f} s")

    # Plot the results.
    plt.figure(figsize=(10, 6))
    # Optionally, you could use log-scale for x-axis if the numbers vary widely.
    plt.plot(n_values, pollard_times, marker='o', label="Pollard's Rho")
    plt.plot(n_values, brute_times, marker='s', label="Trial Division")
    plt.xlabel("Composite Number (n)")
    plt.ylabel("Time (seconds)")
    plt.title("Comparison of Factorization Algorithms in Relation to Time")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def composite_generator(rng_value):
    '''
        Generates Composite values provided the magnitude wanted for test cases
        Arguments:
            rng_value: int
        Returns:
            List[int]
    '''
    composites = []
    for _ in range(20):
        a = random.randint(1000, 5000)
        d = random.randint(0, 50)  # small difference
        b = a + d
        n = a * b
        # Ensure n is odd (Fermat's method requires an odd number)
        if n % 2 == 0:
            continue
        composites.append(n)
    composites.sort()
    return composites


profile_algorithms([10403,22499,100151,1031407,10070001])

# Example usage:
n = 10403  # 101 * 103
factor = pollards_rho(n)
print(f"One factor of {n} is {factor}")
print(brute_factorize(11,345739))
