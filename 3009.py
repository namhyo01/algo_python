x1,y1 = map(int, input().split())
x2,y2 = map(int, input().split())
x3,y3 = map(int, input().split())

x4 = [x1,x2,x3]
y4 = [y1,y2,y3]

for i in range(3):
    if x4.count(x4[i]) == 1:
        x = x4[i]
    if y4.count(y4[i]) ==1:
        y = y4[i]
print(str(x) +' '+ str(y))