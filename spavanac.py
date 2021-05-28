H,M = list(map(int,input().split()))
if M < 45:
    adjustedMinutes = M + 15
    if H == 0:
        adjustedHours = 23
    else:
        adjustedHours = H - 1
else:
    adjustedMinutes = M - 45
    adjustedHours = H
print(F"{adjustedHours} {adjustedMinutes}")