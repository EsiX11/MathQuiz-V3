import random
import os
import time
import datetime
from myDatabase import *


def clearConsole():
    os.system('cls')


#progressBar (Done)
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
 
#asking name (Done)   
def askingName(): 
    playerName = input("What is your name?: ")
    playerSurname = input("What is your surname?: ")
    playerClass = input("Which is your class?:")
    dataBaseInput.dataBaseTests(playerName, playerSurname, playerClass) 

#theGame (Done)
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

#loadingGame (Done)
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

def endGame(correctOrNot):
    progressBar(correctOrNot + 2, correctOrNot);
    print("You won")

def questions():
    operatorList = ["+","-","x","/"]
    x = 0
    correctOrNot = 0
    totalAnswersCorrect = 0
    totalAnswersIncorrect = 0
    operator = operatorList[x]
    for questions in range (1,15):
        number1 = random.randint(1,15)
        number2 = random.randint(1,10)
        loop = True
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
         
        while loop:
            progressBar(correctOrNot + 2, correctOrNot);
            print("what is:", number1, operatorList[x], number2, "?")
            answer = input("Answer: ")
            try: 
                val = int(answer)
                loop = False

            except SyntaxError and ValueError:
                print("You didn't answer the question")
                time.sleep(1)
                clearConsole();
                pass
        if int(answer) == correctAnswer:
            answerCorrect = "Correct"
            correctOrNot += 2
        else:
            answerCorrect = "Incorrect"
        x += 1
        print(answerCorrect)
        dataBaseInput.dataBaseSaveQuestions(number1, operator, number2, correctAnswer, answer, answerCorrect)
        print(correctOrNot)
        time.sleep(1)
        if x > 3:
            x = 0
    
    endGame(correctOrNot);

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
progressBar(2, 0);  
theGame();
questions();

dataBaseInput.dataBaseCommit();
#start();