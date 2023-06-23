import asyncio, json,keyboard,win32gui

import win32gui, win32process, psutil
from EdgeGPT.EdgeGPT import Chatbot, ConversationStyle
from win32gui import GetWindowText, GetForegroundWindow

#Code from https://stackoverflow.com/a/65363087
def active_window_process_name():
    try:
        pid = win32process.GetWindowThreadProcessId(win32gui.GetForegroundWindow())
        return(psutil.Process(pid[-1]).name())
    except:
        pass
async def askBing(activeWindow,question):
    print("Enter question:\n")
    activeWindow = activeWindow.replace(".exe","")
    print("Software is: " + activeWindow)
    bot = await Chatbot.create() # Passing cookies is "optional", as explained above
    request = "Software being used: " + activeWindow + ". " + "My question is: " + question
    print(request)
    response = await bot.ask(prompt=request, conversation_style=ConversationStyle.creative, simplify_response=True)
    print(json.dumps(response, indent=2)) # Returns

    await bot.close()

def main():

    while True:
        if keyboard.is_pressed("k"):
            asyncio.run(askBing(active_window_process_name()))

if __name__ == "__main__":
    main()