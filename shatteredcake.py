W=int(input())
N=int(input())
mean_area=0
for i in range(N):
    w,l=tuple(map(int,input().split()))
    mean_area+=w*l
length=mean_area//W
print(length)