cases=int(input())
for i in range(cases):
    seq1=input()
    seq2=input()
    diffstr=""
    for j in range(len(seq1)):
        if seq1[j]==seq2[j]:
            diffstr+="."  
        else:
            diffstr+="*"
    print(seq1)
    print(seq2)
    print(diffstr,"\n")