import re

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
        if (numerator > 0 and denominator > 0) or (numerator < 0 and denominator < 0):
            # All positive and all negative
            remaining = divmod(numerator, denominator)
            whole_num = remaining[0]
            fraction = simplify(remaining[1], denominator)
            return mixed_number_format(whole_num, fraction[0], fraction[1])
        else:
            if numerator < 0:
                remaining = divmod(abs(numerator), denominator)
                whole_num = remaining[0]
                fraction = simplify(remaining[1], denominator)
                return mixed_number_format(-whole_num, fraction[0], fraction[1])
            elif denominator < 0:
                remaining = divmod(numerator, abs(denominator))
                whole_num = remaining[0]
                fraction = simplify(remaining[1], denominator)
                return mixed_number_format(-whole_num, fraction[0], fraction[1])
        

def simplify(x, y):
    i = 2
    while i < min(x,y) + 1:
        if x % i == 0 and y % i == 0:
            x = x // i
            y = y // i
        else:
            i += 1
    if x < 0 and y < 0:
        x = x // -1
        y = y // -1
    return (x, y)

def mixed_number_format(i, numerator, denominator):
    if i == 0:
        return str(numerator) + '/' + str(denominator)    
    return str(i) + ' ' + str(numerator) + '/' + str(denominator)

print(mixed_fraction('42/9'))
#print(-10%7)