file = open("gymnastics.in")
x = file.readline().split()

K = int(x[0])
N = int(x[1])

sessions = []
for i in range(K):
    x = [int(i) for i in file.readline().split()]
    sessions.append(x)

cows = []
for i in range(1,N+1):
    cows.append(i)

count = 0
for i in range(0,N):
    for x in range(i+1,N):
        pair = [cows[i],cows[x]]
        status = True
        for y in sessions:
            if y.index(cows[i]) < y.index(cows[x]):
                status = False
                break
        if status == True:
            count += 1
            continue
        status = True
        for y in sessions:
            if y.index(cows[i]) > y.index(cows[x]):
                status = False
                break
        if status == True:
            count += 1   
with open("gymnastics.out","w") as f:
    f.write(str(count))
