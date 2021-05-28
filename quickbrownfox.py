cases=int(input())
for k in range(cases):
    word=input()
    temp=""
    panagram_condition=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    for i in range(len(word)):
        if word[i].lower() in panagram_condition:
            panagram_condition.remove(word[i].lower())

    for j in panagram_condition:
        temp+=j

    if len(temp)==0:
        print("pangram")
    else:
        print("missing",temp )
