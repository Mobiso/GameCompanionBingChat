import tkinter as tk
from tkinter import *
import activeWindow
import askBing
import asyncio
import keyboard
import json

def ask(software, question,shortanswer,generalQuestion):
    print("in ask")
    if question is not None:
        response = asyncio.run(askBing.askBing(software, question,shortanswer,generalQuestion))
        for key in response:
            if key == "text":
                return response[key]


def close(window):
    window.destroy()


def answerWindow(response, question):
    answerWindow = tk.Tk()
    answerWindow.attributes('-topmost', True)
    answerWindow.title("Bing answer!")
    tk.Label(answerWindow, text="Question:").grid(row=0, column=0)
    tk.Label(answerWindow, text="Answer:").grid(row=1, columnspan=2)
    tQuestion = tk.Text(answerWindow, height=1, width=40)
    tQuestion.grid(row=0, column=0,columnspan=2)
    tAnswer = tk.Text(answerWindow, height=40, width=100)
    tAnswer.grid(row=1, rowspan=2)
    tQuestion.insert(tk.END, question)
    tAnswer.insert(tk.END, response)
    answerWindow.mainloop()


def middleHand(window, processName, question,shortanswer,generalQuestion):
    close(window)
    answerWindow(ask(processName, question,shortanswer,generalQuestion),question)


programRunning = True
while programRunning:

    print("Started")
    keyboard.wait("k")
    software = activeWindow.active_window_process_name()
    master = tk.Tk()
    master.attributes('-topmost', True)
    master.title("Ask Bing!")

    #Variables
    shortVar = BooleanVar()
    generalQuestion = BooleanVar()

    tk.Label(master, text="Question").grid(row=0)
    e1 = tk.Entry(master)
    checkboxShortAnswer = tk.Checkbutton(master, text="Short answer",variable=shortVar)
    checkboxGeneral = tk.Checkbutton(master, text="General Question", variable=generalQuestion)
    b1 = tk.Button(master, text="Ask!", command=lambda :[middleHand(master, software, e1.get(),shortVar.get(),generalQuestion.get())])

    # b2 = tk.Button(master, text="Quit", command=close(master))
    e1.grid(row=0, column=1, columnspan=2)
    b1.grid(row=1, column=0)
    checkboxShortAnswer.grid(row=1,column=1)
    checkboxGeneral.grid(row = 1, column=2)
    # kb2.grid(row=1, column=1,columnspan=2)
    master.mainloop()
