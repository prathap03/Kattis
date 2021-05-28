cases=int(input())
for i in range(cases):
    test=input()
    if "+" in test:
        Sum=sum(list(map(int,test.split("+"))))
        print(Sum)
    else:
        print("skipped") 