import random
import matplotlib.pyplot as plt
from tkinter import *


root=Tk()
root.geometry('1920x1080')
root.title('Lottery Simulator')
root.state("zoomed")

win=0
lose=0
account=0
x=[]
y=[]

setWinValue = StringVar()
setLoseValue = StringVar()
setAmount = StringVar()

# days = int(input("Enter the number of days: "))

def win_calc(days):
    global x, y, win, lose, account, setWinValue, setLoseValue, setAmount
    for i in range(days):
        bet = random.randint(1, 10)
        x.append(i+1)
        lucky_draw = random.randint(1, 10)
        print("Bet:", bet)
        print("Lucky draw:", lucky_draw)
        
        if bet == lucky_draw:
            account = account+900-100
            win+=1
        else:
            lose+=1
            account = account-100
        y.append(account)
    print("Total Lottery Won: ",win)
    print("Total Lottery Loose: ",lose)
    print("Amount in your game account: ", account)

    setWinValue.set(win)
    setLoseValue.set(lose)
    setAmount.set(account)




def calc_button():
    global days_text, win, lose, account, x, y
    win=0
    lose=0
    account=0
    x.clear()
    y.clear()

    days = int(days_text.get())
    print(days)
    win_calc(days)
    days_text.delete(0,END)


def show_graph():
    global x, y
    plt.plot(x,y)
    plt.show()

days_label = Label(root, text="Days: ")
days_label.config(font =("Courier", 30))
days_label.place(relx=0.2, rely=0.3)

days_text = Entry(root, font=('arial', 30,'bold'))
days_text.place(relx=0.3, rely=0.3)

calc_button = Button(root, text="Calculate", font=("arial", 18,'bold'), command=calc_button)
calc_button.place(relx=0.6,rely=0.3)

graph_button = Button(root, text="Show graph", font=("arial", 15,'bold'), command=show_graph)
graph_button.place(relx=0.6,rely=0.7)

#Result section
lottey_won_label = Label(root, text="Total Lottery Won: ", font=("arial", 18, 'bold')).place(relx=0.3, rely=0.5)
lottey_loose_label = Label(root, text="Total Lottery Lose: ", font=("arial", 18, 'bold')).place(relx=0.3, rely=0.55)
amount_label = Label(root, text="Amount in your game account: ", font=("arial", 18, 'bold')).place(relx=0.3, rely=0.6)

won = Label(root, text="", textvariable=setWinValue, font=("arial", 18, 'bold')).place(relx=0.54, rely=0.5)
lose = Label(root, text="", textvariable=setLoseValue, font=("arial", 18, 'bold')).place(relx=0.54, rely=0.55)
amount = Label(root, text="", textvariable=setAmount, font=("arial", 18, 'bold')).place(relx=0.54, rely=0.6)


root.mainloop()