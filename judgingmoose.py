data=list(map(int,input().split()))
if data[0]==data[1] and data[0]==data[1]!=0:
    print(F"Even {data[0]*2}")
elif data[0]==data[1]==0:
    print("Not a moose")
else:
    print("Odd",max(data)*2)
