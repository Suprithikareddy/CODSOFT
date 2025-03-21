from tkinter import *
from PIL import Image,ImageTk
from random import randint

window =Tk()
window.title("Rock Paper Scissor Game")
window.configure(background="black")


def updateMessage(a):
    game_message['text'] = a


def cscore_update():
    final = int(computer_score['text'])
    final=final+1
    computer_score["text"]=str(final)


def pscore_update():
    final = int(player_score['text'])
    final=final+1
    player_score["text"]=str(final)

def scores(p,c):
    if p==c:
        updateMessage("It's a tie!!")
    elif p=="rock":
        if c=="paper":
            updateMessage("Computer wins!!")
            cscore_update()
        else:
            updateMessage("Player wins!!")
            pscore_update()
    elif p=="paper":
        if c=="scissor":
            updateMessage("Computer wins!")
            cscore_update()
        else:
            updateMessage("Player wins!")
            pscore_update()
    elif p=="scissor":
        if c=="rock":
            updateMessage("Computer wins!")
            cscore_update()
        else:
            updateMessage("Player wins!")
            pscore_update()
    else:
        pass
to_select =["rock","paper","scissor"]

def update_choice(a):
    choice_computer = to_select[randint(0,2)]
    if choice_computer=="rock":
        computer.configure(image=rock_image2)
    elif choice_computer=="paper":
        computer.configure(image= paper_image2)
    else:
        computer.configure(image= scissor_image2)

    if a=="rock":
        player.configure(image=rock_image1)
    elif a=="paper":
        player.configure(image = paper_image1)
    else:
        player.configure(image = scissor_image1)
    
    scores(a,choice_computer)



rock_image1= ImageTk.PhotoImage(Image.open("rock1.jpeg"))
paper_image1= ImageTk.PhotoImage(Image.open("paper1.png"))
scissor_image1= ImageTk.PhotoImage(Image.open("scissor1.png"))
rock_image2= ImageTk.PhotoImage(Image.open("rock2.jpeg"))
paper_image2= ImageTk.PhotoImage(Image.open("paper2.png"))
scissor_image2= ImageTk.PhotoImage(Image.open("scissor2.png"))

computer=Label(window,image=scissor_image1)
player=Label(window,image=scissor_image2)
computer.grid(row=1,column=0)
player.grid(row=1,column=4)

computer_score=Label(window,text=0,font=("arial",60,"bold"),fg="red")
player_score=Label(window,text=0,font=("arial",60,"bold"),fg="blue")
computer_score.grid(row=1,column=1)
player_score.grid(row=1,column=3)

player_indicator=Label(window,font=("arial",40,"bold"),text="PLAYER",bg="yellow",fg="red")
computer_indicator=Label(window,font=("arial",40,"bold"),text="COMPUTER",bg="yellow",fg="red")
computer_indicator.grid(row=0,column=1)
player_indicator.grid(row=0,column=3)

game_message=Label(window,font=("arial",20,"bold"),bg="white",fg="black")
game_message.grid(row=3,column=2)

rock_button= Button(window,width=16,height=4,text="ROCK",font=("arial",20,"bold"),bg="white",fg="black",command=lambda:update_choice("rock")).grid(row=2,column=1)
paper_button= Button(window,width=16,height=4,text="PAPER",font=("arial",20,"bold"),bg="white",fg="black",command=lambda:update_choice("paper")).grid(row=2,column=2)
scissor_button= Button(window,width=16,height=4,text="SCISSOR",font=("arial",20,"bold"),bg="white",fg="black",command=lambda:update_choice("scissor")).grid(row=2,column=3)


window.mainloop()