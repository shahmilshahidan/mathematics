import numpy as np

def sum_fracts(lst):
    # your code
    if lst == []:
        return None
    else:
        # Check for every denominator
        denom = lst[0][1]
        denom_lst = []
        for d in range(1, len(lst)):
            # Same denominator
            if lst[d][1] == denom:
                continue
            else:
                denom_lst.append(lst[d][1])
                denom = lst[d][1]
        # Denominators are equal
        if denom_lst == []:
            result = add_fraction(lst)
            return result
        # Denominators are not equal
        else:
            # Simplify the denominators
            denominator = np.lcm.reduce(denom_lst)
            print(denominator)
            for fraction in lst:
                fraction[0] = denominator // fraction[1]
                fraction[1] = denominator
            print(lst)
            result = add_fraction(lst)
            return result


def calculate_gcd(x, y):
    while(y):
        x, y = y , x % y
    return x
            
def add_fraction(lst):
    numerator = 0
    for fraction in lst:
        numerator += fraction[0]
    if (numerator % lst[0][1]) == 0:
        quotient = numerator // lst[0][1]
        return quotient
    else:
        quotient = [numerator, lst[0][1]]
        return quotient


print(sum_fracts([[1, 2], [1, 3], [1, 4]]))