cases=int(input())
for i in range(cases):
    cities=[]
    for j in range(int(input())):
        city=input()
        if city not in cities:
            cities.append(city)
    print(len(cities))
