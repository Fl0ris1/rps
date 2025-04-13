from tkinter import *
from tkinter.font import Font

def Calculate():
    distance=distance_input.get()
    time=time_input.get()
    distance=float(distance)/1000
    to60=60/float(time)
    speed=float(distance)*to60
    answer_lbl.configure(text=f"You ran an average of {speed}km/h")

root=Tk()
root.title("KM/H Calculator")
root.geometry("750x400")
font=Font(family="consolas",weight="bold")
root.configure(background="#73E2A7")

title_lbl=Label(root,text="KM/H CALCULATOR",font=(font,15),bg="#73E2A7",fg="#218380")
title_lbl.place(x=280,y=10)

distance_lbl=Label(root,text="INPUT THE AMOUNT OF METERS YOU RAN: ",font=(font,13),bg="#73E2A7",fg="#141B41")
distance_lbl.place(x=50,y=100)

distance_lbl=Label(root,text="INPUT THE AMOUNT OF MINUTES YOU RAN: ",font=(font,13),bg="#73E2A7",fg="#141B41")
distance_lbl.place(x=50,y=150)

distance_input=Entry(root)
distance_input.place(x=400,y=103)

time_input=Entry(root)
time_input.place(x=410,y=153)

answer_lbl=Label(root,font=(font,15),bg="#73E2A7",fg="#141B41")
answer_lbl.place(x=200,y=300)

convert=Button(root,text="CALCULATE",font=(font,12),bg="#86BA90",fg="#141B41",command=Calculate)
convert.place(x=300,y=225)

root.mainloop()