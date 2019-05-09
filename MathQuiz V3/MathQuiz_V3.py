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
    explanation.close()

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

#Not done yet
def stageSelector(stage,totalTime,correctOrNot):
    questions(16,0,stage);
    progressBar(correctOrNot + 2, correctOrNot);
    if correctOrNot < 20:
        youLost = open("story/lost.txt","r")
        print(youLost.read())
        youLost.close()
        #dataBaseInput.dataBaseResults()
        time.sleep(3)
    else:
        stageWon = open("story/stageWon" + stage + ".txt", "r")
        print(stageWon.read())

        if stage == 1:
            s.stageOne(correctOrNot);
        elif stage == 2:
            s.stageTwo(correctOrNot);
        elif stage == 3:
            stageThree(correctOrNot);
        time.sleep(2)
        clearConsole();

def questions(rangeQuestions,correctOrNot,stage):
    operatorList = ["+","-","x","/"]
    x = 0
    totalAnswersCorrect = 0
    totalAnswersIncorrect = 0
    totalTime = 0
    operator = operatorList[x]
    for questions in range (1,rangeQuestions):
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
            startTime = time.time()
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
            
        endTime = time.time()
        x += 1
        print(answerCorrect)
        splitTime = round(endTime - startTime,3)
        totalTime = round(totalTime + splitTime,3)
        print("Time: ", splitTime)
        dataBaseInput.dataBaseSaveQuestions(number1, operator, number2, correctAnswer, answer, answerCorrect)
        print(correctOrNot)
        print(totalTime)
        time.sleep(1)
        if x > 3:
            x = 0
    
    return(correctOrNot,totalTime,correctOrNot)
    


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
#loadingGame();
#progressBar is the progress bar at the top of the game. Keeping progress of the players progress.
progressBar(2, 0);  
theGame();
stageSelector(1,0,0);
#questions(16,0,1);

dataBaseInput.dataBaseCommit();
#start();