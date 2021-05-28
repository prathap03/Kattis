setData=list(map(int,input().split()))
validSet={0:1,1:1,2:2,3:2,4:2,5:8}
validSetFinal=[]
for i in range(6):
    if setData[i]>validSet[i]:
        validSetFinal.append(validSet[i]-setData[i])
    elif setData[i]<validSet[i]:
        validSetFinal.append(validSet[i]-setData[i])
    else:
        validSetFinal.append(0)
for i in validSetFinal:
    print(i,end=" ")