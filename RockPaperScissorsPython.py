
#Rock, Paper, Scissors Game!
import sys
from PyQt5.QtWidgets import *
from random import randint

gameArr = ['rock','paper','scissors']

application = QApplication([])

rock = QPushButton('Rock')
paper = QPushButton('Paper')
scissors = QPushButton('Scissors')

window = QWidget()
layout = QVBoxLayout()

window.setWindowTitle('Rock, Paper, Scissors')
window.setGeometry(200,200,200,200)

play = QLabel()
play.setText('Play Rock, Paper, Scissors!')
wait = QLabel()
wait.setText('Choose one. . .')

layout.addWidget(play)
layout.addWidget(wait)
layout.addWidget(rock)
layout.addWidget(paper)
layout.addWidget(scissors)

window.setLayout(layout)

def rockButton():
    compChoice = randint(0,2)
    alert = QMessageBox()
    if gameArr[compChoice] == 'rock':
        text = 'You Tied.'
    elif gameArr[compChoice] == 'paper':
        text = 'You Lost.'
    elif gameArr[compChoice] == 'scissors':
        text = 'You Won!'
    
    alert.setText("You Chose Rock.\nComputer got " + gameArr[compChoice] + ". . .\n\n" + text)
    alert.exec_()

def paperButton():
    compChoice = randint(0,2)
    alert = QMessageBox()
    if gameArr[compChoice] == 'rock':
        text = 'You Won!'
    elif gameArr[compChoice] == 'paper':
        text = 'You Tied.'
    elif gameArr[compChoice] == 'scissors':
        text = 'You Lost.'
    
    alert.setText("You Chose Paper.\nComputer got " + gameArr[compChoice] + ". . .\n\n" + text)
    alert.exec_()

def scissorsButton():
    compChoice = randint(0,2)
    alert = QMessageBox()
    if gameArr[compChoice] == 'rock':
        text = 'You Lost.'
    elif gameArr[compChoice] == 'paper':
        text = 'You Won!'
    elif gameArr[compChoice] == 'scissors':
        text = 'You Tied.'
    
    alert.setText("You Chose Scissors.\nComputer got " + gameArr[compChoice] + ". . .\n\n" + text)
    alert.exec_()


rock.clicked.connect(rockButton)
paper.clicked.connect(paperButton)
scissors.clicked.connect(scissorsButton)

window.show()
application.exec_()




