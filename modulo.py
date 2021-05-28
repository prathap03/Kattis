distinct_numbers=[]
for i in range(10):
    mod42=int(input())%42
    if mod42 not in distinct_numbers:
        distinct_numbers.append(mod42)
print(len(distinct_numbers))