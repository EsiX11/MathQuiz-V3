import sqlite3
from sqlite3 import Error
conn = sqlite3.connect('test.db')
c = conn.cursor()
c.execute('PRAGMA foreign_keys = ON')

class dataBase():


    def dataBaseTests():
        c = conn.cursor()
        c.execute(''' CREATE TABLE IF NOT EXISTS Tests  (
                    testID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Name TEXT,
                    Surname TEXT,
                    Class TEXT)
                    ''')

    def dataBaseQuestions():
        c = conn.cursor()
        c.execute(''' CREATE TABLE IF NOT EXISTS Questions  (
                    Number1 INTEGER,
                    Operator TEXT,
                    Number2 INTEGER,
                    Answer INTEGER,
                    AnswerGiven INTEGER,
                    Correct TEXT,
                    Time_taken TEXT,
                    testID INTEGER,
                    CONSTRAINT fk_tests
                        FOREIGN KEY(testID)
                        REFERENCES Tests(testID))
                    ''')

    def dataBaseResults():
        c = conn.cursor()
        c.execute(''' CREATE TABLE IF NOT EXISTS Results  (
                    ResultID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Correctly_answerd INTEGER,
                    Total_time INTEGER,
                    Final_Stage INTERGER,
                    testID INTEGER,
                    CONSTRAINT fk_tests
                        FOREIGN KEY(testID)
                        REFERENCES Tests(testID))
                    ''')

class dataBaseInput:
    def dataBaseTests(Name,Surname,Class):
        c = conn.cursor()
        c.execute(''' INSERT INTO Tests (Name,Surname,Class)
                    VALUES (?, ?, ?)
                    ''', (Name,Surname,Class))

    def dataBaseSaveQuestions(number1, operator, number2, Answer, AnswerGiven, Correct, Time):
        c = conn.cursor()
        c.execute(''' INSERT INTO Questions (number1, operator, number2, Answer, AnswerGiven, Correct, Time_taken)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                    ''', (number1, operator, number2, Answer, AnswerGiven, Correct, Time))

    def dataBaseResults(totalCorrectAnswers, totalTime , stage):
        c = conn.cursor()
        c.execute(''' INSERT INTO Results (Correctly_answerd, Total_time, Final_Stage)
                    VALUES (?, ?, ?)
                    ''', (totalCorrectAnswers, totalTime, stage))

    # Commmit the changes
    def dataBaseCommit():
        conn.commit()
        conn.close()


