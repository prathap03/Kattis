P=int(input())
for i in range(P):
    K,D=list(map(int,input().split()))
    candels=0
    for j in range(1,D+1):
        candels+=j
    print(K,candels+D)