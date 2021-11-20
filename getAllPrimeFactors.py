def getAllPrimeFactors(n):
    #your code here
    prime_factors = []
    # FYI for all natural numbers 1 is not a prime number =)
    prime_num = 2
    remainder = n
    while remainder > 1:
        if remainder % prime_num == 0:
            prime_factors.append(prime_num)
            remainder = remainder // prime_num
        else:
            # Raise the prime number
            prime_num += 1
            # Check if prime number is not a multiple of 2,3,5,7
            if (prime_num % 2 != 0) or (prime_num % 3 != 0) or (prime_num % 5 != 0) or (prime_num % 7 != 0):
                if remainder % prime_num == 0:
                    prime_factors.append(prime_num)
                    remainder = remainder // prime_num
    return prime_factors

def getUniquePrimeFactorsWithCount(n):
    #your code here
    factors = getAllPrimeFactors(n)
    prime_count = []
    #TODO:Remove the duplicates
    current_factor = factors[0]
    for i in range(1,len(factors)):
        if factors[i] == current_factor:
            current_factor = factors[i]
            factors.remove(factors[i-1])
        elif factors[i] != current_factor:
            current_factor = factors[i]
    count.remove(0)
    prime_count.append(count)
    return prime_count

def getUniquePrimeFactorsWithProducts(n):
    #your code here
    factors = getUniquePrimeFactorsWithCount(n)
    pow_factors = []
    return pow_factors

print(getAllPrimeFactors(100))
print(getUniquePrimeFactorsWithCount(100))