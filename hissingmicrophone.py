word=input()
isHiss=False
for i in range(len(word)-1):
    if word[i]=="s" and word[i+1]=="s":
        isHiss=True
if isHiss:
    print("hiss")
else:
    print("no hiss")