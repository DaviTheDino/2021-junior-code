# input : base2 no x, base2 no y
# output : integer, edit-distance
# algorthm : loop each bit, cal the diff , count as 1
#
def edit_distance(x,y):
    runningtotal=0
    for i in range(1,len(x)):
       if x[i]!=y[i]:
           runningtotal=runningtotal+1
    return runningtotal

x=[1,0,1,1]
y=[1,1,1,0]
print(edit_distance(x,y))

