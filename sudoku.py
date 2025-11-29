from tkinter import *
from PIL import Image,ImageTk
import subprocess
def mousepos(event):
    status.set(f"{event.x}x{event.y}")
def click(event):
    if((((event.x)>=583)and(event.x<=596))and((event.y>=28)and(event.y<=40))):
        for row in entries:
            for entry in row:
                entry.delete(0,END)
    elif((((event.x)>=613)and(event.x<=627))and((event.y>=28)and(event.y<=40))):
        subprocess.Popen(["Python","sudoabout.py"])
        root.destroy()
def solve():
    
    board=[]
    for i in range (9):
        row = []
        for j in range (9):
            value = entries[i][j].get()
            if(value==""):
                row.append(0)
            else:
                row.append(int(value))
        board.append(row)
    with open ('board.txt','w') as f:
        for row in board:
            for element in row:
                f.write(f"{element} ")
            f.write("\n")
        f.close()
    with open ('boarddata.txt','w') as f:
        for row in board:
            for element in row:
                f.write(f"{element} ")
        f.close()
    subprocess.Popen(["Python","solver.py"])
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
status = StringVar()
status.set("Ready")
sbar = Label(root,textvariable=status,relief=SUNKEN)
sbar.pack(side=BOTTOM,fill=X)
root.bind('<Motion>',mousepos)
ubar.pack()
root.bind('<Button-1>',click)
ubar.place(x=150,y=10)
msg = Label(text="Enter the numbers in the\n grid and we will\n   solve the rest",fg="#5F7367",bg="white",font=("IBM Plex Sans",15))
msg.pack()
msg.place(x=560,y=150)
img4 = Image.open("warning.png")
img5 = img4.resize((200,50))
warn = ImageTk.PhotoImage(img5)
warnimg = Label(image=warn,bg="white")
warnimg.pack()
warnimg.place(x=560,y=250)
solveb = Button(text="SOLVE",font=("IBM Plex Sans",13,"bold"),fg="white",bg="#429EA6",command=solve)
solveb.pack()
solveb.place(x=560,y=530,width=220,height=44)
rows = 9
column = 9
entries = []
xp = 82
yp = 166
i = 0
j = 0
while(i<rows):
    xp=82
    # yp=166
    if((((i%3)==0))and(i!=0)):
        yp+=45
    elif(i!=0):
        yp+=37
    j=0
    row_entry =[]
    while(j<column):
        entry=Entry(root,bg="white",fg="black",width=2,relief='flat',borderwidth=0,font=("Arial",15,"bold"))
        
        if(((j%3)==0)and(j!=0)):
            xp = xp+45
            entry.place(x=xp,y=yp)
        elif(((j%3)!=0)and(j!=0)):
            xp=xp+37
            entry.place(x=xp,y=yp)
        elif(j==0):
            entry.place(x=xp,y=yp)
        
        row_entry.append(entry)
        j+=1
    entries.append(row_entry)
    i+=1
    about = Label(text="About Us",font=("IBM Plex Sans",5),fg="#5F7367",bg="#A8D94E")
    about.pack()
    about.place(x=752,y=51)
    home = Label(text="Home",font=("IBM Plex Sans",5),fg="#5F7367",bg="#A8D94E")
    home.pack()
    home.place(x=727,y=50)
root.mainloop()