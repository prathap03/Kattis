expense=0
cases=int(input())
data=list(map(int,input().split()))
for spendings in data:
    if spendings<0:
        expense-=spendings
print(expense)