set_hamburger = []
set_coke = []
for i in range(3):
    set_hamburger.append(int(input()))
for i in range(2):
    set_coke.append(int(input()))
print(min(set_coke) + min(set_hamburger) - 50)