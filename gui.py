import tkinter as tk

import activeWindow
import askBing
import asyncio
import keyboard
import json


def ask(software, question):
    print("in ask")
    if question is not None:
        response = asyncio.run(askBing.askBing(software, question))
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
    tQuestion.grid(row=0, column=1)
    tAnswer = tk.Text(answerWindow, height=40, width=100)
    tAnswer.grid(row=1, rowspan=2)
    tQuestion.insert(tk.END, question)
    tAnswer.insert(tk.END, response)
    answerWindow.mainloop()


def middleHand(window, processName, question):
    print("Entered middleHand")
    close(window)
    answerWindow(ask(processName, question),question)


programRunning = True
while programRunning:
    print("Started")
    keyboard.wait("k")
    print("K pressed")
    master = tk.Tk()
    print("Master createdk")
    master.attributes('-topmost', True)
    master.title("Ask Bing!")
    tk.Label(master, text="Question").grid(row=0)
    e1 = tk.Entry(master)
    print("next is b1")
    b1 = tk.Button(master, text="Ask!", command=lambda :[middleHand(master, activeWindow.active_window_process_name(), e1.get())])
    # b2 = tk.Button(master, text="Quit", command=close(master))
    e1.grid(row=0, column=1, columnspan=2)
    b1.grid(row=1, column=0, columnspan=2)
    # kb2.grid(row=1, column=1,columnspan=2)
    master.mainloop()
