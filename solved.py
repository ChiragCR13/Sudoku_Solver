from tkinter import *
from PIL import Image,ImageTk
import subprocess
def click(event):
    if((((event.x)>=583)and(event.x<=596))and((event.y>=28)and(event.y<=40))):
        subprocess.Popen(["Python","sudoku.py"])
        root.destroy()
    elif((((event.x)>=613)and(event.x<=627))and((event.y>=28)and(event.y<=40))):
        subprocess.Popen(["Python","sudoabout.py"])
        root.destroy()

def solve():
    subprocess.Popen(["Python","sudoku.py"])
    root.destroy()
root = Tk()
root.config(bg="white")
root.geometry("1280x648")
img = Image.open("grid.png")
img1 = img.resize((380,380))
grid = ImageTk.PhotoImage(img1)
canvas = Canvas(root,width=500,height=500,bg="white",highlightthickness=0)
canvas.pack(side=LEFT,padx=50)
grid_id=canvas.create_image(200,260,image=grid)
img2 = Image.open("upper_bar.png")
img3 = img2.resize((650,65))
bar = ImageTk.PhotoImage(img3)
ubar=Label(image=bar,borderwidth=0)
ubar.pack()
root.bind('<Button-1>',click)
home = Label(text="Home",font=("IBM Plex Sans",5),fg="#5F7367",bg="#A8D94E")
home.pack()
home.place(x=727,y=50)
ubar.place(x=150,y=10)
msg = Label(text="This is how it should\n   be solved",fg="#5F7367",bg="white",font=("IBM Plex Sans",15))
msg.pack()
msg.place(x=560,y=150)
img4 = Image.open("solved.png")
img5 = img4.resize((220,44))
solvebar = ImageTk.PhotoImage(img5)
bar2 = Label(image=solvebar,bg="white")
bar2.pack()
bar2.place(x=560,y=530)
solveb = Button(text="SOLVE ANOTHER",font=("IBM Plex Sans",10,"bold"),fg="white",bg="#429EA6",command=solve,relief="flat")
solveb.pack()
solveb.place(x=570,y=480,width=200,height=44)
count = 0
i = 0
j = 0
yp = 166
about = Label(text="About Us",font=("IBM Plex Sans",5),fg="#5F7367",bg="#A8D94E")
about.pack()
about.place(x=752,y=50)
with open ("board.txt","r") as f:
    data = f.read()
    f.close()
if(data=="False"):
    subprocess.Popen(["Python","unsolved.py"])
    root.destroy()
while(i<9):
    xp=82
    # yp=166
    if((((i%3)==0))and(i!=0)):
        yp+=45
    elif(i!=0):
        yp+=37
    j=0
    row_entry =[]
    while(j<9):
        if(count>len(data)-2):
            break
        dat=Label(root,text=data[count],bg="white",fg="black",font=("Arial",13,"bold"))
        dat.pack()
        count+=2

        if(((j%3)==0)and(j!=0)):
            xp = xp+45
            dat.place(x=xp,y=yp)
        elif(((j%3)!=0)and(j!=0)):
            xp=xp+37
            dat.place(x=xp,y=yp)
        elif(j==0):
            dat.place(x=xp,y=yp)
        
        
        j+=1
    i+=1

root.mainloop()