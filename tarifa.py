MbPerMonth=int(input())
noOfMonths=int(input())

available=0
spent=0

for i in range(noOfMonths):
    usedMb=int(input())
    spent+=usedMb
    available+=MbPerMonth

available+=MbPerMonth
carryForwardData=available-spent
print(carryForwardData)
