n = int(input())

star_right = '* '
star_left = ' *'
space = ' '

b,c = n, n//2
for i in range(1, n+1):
    if b%2==0:
        print(star_right*c)
        print(star_left * (b-c))
    else:
        print(star_right * (b-c))
        print(star_left * c)