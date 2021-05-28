n,T=tuple(list(map(int,input().split())))
timeRequired=list(map(int,input().split()))
current_time=0
count=0
for i in range(n):
    current_time+=timeRequired[i]
    if current_time<=T:
        count+=1
    else:
        break
print(count)