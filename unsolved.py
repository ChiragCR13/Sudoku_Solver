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
root.geometry("1280x648")
root.config(bg="white")
img = Image.open("grid.png")
img1 = img.resize((380,380))
grid = ImageTk.PhotoImage(img1)
canvas = Canvas(root,width=500,height=500,bg="white",highlightthickness=0)
canvas.pack(side=LEFT,padx=50)
grid_id=canvas.create_image(200,260,image=grid)
img2 = Image.open("upper_bar.png")
img3 = img2.resize((650,65))
bar = ImageTk.PhotoImage(img3)
ubar=Label(image=bar)
status = StringVar()
status.set("Ready")
sbar = Label(root,textvariable=status,relief=SUNKEN,borderwidth=0)
sbar.pack(side=BOTTOM,fill=X)
# root.bind('<Motion>',mousepos)
ubar.pack()
root.bind('<Button-1>',click)
ubar.place(x=150,y=10)
msg = Label(text="Unfortunately, this\nsudoku is unsolvable",fg="#5F7367",bg="white",font=("Consolas",15))
msg.pack()
msg.place(x=560,y=150)
home = Label(text="Home",font=("IBM Plex Sans",5),fg="#5F7367",bg="#A8D94E")
home.pack()
home.place(x=727,y=52)
img4 = Image.open("warning.png")
img5 = img4.resize((200,50))
warn = ImageTk.PhotoImage(img5)
warnimg = Label(image=warn,bg="white")
warnimg.pack()
warnimg.place(x=560,y=250)
solveb = Button(text="TRY AGAIN",font=("Consolas",13,"bold"),fg="white",bg="#429EA6",command=solve)
solveb.pack()
solveb.place(x=560,y=530,width=220,height=44)
count = 0
i = 0
j = 0
yp = 166
with open ("boarddata.txt","r") as f:
    data1 = f.read()
    f.close()
data=""
for chars in data1:
    if (chars=="0"):
        data+=" "
    else:
        data+=chars

while(i<9):
    xp=82
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
about = Label(text="About Us",font=("IBM Plex Sans",5),fg="#5F7367",bg="#A8D94E")
about.pack()
about.place(x=752,y=52)
root.mainloop()