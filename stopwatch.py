no_press=int(input())
accumulatedTime=0
previousTime=0
isRunning=False
for i in range(no_press):
    currentTime=int(input())
    if isRunning:
        accumulatedTime+=currentTime-previousTime
    previousTime=currentTime
    isRunning= not isRunning
if isRunning:
    print("Still Running")
else:
    print(accumulatedTime)