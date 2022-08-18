def new_make_num(n):
    if n>=10:
        n = int(((n/10)+(n%10))%10) + int((n%10)*10)
    else:
        n = int(n*10) + int(n)
    return n

n = int(input())
cycle = 1

new_num = new_make_num(n)

while n!=new_num:
    new_num = new_make_num(new_num)
    cycle = cycle + 1 

print(cycle)

