import random
import tkinter

stats = []

def get_winner(call):
    if random.random() <= (1 / 3):
        throw = "Stone"
    elif (1 / 3) < random.random() <= (2 / 3):
        throw = "Scissors"
    else:
        throw = "Paper"

    if (throw == "Stone" and call == "Paper") or (throw == "Paper" and call == "Scissors")\
            or (throw == "Scissors" and call == "Stone"):
        stats.append('W')
        result = "You won this round! Go for it"
    elif throw == call:
        stats.append('D')
        result = "It's a draw!! You can win!."
    else:
        stats.append('L')
        result = "You lost! Try to win"
        

    global output
    output.config(text="Computer did: " + throw + "\n" + result)


def pass_s():
    get_winner("Scissors")
def pass_r():
    get_winner("Stone")
def pass_p():
    get_winner("Paper")

window = tkinter.Tk()
window.title('Stone-Paper-Scissors')

scissors = tkinter.Button(window, text = "Scissors", bg = "#ff9999", padx=10, pady=5, command=pass_s, width=20)
stone = tkinter.Button(window, text = "Stone", bg = "#80ff80", padx=10, pady=5, command=pass_r, width=20)
paper = tkinter.Button(window, text = "Paper", bg = "#3399ff", padx=10, pady=5, command=pass_p, width=20)
output = tkinter.Label(window, width=20, fg = "red", text="What's your call?")

stone.pack(side = "left")
paper.pack(side = "left")
scissors.pack(side = "left")
output.pack(side="right")
window.mainloop()

for i in stats: print(i, end=" ")
if stats.count('L') > stats.count('W'):
    result = "\nYou lost, Try again."
elif stats.count('L') == stats.count('W'):
    result = "\nIts a Draw or you didn't play at all."
else:
    result = "\nYou Won, Yaay!."

print(result)

