def perfect_square(n):
    if n == 0:
        return n
    else:
        n **= 2
    return n


num = int(input('A number: '))
t = []
for i in range(num):
    x = int(input('Square of: '))
    t.append(perfect_square(x))
print(t)
