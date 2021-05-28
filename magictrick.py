case=input()
for i in case:
    if case.count(i)%2==0:
        print("0")
        break
else:
    print("1")