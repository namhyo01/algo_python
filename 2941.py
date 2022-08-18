croatia_alphabet = ['c=','c-','dz=','d-','lj','nj','s=','z=']
alphabet = input()
for i in croatia_alphabet:
    alphabet = alphabet.replace(i,'a')
print(len(alphabet))