dial = [['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]
num = input().lower()
num = [n for n in num]
time = 0
for i in range(len(num)):
    for j in range(8):
        try:
            dial[j].index(num[i])

            time += j+3
            #print(dial[j].index(num[i]))
        except:
            continue

print(time)