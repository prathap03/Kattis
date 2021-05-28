n=int(input())
data=[]
no_output=0
for i in range(n):
    data.append(input().split())
for i in range(len(data)):
    no_output=0
    no_output-=int(data[i][0])
    for j in range(1,len(data[i])):
        no_output+=int(data[i][j])
    print(no_output+1)