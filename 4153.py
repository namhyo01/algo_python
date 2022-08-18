while True:
    a,b,c = map(int, input().split())
    if a==0 and b==0 and c==0:
        break
    triangle = [a,b,c]
    max_length = max(triangle)
    triangle.remove(max_length)
    if max_length**2 == (triangle[0]**2 + triangle[1] **2):
        print('right')
    else:
        print('wrong')