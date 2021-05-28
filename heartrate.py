n=int(input())
for i in range(n):
    data=input().split()
    beats=int(data[0])
    seconds=float(data[1])
    bpm=(60*beats)/seconds
    abpm=60/seconds
    minabpm=bpm-abpm
    maxbpm=bpm+abpm
    print(round(minabpm,4),round(bpm,4),round(maxbpm,4))