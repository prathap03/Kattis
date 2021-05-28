N=int(input())
sum=0
for i in range(N):
    case=input()
    correct_case=int(case[:len(case)-1])**int(case[-1])
    sum+=correct_case
print(sum)