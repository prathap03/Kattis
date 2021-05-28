blimp_lst=[]
for blimp in range(1,6):
    name=input()
    if "FBI" in name:
        blimp_lst.append(blimp)
if blimp_lst==[]:
    print("HE GOT AWAY!")
else:
    for name in blimp_lst:
        print(name,end=" ")