import sqlite3
from sqlite3 import Error
conn = sqlite3.connect('test.db')

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
        c.execute('PRAGMA foreign_keys = ON')
        c.execute(''' CREATE TABLE IF NOT EXISTS Questions  (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Number1 INTEGER,
                    Operator TEXT,
                    Number2 INTEGER,
                    Answer INTEGER,
                    AnswerGiven INTEGER,
                    Correct TEXT,
                    testID INTEGER,
                    CONSTRAINT fk_tests
                        FOREIGN KEY (testID)
                        REFERENCES Tests (testID))
                    ''')

    def dataBaseResults():
        c = conn.cursor()
        c.execute(''' CREATE TABLE IF NOT EXISTS Results  (
                    ResultID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Answer INTEGER,
                    Correct INTEGER,
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

    def dataBaseSaveQuestions(number1, operator, number2, Answer, AnswerGiven, Correct):
        c = conn.cursor()
        c.execute(''' INSERT INTO Questions (number1, operator, number2, Answer, AnswerGiven, Correct)
                    VALUES (?, ?, ?, ?, ?, ?)
                    ''', (number1, operator, number2, Answer, AnswerGiven, Correct))

    def dataBaseResults():
        c = conn.cursor()
        c.execute(''' INSERT INTO Results (Operand1, Operator, Operand2, ExpectedAnswer, Answer, Correct)
                    VALUES (?, ?, ?, ?, ?, ?)
                    ''', (operand1, operator, operand2, eAnswer, sAnswer, correct))

    # Commmit the changes
    def dataBaseCommit():

        conn.commit()

        conn.close()


