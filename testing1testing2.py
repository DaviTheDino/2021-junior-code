a = ['y','E','e','T',"'","["]
newa = []
finala = ''
for i in a:
    if ord(i) > 64 and ord(i) < 91:
        newa.append(chr(ord(i)+32))
    elif ord(i) > 96 and ord(i) < 123:
        newa.append(chr(ord(i)-32))
    else:
        newa.append(i)
for i in newa:
    finala += i
print(finala)


