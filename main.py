import tkinter as tk

def rollDice():
    print("rolling dice")
    return 1

app = tk.Tk()
message = tk.Message(app, text="Welcome to the dice roller", width=150)
message.config(bg='orange')
message.pack()

rollButton = tk.Button(app, text='Roll', width=25, command=rollDice())
rollButton.pack()

app.mainloop()