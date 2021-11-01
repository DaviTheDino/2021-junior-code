def sarcasm(string):
    newstring = '"'
    string = list(string)
    for i in range(len(string)):
        if i%2 == 1:
            if ord(string[i]) > 64 and ord(string[i]) < 91:
                newstring += (chr(ord(string[i]) + 32))
            elif ord(string[i]) > 96 and ord(string[i]) < 123:
                newstring += (chr(ord(string[i]) - 32))
            else:
                newstring += (string[i])
        else:
            newstring += (string[i])
    return newstring + '"'
if __name__ == "__main__":
    print('''The SARCASM MACHINE!!!!!''')
    lines = int(input("how many lines shall be sarcasmed?"))
    listolines = []
    for i in range(lines):
        listolines.append(input(f"{i+1}."))
    print("tHe nEwLy sArCaSmEd lInEs aRe")
    for i in range(lines):
        print(f"{i+1}.{sarcasm(listolines[i])}")

