import tkinter as tk
import main, asyncio


def ask():
    question = e1.get()
    if question is not None:
        asyncio.run(main.askBing("Skype", question))
master = tk.Tk()
master.title("Ask Bing!")
tk.Label(master, text="Question").grid(row=0)
e1 = tk.Entry(master)
b1 = tk.Button(master, text="Ask!", command=ask)
e1.grid(row=0, column=1)
b1.grid(row=1, column=0)



master.mainloop()