A, B, C = list(map(int, input().split()))
maxMoves = max(B - A, C - B) - 1
print(maxMoves)