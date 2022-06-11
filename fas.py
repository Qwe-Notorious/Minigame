import random
from random import randint
from tkinter import *
import sys

window = Tk()
window.title("21 очко")
window.geometry('395x250')


def clicked():
    AnswerVar = IntVar()
    AdditionQuestionRightSide = random.randint(1 , 21)
    AdditionQuestionRightSide = Label(window, text=AdditionQuestionRightSide,
    font='Times 30', fg='#6A5ACD').grid(row=1, column=0)
    string_answer = AnswerVar.get()
    int_answer = int(string_answer)

def clicked2():
    AnswerVar = IntVar()
    AdditionQuestionLeftSide = random.randint(1, 21)
    AdditionQuestionLefttSide = Label(window, text=AdditionQuestionLeftSide,
    font='Times 30', fg='#6A5ACD').grid(row=2, column=0)
    string_answer = AnswerVar.get()
    int_answer = int(string_answer)


btn1 = Button(window, text="Нажать", justify=LEFT, activebackground='#44944A', bg='#293133', fg='#FFFAFA',
              padx="20",
              pady="8",
              font="16",
              height='-100', command=clicked)
btn1.grid(column=1, row=1)

btn2 = Button(window, text="Нажать", justify=LEFT, activebackground='#44944A', bg='#293133', fg='#FFFAFA',
              padx="20",
              pady="8",
              font="16",
              height='-100', command=clicked2)
btn2.grid(column=2, row=1)


window.mainloop()