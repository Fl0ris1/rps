from tkinter import *
from random import choice

player_score=0
computer_score=0
options=["rock","paper","scissors"]

def computer_wins():
    global computer_score, player_score
    computer_score+=1
    winner_lbl.config(text="COMPUTER WON")
    comp_score_lbl.config(text=f"Computer Score: {computer_score}")
    player_score_lbl.config(text=f"Your Score: {player_score}")

def player_wins():
    global computer_score,player_score
    player_score+=1
    winner_lbl.config(text="YOU WON")
    comp_score_lbl.config(text=f"Computer Score: {computer_score}")
    player_score_lbl.config(text=f"Your Score: {player_score}")

def tie():
    winner_lbl.config(text="Tie!")
    comp_score_lbl.config(text=f"Computer Score: {computer_score}")
    player_score_lbl.config(text=f"Your Score: {player_score}")

def computer_choice():
    return choice(options)

def player_choice(player_input):
    global computer_score,player_score
    print(player_input)

    computer_input=computer_choice()
    print(computer_input)

    comp_choice_lbl.config(text=f"Computer Selected: {computer_input}")    
    player_choice_lbl.config(text=f"You Selected: {player_input}")

    if player_input==computer_input:
        tie()
    
    if player_input=="rock":
        if computer_input=="paper":
            computer_wins()
        elif computer_input=="scissors":
            player_wins()

    elif player_input=="paper":
        if computer_input=="scissors":
            computer_wins()
        elif computer_input=="rock":
            player_wins()
    elif player_input=="scissors":
        if computer_input=="rock":
            computer_wins()
        elif computer_input=="paper":
            player_wins()



root=Tk()
root.geometry("700x400")
root.title("Rock Paper Scissors")

root.configure(background="#AAABBC")

heading_lbl=Label(root,text="ROCK PAPER SCISSORS",font=("consolas",20,"bold"),bg="#AAABBC",fg="#2B2D42")
heading_lbl.pack()

winner_lbl=Label(root,text="Let The Game Begin!",font=("consolas",15,"bold"),bg="#AAABBC",fg="#4F6D7A",pady=10)
winner_lbl.pack()

frame=Frame(root,bg="#AAABBC")
frame.pack()

player_options=Label(frame,text="Player Options: ",font=("consolas",14,"bold"),bg="#AAABBC",fg="#1D4C72")
player_options.grid(row=0,column=0,pady=10)

rock_but=Button(frame,text="Rock",font=("consolas",12,"bold"),bg="#3C787E",fg="#1D4C72",bd=0,width=15,pady=5,command=lambda:player_choice(options[0]))
rock_but.grid(row=1,column=1,padx=8,pady=5)

paper_but=Button(frame,text="Paper",font=("consolas",12,"bold"),bg="#3C787E",fg="#1D4C72",bd=0,width=15,pady=5,command=lambda:player_choice(options[1]))
paper_but.grid(row=1,column=2,padx=8,pady=5)

scissors_but=Button(frame,text="Scissors",font=("consolas",12,"bold"),bg="#3C787E",fg="#1D4C72",bd=0,width=15,pady=5,command=lambda:player_choice(options[2]))
scissors_but.grid(row=1,column=3,padx=8,pady=5)

score_lbl=Label(frame,text="Score: ",font=("consolas",14,"bold"),bg="#AAABBC",fg="#1D4C72")
score_lbl.grid(row=2,column=0)

player_choice_lbl=Label(frame,text="You Selected: ",font=("consolas",14,"bold"),bg="#AAABBC",fg="#5465FF")
player_choice_lbl.grid(row=3,column=1,pady=5)

player_score_lbl=Label(frame,text="Your Score: ",font=("consolas",14,"bold"),bg="#AAABBC",fg="#5465FF")
player_score_lbl.grid(row=3,column=2,pady=5)

comp_choice_lbl=Label(frame,text="Computer Selected: ",font=("consolas",14,"bold"),bg="#AAABBC",fg="#5465FF")
comp_choice_lbl.grid(row=4,column=1,pady=5)

comp_score_lbl=Label(frame,text="Computer Score: ",font=("consolas",14,"bold"),bg="#AAABBC",fg="#5465FF")
comp_score_lbl.grid(row=4,column=2,pady=5)

root.mainloop()