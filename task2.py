from random import shuffle

queue = 200
j = 0
N = 1000000
mass = [50] * 100 + [100] * 100
for k in range(N):
    people = 0  # number of people
    flag = True
    shuffle(mass)
    for elem in mass:
        if elem == 50:
            people += 1
        else:
            people -= 1
        if people < 0:
            flag = False
            break
    if flag:
        j += 1
print(j / N)
