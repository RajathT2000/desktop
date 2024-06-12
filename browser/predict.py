m = []
with open("points.txt", "r") as file:
    m = file.read().split('\n')[::-1]

money = 100    

m = m[:48]

for i,j in enumerate(m):
    num = j.split()[2][0]
    if i == 0:
        p = num
        continue
    print(i, j, p, num, money)
    if num == p:
        money += 10
    else:
        p = num
        money -= 10

