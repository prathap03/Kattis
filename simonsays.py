cases=int(input())
for i in range(cases):
    test=input()
    if "Simon says" in test:
        action=test.split("Simon says")
        print(action[1].lstrip())