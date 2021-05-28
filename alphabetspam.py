whitespace=0
lower=0
upper=0
symbols=0
case=input()
for i in case:
    if i.isupper():
        upper+=1
    elif i.islower():
        lower+=1
    elif i=="_":
        whitespace+=1
    else:
        symbols+=1
print(whitespace/len(case))
print(lower/len(case))
print(upper/len(case))
print(symbols/len(case))