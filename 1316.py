n = int(input())
count = 0
for i in range(n):
    word = input()
    word = [w for w in word]
    _index = 0
    routine = True
    while ((_index < len(word))and(routine)):
        _cnt = word.count(word[_index])
        if (_cnt==1): # 단어가 한개밖에없을때
            _index += 1
        elif _cnt>1: # 중복단어가 한개 초과일때는
            for k in range(1,_cnt):
                if word[k+_index] == word[_index]:
                    continue
                else:
                    routine = False
                    break
            _index += _cnt
    if routine:
        count += 1        
print(count)

            

