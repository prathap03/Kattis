cardsInHand=input().split()
rankOfCardsInHand=[]
previousRank=0
strenghtOfHand=1
for card in cardsInHand:
    rankOfCardsInHand.append(card[0])
for rank in rankOfCardsInHand:
    if previousRank<rankOfCardsInHand.count(rank):
        strenghtOfHand=rankOfCardsInHand.count(rank)
        previousRank=strenghtOfHand
print(strenghtOfHand)