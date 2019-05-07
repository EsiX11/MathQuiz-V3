import time
from myDatabase import dataBaseInput
from MathQuiz_V3 import clearConsole

class questionsCheck():
    def questionChecking():
        questionLoop = True
        while questionLoop:
            answer = input("answer: ")
            try: 
                val = int(answer)
                if int(answer) == int(correctAnswer) :
                    answerCorrect = "Correct"
                    totalAnswersCorrect += 1
                    questionLoop = False
                    correctOrNot += 2
                elif answer != correctAnswer:
                    answerCorrect = "Incorrect"
                    totalAnswersIncorrect += 1
                    questionLoop = False
                    correctOrNot += 0
            except SyntaxError and ValueError:
                print("You didn't answer the question")
                time.sleep(1)
                clearConsole();
                progressBar(correctOrNot + 2, correctOrNot);
                pass
        x += 1
        print(answerCorrect)
        dataBaseInput.dataBaseSaveQuestions(number1, operator, number2, correctAnswer, answer, answerCorrect)
        time.sleep(1)