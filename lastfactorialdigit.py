case=int(input())
for i in range(case):
    test=int(input())
    fact=1
    for j in range(test,0,-1):
        fact*=j
    fact_str=str(fact)
    print(fact_str[-1])