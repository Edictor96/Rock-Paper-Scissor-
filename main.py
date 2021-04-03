from tkinter import *
import random 
root=Tk(className="Rock Paper Scissor")
root.geometry("480x260")
root.configure(bg="darkcyan")
root.resizable(width=False, height=False)
a=Label(root,font=('ComicSans',20),text="Rock Paper Scissor",bg="lightsteelblue")
a.place(x=120,y=10)
p=""
new_pc=0
def choice(option):
    p.destroy()
    if option=="Quit" :
        root.destroy()
    if option=="Repeat" :
        rock['state']='active'
        paper['state']='active'
        scissor['state']='active'
        global new_pc
        new_pc=random.randint(1,3)
def rc():
    if new_pc==1:
        out2=Label(root,font=('ComicSans',18),text="It's a tie:/",bg="lightsteelblue")
        out2.place(x=180,y=210)
        print("Dio Chose Rock") 
        print("It's a tie")
    elif new_pc==2:
        out2=Label(root,font=('ComicSans',18),text="You Lose :(",bg="lightsteelblue")
        out2.place(x=180,y=210)
        print("Dio Chose Paper")
        print("You Lose :(")
    elif new_pc==3:
        out2=Label(root,font=('ComicSans',18),text="You Win :)",bg="lightsteelblue")
        out2.place(x=180,y=210) 
        print("Dio Chose Scissor") 
        print("You win :)")
def pp():
    if new_pc==1  :
        out2=Label(root,font=('ComicSans',18),text="You Win :)",bg="lightsteelblue")
        out2.place(x=180,y=210)
        print("Dio Chose Rock") 
        print("You win:)")
    elif new_pc==2 :
        out2=Label(root,font=('ComicSans',18),text="It's a tie :/",bg="lightsteelblue")
        out2.place(x=180,y=210) 
        print("Dio Chose Paper") 
        print("It's a tie :/")
    elif new_pc==3 :
        out2=Label(root,font=('ComicSans',18),text="You Lose :(",bg="lightsteelblue")
        out2.place(x=180,y=210)
        print("Dio Chose Scissor") 
        print("You lose :(")
def sc():
    if new_pc==1 :
        out2=Label(root,font=('ComicSans',18),text="You Lose :(",bg="lightsteelblue")
        out2.place(x=180,y=210)
        print("Dio Chose Rock") 
        print("You lose:(")
    elif new_pc==2 :
        out2=Label(root,font=('ComicSans',18),text="You Win :)",bg="lightsteelblue")
        out2.place(x=180,y=210)
        print("Dio Chose Paper") 
        print("You win :)")
    elif new_pc==3 :
        out2=Label(root,font=('ComicSans',18),text="It's a tie :/",bg="lightsteelblue")
        out2.place(x=180,y=210) 
        print("Dio Chose Scissor") 
        print("Its a Tie :/")
def click():
    global p 
    p = Toplevel(root)
    p.title("My Popup")
    p.geometry("150x70")
    p.configure(bg="black")
    Repeat=Button(p,text="Repeat",width=7,height=1,command=lambda: choice ("Repeat"),bg="orange")
    Repeat.place(x=20,y=30)
    No=Button(p,text="Quit",width=7,height=1,command=lambda: choice ("Quit"),bg="pink")
    No.place(x=80,y=30)
    rock['state']='disabled'
    paper['state']='disabled'
    scissor['state']='disabled'
rock=Button(root,text="ROCK",width=10,height=3,bg="lightsteelblue",command=lambda:[rc(),click()]) 
rock.place(x=120,y=150)
paper=Button(root,text="PAPER",width=10,height=3,bg="lightsteelblue",command=lambda:[pp(),click()])
paper.place(x=200,y=150)
scissor=Button(root,text="SCISSOR",width=10,height=3,bg="lightsteelblue",command=lambda:[sc(),click()])
scissor.place(x=280,y=150)
print(new_pc)
root.mainloop()
