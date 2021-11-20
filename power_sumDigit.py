import math

def pow_sumToDigit(n):
    while True:
        base = 9
        exp = 2
        x = pow(9, exp)
        #print(x)
        digitSum = ((x // 10) + (x % 10))
        #print(digitSum)
        if digitSum and pow(digitSum, 2):
            return x
        else:
            if exp < 4:
                base -= 1
                exp += 1
            elif exp >= 4:
                base += 1


print(pow_sumToDigit(1))