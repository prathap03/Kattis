C=float(input())
L=int(input())
total_area=0
for i in range(L):
    w,l=list(map(float,input().split()))
    total_area+=w*l
total_cost=round(total_area*C,7)
print(total_cost)