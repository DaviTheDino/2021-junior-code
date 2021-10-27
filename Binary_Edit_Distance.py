def edit_distance(x,y):
    runningtotal=0
    for i in range(1,len(x)):
       if x[i]!=y[i]:
           runningtotal=runningtotal+1
    return runningtotal
x=[1,0,1,1]
y=[1,1,1,0]
print(edit_distance(x,y))
