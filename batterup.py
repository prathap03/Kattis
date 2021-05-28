noOfAtBats=int(input())
officailAtbats=0
cases=list(map(int,input().split()))
for i in cases:
    if i!=-1:
        officailAtbats+=i
    else:
        noOfAtBats-=1
print(officailAtbats/noOfAtBats)