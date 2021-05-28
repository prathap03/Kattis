N,P,S=list(map(int,input().split()))
for i in range(S):
    cardSet=list(map(int,input().split()))
    print("KEEP") if P in cardSet[1:] else print("REMOVE")