import asyncio, json
from EdgeGPT.EdgeGPT import Chatbot, ConversationStyle


async def askBing(activeWindow,question,shortanswer,generalQuestion):
    activeWindow = activeWindow.replace(".exe","")
    print("Software is: " + activeWindow)
    bot = await Chatbot.create() # Passing cookies is "optional", as explained above
    if shortanswer is True:
        question = question + ". Answer length: Short"
    if generalQuestion is not True:
        request = "Software being used: " + activeWindow + ". " + "My question is: " + question
    elif generalQuestion is True:
        request = question

    print(request)
    response = await bot.ask(prompt=request, conversation_style=ConversationStyle.creative, simplify_response=True)
    return response
    #print(json.dumps(response, indent=2)) # Returns

    await bot.close()
