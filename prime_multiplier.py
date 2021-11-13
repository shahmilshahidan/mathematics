"""
Muhammad Shahmil Shahidan
Program to compute the prime factors of a number N.
"""

def nextPrimeNumber(p):
    if ((p+1) % 2 == 0) or ((p+1) % 3 == 0) or ((p+1) % 5 == 0) or ((p+1) % 7 == 0):
        p += 1
        return p
    else:
        nextPrimeNumber(p+1) 

def primeFactors(n):
    factors = []
    p = 2
    while n > 1:
        # Determine the remaining value is divisible by current prime number
        if n % p == 0:
            n = n // p
            factors.append(p)
        else:
            # Get the next prime number
            p = nextPrimeNumber(p)
    return factors

def primeFactorsWithCount(n):
    result = []
    factors = primeFactors(n)
    #Count the number of occurrence of each prime number
    factors_count = []
    prime_factors = []
    current_factor = factors[0]
    count = 1
    for f in range(1, len(factors)):
        if current_factor == factors[f]:
            count += 1
        else:
            factors_count.append(count)
            #Keep single value of prime factor in prime factors list
            prime_factors.append(current_factor)
            current_factor = factors[f]
            count = 1
    factors_count.append(count)
    prime_factors.append(current_factor)
    result.append(factors_count)
    result.append(prime_factors)
    return result

def powPrimeFactors(n):
    freq_primes = primeFactorsWithCount(n)
    pow_factors = freq_primes[-1]
    print(pow_factors)
    for p in range(len(pow_factors)):
        pow_factors[p] = pow_factors[p] ** 2
    return pow_factors


print(primeFactors(1000))
print(primeFactorsWithCount(1000))
print(powPrimeFactors(1000))