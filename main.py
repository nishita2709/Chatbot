#Import the library
import random
import tkinter as tk

#create the tkinter object. This represents the parent window.
root = tk.Tk()
user_input = tk.Entry(root)
#pack is used to organize widget in the block
user_input.pack()

greetings = ['hola', 'hello', 'hi', 'Hi', 'hey!', 'hey']
question = ['How are you?', 'How are you doing?']
responses = ['Okay', "I'm fine"]
huh = "I did not understand what you said"

def cb():
    user_text = user_input.get()
    if user_text in greetings:
        bot_text = random.choice(greetings)
    elif user_text in question:
        bot_text = random.choice(responses)
    else:
        bot_text = huh
    output.config(text=bot_text)

button = tk.Button(root, text="Enter", command=cb)
button.pack()

output = tk.Label(root, text='')
output.pack()

tk.mainloop()
