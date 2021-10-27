def polynomialmultiplier(polynomial1, polynomial2):
    answer = [0]*(len([polynomial1])+len(polynomial2))
    for i in range(len(polynomial1)):
        for j in range(len(polynomial2)):
            answer[i+j] += polynomial1[i]*polynomial2[j]
    return answer

polynomial1=[1,2]
polynomial2=[1,2]
a=polynomialmultiplier(polynomial1,polynomial2)
print(a)