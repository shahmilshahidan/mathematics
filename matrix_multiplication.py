def multiply_matrix(a, b):
    for i in range(len(a)):
        for j in range((b[0])):
            for k in range(len(b)):
                res[i][j] += a[i][k] * b[k][j]
    for r in  result:
        print(r)

row_size = int(input("Size of row: "))
col_size = int(input("Size of column: "))

row = row_size * []
col = col_size * []
for m in range(row_size*2):
    num = int(input("Enter a number: "))
    row.append(num)
print(row)

for n in range(col_size*2):
    num1 = int(input("Enter a number: "))
    col.append(num1)
print(col)

print(multiply_matrix(row, col))
