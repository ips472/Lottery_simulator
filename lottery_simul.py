import random
import matplotlib.pyplot as plt

win=0
lose=0
account=0
x=[]
y=[]

for i in range(365):
    x.append(i+1)
    bet = random.randint(1, 10)
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
plt.plot(x,y)
plt.show()