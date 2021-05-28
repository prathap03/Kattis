import math
cases = int(input())
for _ in range(cases):
    v0,angle,x1,h1,h2 = list(map(float,input().split()))
    gravity = 9.81
    radians = math.radians(angle)
    timeAtX1 = x1 / (v0 * math.cos(radians))
    flight = v0 * timeAtX1 * math.sin(radians)
    fall = 1/2 * gravity * (timeAtX1 ** 2)
    heightAtX1 = flight - fall
    if h1 + 1 <= heightAtX1 and heightAtX1 <= h2 - 1:
        print("Safe")
    else:
        print("Not Safe")