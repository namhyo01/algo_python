N = int(input())
star = '*'
space = ' '
for i in range(2*N-1):
    if i < N:
        star_num = 2*N-1 - i*2
        space_num = i
        print(space*space_num,end='')
        print(star*star_num,end='')
        #print(space*space_num)
        print()
    else:
        star_num = star_num+2
        space_num = space_num-1
        print(space*space_num + star * star_num)


