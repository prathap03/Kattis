count=0
unis=int(input())
winning_unis=[]
winning_team=[]
for case in range(unis):
    uni,team=input().split()
    if count<12 and uni not in winning_unis:
        count+=1
        winning_unis.append(uni)
        winning_team.append(team)
for i in range(len(winning_unis)):
    print(winning_unis[i],winning_team[i])