n = int(input())
count = 0
num = 666
while True:
    if n == count:
        print(num-1)
        break
    if '666' in str(num):
        count += 1
    num+=1
    