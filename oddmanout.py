cases=int(input())
for i in range(cases):
    test=int(input())
    data=list(map(int,input().split()))
    for j in range(test):
        if data.count(data[j])<=1:
            print(F"Case #{i+1}: {data[j]}")