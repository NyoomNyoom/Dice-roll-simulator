import tkinter as tk
from random import randint

def rollDice(appIn, messageIn):
    value = randint(0,6)
    messageIn.config(text="The dice roll is: "+str(value))
    messageIn.update()

app = tk.Tk()
welcomeMessage = tk.Message(app, text="Welcome to the dice roller", width=150)
welcomeMessage.config(bg='orange')
welcomeMessage.pack()

output = tk.Message(app, text="", width=300)
output.pack()

rollButton = tk.Button(app, text='Roll', width=25, command=lambda: rollDice(app, output))
rollButton.pack()

app.mainloop()