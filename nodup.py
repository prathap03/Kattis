test=input().split()
ans="yes"
for i in test:
    if test.count(i)>1:
        ans="no"
print(ans)