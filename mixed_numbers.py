import re, math

def mixed_fraction(s):
    parsing = re.split("\/", s)
    numerator = int(parsing[0])
    denominator = int(parsing[1])
    if denominator == 0:
        raise ZeroDivisionError
    elif numerator == 0:
        return '0'
    result = numerator % denominator
    if result == 0:
        return str(numerator // denominator)
    else:
        # All positive fractions or all negative fractions
        if (numerator > 0 and denominator > 0) or (numerator < 0 and denominator < 0):
            proper_fraction = factoring(numerator, denominator)
            return mixed_number_format(proper_fraction[0], proper_fraction[1], proper_fraction[2])
        else:
            # Numerator is negative
            # Improper fraction case
            if numerator < 0 and (abs(numerator) > abs(denominator)):
                proper_fraction = factoring(abs(numerator), denominator)
                return mixed_number_format(-proper_fraction[0], proper_fraction[1], proper_fraction[2])
            # Proper fraction case
            elif numerator < 0 and (abs(numerator) < abs(denominator)):
                # Quotient equals to numerator
                if numerator // denominator == -1:
                    pf = simplify(abs(numerator), denominator)
                    return mixed_number_format(0, -pf[0], pf[1])
                proper_fraction = factoring(abs(numerator), denominator)
                return mixed_number_format(proper_fraction[0], -proper_fraction[1] * -1, proper_fraction[2])
            # Denominator is negative
            elif denominator < 0:
                # Quotient equals to numerator
                if numerator // denominator == -1:
                    pf = simplify(numerator, abs(denominator))
                    return mixed_number_format(0, -pf[0], pf[1])
                proper_fraction = factoring(numerator, abs(denominator))
                return mixed_number_format(-proper_fraction[0], proper_fraction[1], proper_fraction[2])


def proper_fraction(numerator, denominator):
    # Quotient equals to numerator
    if numerator // denominator == -1:
        pf = simplify(abs(numerator), denominator)
        return mixed_number_format(0, -pf[0], pf[1])
    proper_fraction = factoring(abs(numerator), denominator)
    return mixed_number_format(proper_fraction[0], -proper_fraction[1] * -1, proper_fraction[2])

def improper_fraction(numerator, denominator):
    proper_fraction = factoring(abs(numerator), denominator)
    return mixed_number_format(-proper_fraction[0], proper_fraction[1], proper_fraction[2])

def factoring(x,y):
    remaining = divmod(x, y)
    whole_num = remaining[0]
    fraction = simplify(remaining[1], y)
    return [whole_num, fraction[0], fraction[1]]

def simplify(x, y):
    divisor = math.gcd(x,y)
    x = x // divisor
    y = y // divisor
    if x < 0 and y < 0:
        x = x // -1
        y = y // -1
    return (x, y)

def mixed_number_format(i, numerator, denominator):
    if i == 0:
        return str(numerator) + '/' + str(denominator)
    return str(i) + ' ' + str(numerator) + '/' + str(denominator)

print(1104055 // 3033796)
print(1104055 % -3033796)