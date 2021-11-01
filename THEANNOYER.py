import random
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
    print("Hello I am a nice chatbot!")
    while 1<2:
        listoinsults = ['trash dood','cringe','LOAL','bruh not cool','your not funny']
        answer = input()
        if answer == '69':
            while 1 < 2:
                print('why ', end = '')
        else:
            print(sarcasm(answer))
            print(listoinsults[random.randint(0,len(listoinsults)-1)])