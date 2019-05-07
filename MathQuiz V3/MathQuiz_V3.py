import random
import os
import time
import datetime
from myDatabase import *
from myQuestions import *


def clearConsole():
    os.system('cls')

def progressBar(line,space):
    clearConsole();
    lines = open("Code/Lines.txt","r")
    spaces = open("Code/Spaces.txt","r")
    if line > 20:
        space = 30 - space
        x = open("Code/x.txt","r")
        print("Progess: [" + lines.read(24) + ">" + spaces.read(0) + "]")
        print("Overdrive!: [" + x.read(line-20) + ">" + spaces.read(space) + "]")
        print("You unlocked the overdrive. You're save from the aliens but you can never be to sure")
        x.close()
    else:
        space = 22 - space
        print("Progess: [" + lines.read(line) + ">" + spaces.read(space) + "]")
    print("\n")
    lines.close()
    spaces.close()

 
#asking name (done)   
def askingName(): 
    playerName = input("What is your name?: ")
    playerSurname = input("What is your surname?: ")
    playerClass = input("Which is your class?:")
    dataBaseInput.dataBaseTests(playerName, playerSurname, playerClass) 

def theGame():
    explanation = open("story/explanation.txt", "r")
    os.system('color 2')
    print(explanation.read())
    try:
        input("Press enter to continue")
    except SyntaxError:
        pass
    print("")
    clearConsole();

def loadingGame():
    loadingBarPlus = ["+","+","+","+","+","+","+","+","+","+","+","+","+","+","+","+","+","+","+","+","+","+"]
    print("Loading:" , end="", flush=True)
    for x in loadingBarPlus: 
        print (x , end="", flush=True) 
        time.sleep(0.1)
    print("", end="\n")
    clearConsole();
    print("Loaded")
    try:
        input("Press enter to continue")
    except SyntaxError:
        pass
    print("")

def questions():
    operatorList = ["+","-","x","÷"]
    x = 0
    correctOrNot = 0
    totalAnswersCorrect = 0
    totalAnswersIncorrect = 0
    for questions in range (1,15):
        number1 = random.randint(1,15)
        number2 = random.randint(1,10)

        if x == 0:
            correctAnswer = number1 + number2
        elif x == 1:
            correctAnswer = number1 - number2
        elif x == 2:
            correctAnswer = number1 * number2
        elif x == 3:
            while number1 % number2:
                number1 = random.randint(1,15)
                number2 = random.randint(1,10)
            correctAnswer = number1 / number2
            x = 0
        progressBar(correctOrNot + 2, correctOrNot);
        operator = operatorList[x]
        print("what is:", number1, operatorList[x], number2, "?")
        answer = input("Answer: ")
        try: 
            val = int(answer)
        except SyntaxError and ValueError:
            print("You didn't answer the question")
            time.sleep(1)
            clearConsole();
            progressBar(correctOrNot + 2, correctOrNot);
            pass
        questionsCheck.questionChecking();



'''def questions():
    correctOrNot = 0
    totalCorrectAnswers = 0
    x = 0
    questionList = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']
    random.shuffle(questionList)
    for i in questionList:
        progressBar(line = correctOrNot + 2, space = correctOrNot);
        questionFilename = "questions/question" + questionList[x] + ".txt"
        answerFilename = "questions/answer(" + questionList[x] + ").txt"
        x += 1
        correctAnswers = open(answerFilename, "r")
        question = open(questionFilename , "r")
        print(question.read())
        answer = input("Answer: ")
        question.close()
        correctAnswer = correctAnswers.read()
        try: 
            val = int(answer)
            if int(answer) == int(correctAnswer) :
                print ("correct")
                questionLoop = False
                correctOrNot += 2
            elif answer != correctAnswer:
                print ("incorrect")
                questionLoop = False
                correctOrNot += 0
                incorrect = questionFilename
            time.sleep(1)
        except SyntaxError and ValueError:
            print("You didn't answer the question")
            time.sleep(1)
            clearConsole();
            pass
        
        if correctOrNot >= 20 and x == 15:
            progressBar(line = correctOrNot + 2, space = correctOrNot);
            print("You won")
            time.sleep(15)
            break
        if x == 15 and correctOrNot <= 20:
            progressBar(line = correctOrNot + 2, space = 22 - correctOrNot);
            print("You lost")
            time.sleep(10)
            break
        clearConsole();

    else:
        print("Good Bye")
        time.sleep(3)'''

def dataBaseCreation():
    DB = dataBase
    DB.dataBaseTests();
    DB.dataBaseQuestions();
    DB.dataBaseResults();

#creating the databases tables for saving data
dataBaseCreation();
#Askingname speaks for it selfs. Uses the info the player gives to correctly save it.
askingName();
#loadingGame is just a visual loading bar nothing else
loadingGame();
#progressBar is the progress bar at the top of the game. Keeping progress of the players progress.
progressBar(2, 22);  
theGame();
questions();

dataBaseInput.dataBaseCommit();
#start();