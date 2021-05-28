cases=int(input())
temperature_data=list(map(int,input().split()))
count=0
for i in range(cases):
    if temperature_data[i]<0:
        count+=1
print(count)