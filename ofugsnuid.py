cases=int(input())
data=[]
for i in range(cases):
    data.append(int(input()))
for i in range(len(data)-1,-1,-1):
    print(data[i])