from random import randrange

queue = 200
j = 0
N = 10000000
for k in range(N):
    num_50 = 0  # amount of people with 50 rubles
    change = 0
    flag = True
    for i in range(queue):
        person = randrange(2)  # 0 - 50 rubles, 1 - 100 rubles
        if person == 0:
            change += 50
            num_50 += 1
        elif change == 0:
            flag = False
            break
        else:
            change -= 50
        if num_50 == 100:
            flag = True
            break
    if flag:
        j += 1
print(j / N)
