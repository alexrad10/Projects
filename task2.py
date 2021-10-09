from random import randrange
from tqdm import tqdm

queue = 200
j = 0
N = 10000000
for k in tqdm(range(N)):
    num_50 = 0
    num_100 = 0
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
            num_100 += 1
        if num_100 == 100:
            flag = True
            break
        if num_50 == 100:
            if change % (queue - (i + 1)) == 0:
                flag = True
            else:
                flag = False
    if flag:
        j += 1
print(j / N)
