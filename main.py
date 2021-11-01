def swap_case(s):
    s = list(s)
    print(s)
    s_new = []
    for i in s:
        if ord(i) < 91 and ord(i) > 64:
            s_new.append(chr(ord(i)+32))
        else:
            s_new.append(chr(ord(i)+32))
    s_new2 = ''
    print(s_new)
    for i in s_new:
        s_new2 = s_new2 + i
    return s_new2

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)