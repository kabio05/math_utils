def isprime(n):
    """Return whether n is a prime number"""
    from math import sqrt 
    # exclude invalid cases
    if n <= 0 or n != int(n):
        return "Argument is not a positive integer"
    # exclude extreme case 
    if n == 1:
        return False
    if n == 2 or n == 3:
        return True
    # check whether the number is zero modulo any of the integers less than its square root
    for k in range(2,int(sqrt(n))+1):
        if n % k == 0:
            return False 
    return True
