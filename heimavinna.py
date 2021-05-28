problems=input().split(";")
count=0
for i in problems:
    if "-" in i:
        lower,upper=list(map(int,i.split("-")))
        for j in range(lower,upper+1):
            count+=1
    else:
        count+=1
print(count)