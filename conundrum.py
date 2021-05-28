encryptText = input()
name = "PER" * (len(encryptText) // 3)
days = 0
for cipherLetter, targetLetter in zip(encryptText, name):
    if cipherLetter != targetLetter:
        days += 1
print(days)