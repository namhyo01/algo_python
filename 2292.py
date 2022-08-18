k = input()
k = int(k)
i=1
while True:
    room = 1+6*(i-1)*i/2
    if k <= room:
        print(i)
        break
    i += 1
   