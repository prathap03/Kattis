import math
h,v=list(map(int,input().split()))
l=h/math.sin(math.radians(v))
print(math.ceil(l))