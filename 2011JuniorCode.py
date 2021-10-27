def greaterThan10Mil(size5List):
    result=0
    for i in range(5):
        if size5List[i][1]/size5List[i][0] > 10:
            result+=1
    return result
def averageSalary(size5List):
    result=0
    for i in range(5):
        result+=size5List[i][1]/size5List[i][0]
    result = round(result*200000)
    return result
def lowestSalary16(size5List):
    tempList=[size5List[0][1]/size5List[0][0],size5List[1][1]/size5List[1][0],size5List[2][1]/size5List[2][0],size5List[3][1]/size5List[3][0],size5List[4][1]/size5List[4][0]]
    result=(sorted(tempList)[0])/16
    result=round(result*1000000)
    return result
def highestSalary18(size5List):
    tempList=[size5List[0][1]/size5List[0][0],size5List[1][1]/size5List[1][0],size5List[2][1]/size5List[2][0],size5List[3][1]/size5List[3][0],size5List[4][1]/size5List[4][0]]
    result=(sorted(tempList)[4])/18
    result=round(result*1000000)
    return result
def difference18Versus16(size5List):
    a=round(averageSalary(size5List)/16 - averageSalary(size5List)/18)
    return a
if __name__=="__main__":
    Pick1=[5,57.5]
    Pick2=[6,56.5]
    Pick3=[6,72]
    Pick4=[6,60]
    Pick5=[5,51]
    bigList=[Pick1,Pick2,Pick3,Pick4,Pick5]
    print(greaterThan10Mil(bigList))
    print(averageSalary(bigList))
    print(lowestSalary16(bigList))
    print(highestSalary18(bigList))
    print(difference18Versus16(bigList))
    #I suck so dont mind the notaiton
