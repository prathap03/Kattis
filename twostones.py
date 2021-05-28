n=int(input())
count=0
while count<=n:
    count+=2
if (n-count)%2==0:
    print("Bob")
else:
    print("Alice")