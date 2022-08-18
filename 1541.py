import sys

num = sys.stdin.readline().rstrip().split('-')
small_num = 0
count = 0
for numbers in num:
    real_nums = numbers.split('+')
    real_nums = list(map(int, real_nums))
    if(count==0):
        small_num+=sum(real_nums)
        count+=1
    else:
        small_num-=sum(real_nums)
print(small_num)

    

