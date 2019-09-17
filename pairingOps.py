def pairOps(n):
  even = []
  odd = []
  for i in range(len(n)-1):
    pair1 = n[i]
    for j in range(i+1,len(n)):
      pair2 = n[j]
      if (pair1 * pair2) % 2 == 0:
        even.append((pair1, pair2))
        if (pair1 + pair2) % 2 != 0:
          odd.append((pair1, pair2))
      elif (pair1 + pair2) %2 != 0:
          odd.append((pair1, pair2))
      else:
        continue
  print("Sum pair: ", odd, '\n', "Product pair: ", even)


def pairing(n):
  pair = []
  for i in range(len(n)-1):
    pair1 = n[i]
    for j in range(i+1,len(n)):
      pair2 = n[j]
      pair.append((pair1, pair2))
  return pair


def main():
  int_num = int(input("How many integers?\n"))
  int_list = [0] * int_num
  for n in range(int_num):
    int_list[n] = int(input("Enter an integer: "))
  pairOps(int_list)
  print(pairing(int_list))


main()