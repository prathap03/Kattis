n=int(input())
data=[]
qual=0
for i in range(n):
    data.append(input().split())
for i in range(len(data)):
    qual+=float(data[i][0])*float(data[i][1])
print(qual)
