n=int(input())
for i in range(n):
    r,e,c=tuple(map(int,input().split()))
    profitWithAds=e-c
    profitWithoutAds=r
    if profitWithAds>profitWithoutAds:
        print("advertise")
    elif profitWithAds==profitWithoutAds:
        print("does not matter")
    else:
        print("do not advertise")