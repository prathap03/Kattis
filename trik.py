initial=[1,0,0]
moves=input()
for move in moves:
    if move=="A":
        initial[0],initial[1]=initial[1],initial[0]
    elif move=="B":
        initial[1],initial[2]=initial[2],initial[1]
    elif move=="C":
        initial[0],initial[2]=initial[2],initial[0]
print(initial.index(1)+1)