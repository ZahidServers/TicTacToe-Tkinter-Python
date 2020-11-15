from tkinter import *
from tkinter import messagebox
main=Tk()

main.title("Zahid Tic Tac Toe")

p1=1
p2=0

def player():
	global p1,p2
	if p1==1:
		p1=0
		p2=1
		return "X"
	elif p2==1:
		p1=1
		p2=0
		return "O"
def victory():
	winner=""
	if a1['text']==a2['text'] and a2['text']==a3['text']:
		if a1['text']=="X":
			winner="Player 1"
			messagebox.showinfo("Game Ended",winner)
			main.quit()
		elif a1['text']=="O":
			winner="Player 2"
			messagebox.showinfo("Game Ended",winner)
			main.quit()
	elif b1['text']==b2['text'] and b2['text']==b3['text']:
		if b1['text']=="X":
			winner="Player 1"
			messagebox.showinfo("Game Ended",winner)
			main.quit()
		elif b1['text']=="O":
			winner="Player 2"
			messagebox.showinfo("Game Ended",winner)
			main.quit()
	elif c1['text']==c2['text'] and c2['text']==c3['text']:
		if c1['text']=="X":
			winner="Player 1"
			messagebox.showinfo("Game Ended",winner)
			main.quit()
		elif c1['text']=="O":
			winner="Player 2"
			messagebox.showinfo("Game Ended",winner)
			main.quit()
	elif a1['text']==b1['text'] and b1['text']==c1['text']:
		if a1['text']=="X":
			winner="Player 1"
			messagebox.showinfo("Game Ended",winner)
			main.quit()
		elif a1['text']=="O":
			winner="Player 2"
			messagebox.showinfo("Game Ended",winner)
			main.quit()
	elif a2['text']==b2['text'] and b2['text']==c2['text']:
		if a2['text']=="X":
			winner="Player 1"
			messagebox.showinfo("Game Ended",winner)
			main.quit()
		elif a2['text']=="O":
			winner="Player 2"
			messagebox.showinfo("Game Ended",winner)
			main.quit()
	elif a3['text']==b3['text'] and b3['text']==c3['text']:
		if a3['text']=="X":
			winner="Player 1"
			messagebox.showinfo("Game Ended",winner)
			main.quit()
		elif a3['text']=="O":
			winner="Player 2"
			messagebox.showinfo("Game Ended",winner)
			main.quit()
	elif a1['text']==b2['text'] and b2['text']==c3['text']:
		if a1['text']=="X":
			winner="Player 1"
			messagebox.showinfo("Game Ended",winner)
			main.quit()
		elif a1['text']=="O":
			winner="Player 2"
			messagebox.showinfo("Game Ended",winner)
			main.quit()
	elif a3['text']==b2['text'] and b2['text']==c1['text']:
		if a3['text']=="X":
			winner="Player 1"
			messagebox.showinfo("Game Ended",winner)
			main.quit()
		elif a3['text']=="O":
			winner="Player 2"
			messagebox.showinfo("Game Ended",winner)
			main.quit()
def a1c():
	val=str(player())
	a1.config(text=val)
	victory()
	a1["state"]="disabled"
def a2c():
	val=str(player())
	a2.config(text=val)
	victory()
	a2["state"]="disabled"
def a3c():
	val=str(player())
	a3.config(text=val)
	victory()
	a3["state"]="disabled"
def b1c():
	val=str(player())
	b1.config(text=val)
	victory()
	b1["state"]="disabled"
def b2c():
	val=str(player())
	b2.config(text=val)
	victory()
	b2["state"]="disabled"
def b3c():
	val=str(player())
	b3.config(text=val)
	victory()
	b3["state"]="disabled"
def c1c():
	val=str(player())
	c1.config(text=val)
	victory()
	c1["state"]="disabled"
def c2c():
	val=str(player())
	c2.config(text=val)
	victory()
	c2["state"]="disabled"
def c3c():
	val=str(player())
	c3.config(text=val)
	victory()
	c3["state"]="disabled"

a1=Button(main,text="",width=10,height=10,command=a1c)
a2=Button(main,text="",width=10,height=10,command=a2c)
a3=Button(main,text="",width=10,height=10,command=a3c)

b1=Button(main,text="",width=10,height=10,command=b1c)
b2=Button(main,text="",width=10,height=10,command=b2c)
b3=Button(main,text="",width=10,height=10,command=b3c)

c1=Button(main,text="",width=10,height=10,command=c1c)
c2=Button(main,text="",width=10,height=10,command=c2c)
c3=Button(main,text="",width=10,height=10,command=c3c)

a1.grid(row=1,column=1)
a2.grid(row=1,column=2)
a3.grid(row=1,column=3)

b1.grid(row=2,column=1)
b2.grid(row=2,column=2)
b3.grid(row=2,column=3)

c1.grid(row=3,column=1)
c2.grid(row=3,column=2)
c3.grid(row=3,column=3)
main.mainloop()