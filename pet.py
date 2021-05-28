previous_score=0
winner=None
for i in range(5):
    Sum=0
    Sum=sum(list(map(int,input().split())))
    if Sum>previous_score:
        winner=i+1
        previous_score=Sum
print(winner, previous_score)