import tkinter as tk

import activeWindow
import askBing
import asyncio
import keyboard
import json


def ask():
    question = e1.get()
    if question is not None:
        response = asyncio.run(askBing.askBing(software, question))
        for key in response:
            if key == "text":
                print(response[key])





keyboard.wait("k")
software = activeWindow.active_window_process_name()
master = tk.Tk()
master.title("Ask Bing!")
tk.Label(master, text="Question").grid(row=0)
e1 = tk.Entry(master)
b1 = tk.Button(master, text="Ask!", command=ask)
e1.grid(row=0, column=1)
b1.grid(row=1, column=0)
master.mainloop()
