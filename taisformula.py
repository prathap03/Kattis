cases=int(input())
glucoseData={}
for i in range(cases):
    t,v=list(map(float,input().split()))
    glucoseData[t]=v
keys=list(glucoseData.keys())
area=0
for i in range(len(keys)-1):
    Sum=0
    totalTime=0
    Sum+=glucoseData.get(keys[i])+glucoseData.get(keys[i+1])
    totalTime+=keys[i+1]-keys[i]
    area+=((Sum/2)*totalTime)/1000
print(area)