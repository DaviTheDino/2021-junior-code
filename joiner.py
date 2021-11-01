def splitnjoin(string):
    string = string.split(' ')
    string = ''.join(string)
    return string
if __name__ == '__main__':
    thing = splitnjoin(input())
    listofpauses = [',',';','.','!','?',]
    for i in listofpauses:
        thing = thing.split(i)
        thing = ''.join(thing)
    thing = list(thing)
    for i in range(len(thing)):
        if ord(thing[i]) < 91 and ord(thing[i]) > 64:
            thing[i] = chr(ord(thing[i]) + 32)
    thing2 = ''
    for i in thing:
        thing2 = thing2 + str(i)
    print(thing2)