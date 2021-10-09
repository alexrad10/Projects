n = int(input())
for k in range(1, int(n ** (1 / 3)) + 1):
    for i in range(1, int(n ** (1 / 3)) + 1):
        for j in range(1, int(n ** (1 / 3)) + 1):
            for l in range(1, int(n ** (1 / 3)) + 1):
                if k ** 3 + i ** 3 == j ** 3 + l ** 3 and k ** 3 + i ** 3 <= n and k != j and i != l and i > k and l > j and j > k:
                    print(k ** 3 + i ** 3, ' ', k, ' ', i, ' ', j, ' ', l, ' ')

