numbers=tuple(list(input().split()))
rev_s=""
data=[]
for i in range(len(numbers)):
    rev_s=""
    for j in range(len(numbers[i])-1,-1,-1):
        rev_s+=numbers[i][j]
    data.append(int(rev_s))
print(max(data))