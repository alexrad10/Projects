# task 5 from list

N, M = map(int, input().split())  # N - number of accounts, M - number of employees
Cn = []  # money on each account
for i in range(N):
    Cn.append(int(input()))
my_max = sum(Cn)
my_min = 0
while True:
    num = (my_max + my_min) // 2
    if num == 0:
        break
    temp_sum = 0
    for i in range(N):
        temp_sum += Cn[i] // num
    if temp_sum == M:
        while temp_sum == M:
            num += 1
            temp_sum = 0
            for i in range(N):
                temp_sum += Cn[i] // num
        num -= 1
        break
    elif temp_sum < M:
        my_max = num
    else:
        my_min = num
print(num)
