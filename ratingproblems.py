n,k=tuple(list(map(int,input().split())))
sum=0
for i in range(k):
    sum+=int(input())
if n!=k:
    minmumRating=(sum-3*(n-k))/n
    MaximumRatingsum=(sum+3*(n-k))/n
else:
    minmumRating=sum/n
    MaximumRatingsum=sum/n

print(minmumRating,MaximumRatingsum)