# task 5 from list

N, M = map(int, input().split())  # N - number of accounts, M - number of employees
Cn = []  # money on each account
num = 0  # counter
for i in range(N):
    Cn.append(int(input()))
min_in_mas = min(Cn)
while True:
    num += 1
    temp_sum = 0
    for i in range(N):
        temp_sum += Cn[i] // num
    if temp_sum < M:
        num -= 1
        break
print(num)
