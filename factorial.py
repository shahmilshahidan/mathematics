def factorial(n):
    if n == 0:
        return n
    else:
        m = n-1
        while m > 0:
            n *= m
            m -= 1

    return n

index = int(input("Enter a number: "))
if index < 0:
    print("The factorial is invalid")
elif index == 0:
    print(factorial(index))
else:
    print(factorial(index))
