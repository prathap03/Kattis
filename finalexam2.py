questions = int(input())
previousAnswer = input()
correctAnswers = 0
for i in range(questions - 1):
    currentAnswer = input()
    if previousAnswer == currentAnswer:
        correctAnswers += 1
    previousAnswer = currentAnswer
print(correctAnswers)