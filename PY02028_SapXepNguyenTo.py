from math import sqrt


def prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


n = int(input())
a = [int(x) for x in input().split()]
not_prime_arr = []
prime_arr = []

for i in range(n):
    if not prime(a[i]):
        not_prime_arr.append(a[i])
        a[i] = -1
    else:
        prime_arr.append(a[i])

prime_arr = sorted(prime_arr)

j, k = 0, 0
for i in range(n):
    if a[i] == -1:
        print(not_prime_arr[j], end=' ')
        j += 1
    else:
        print(prime_arr[k], end=' ')
        k += 1