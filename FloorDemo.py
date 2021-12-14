from tkinter import *
from PIL import Image, ImageTk

window = Tk()
window.title("Event Floor Plan")
window.geometry('1168x730')
window.config(bg="white")
img = ImageTk.PhotoImage(file='Banquetroom_1168x730.png', master = window)
photolabel = Label(window,image=img)
photolabel.place(x=0,y=0)

#Create Table
#booted = False

#while booted == False:
    #for i in range (100):
      # label = label[i].append(Label(window,bg="Brown",width = .5,height =.5,text=(100-i) ))

    #while i == 100:
        #booted = True
def DragClick(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y

def DragMove(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x,y=y)

    


label = Label(window,bg="Brown",width = 2,height =2,text=f"12" )
label.place(x=0,y=0)
label2 = Label(window,bg="Brown",width = 2,height =2,text=f"11" )
label2.place(x=0,y=0)
label3 = Label(window,bg="Brown",width = 2,height =2,text=f"10" )
label3.place(x=0,y=0)
label4 = Label(window,bg="Brown",width = 2,height =2,text=f"9" )
label4.place(x=0,y=0)
label5 = Label(window,bg="Brown",width = 2,height =2,text=f"8" )
label5.place(x=0,y=0)
label6 = Label(window,bg="Brown",width = 2,height =2,text=f"7" )
label6.place(x=0,y=0)
label7 = Label(window,bg="Brown",width = 2,height =2,text=f"6" )
label7.place(x=0,y=0)
label8 = Label(window,bg="Brown",width = 2,height =2,text=f"5" )
label8.place(x=0,y=0)
label9 = Label(window,bg="Brown",width = 2,height =2,text=f"4" )
label9.place(x=0,y=0)
label10 = Label(window,bg="Brown",width = 2,height =2,text=f"3" )
label10.place(x=0,y=0)
label11 = Label(window,bg="Brown",width = 2,height =2,text=f"2")
label11.place(x=0,y=0)
label12 = Label(window,bg="Brown",width = 2,height =2,text=f"1")
label12.place(x=0,y=0)


label.bind("<Button-1>",DragClick)
label.bind("<B1-Motion>",DragMove)
label2.bind("<Button-1>",DragClick)
label2.bind("<B1-Motion>",DragMove)
label3.bind("<Button-1>",DragClick)
label3.bind("<B1-Motion>",DragMove)
label4.bind("<Button-1>",DragClick)
label4.bind("<B1-Motion>",DragMove)
label5.bind("<Button-1>",DragClick)
label5.bind("<B1-Motion>",DragMove)
label6.bind("<Button-1>",DragClick)
label6.bind("<B1-Motion>",DragMove)
label7.bind("<Button-1>",DragClick)
label7.bind("<B1-Motion>",DragMove)
label8.bind("<Button-1>",DragClick)
label8.bind("<B1-Motion>",DragMove)
label9.bind("<Button-1>",DragClick)
label9.bind("<B1-Motion>",DragMove)
label10.bind("<Button-1>",DragClick)
label10.bind("<B1-Motion>",DragMove)
label11.bind("<Button-1>",DragClick)
label11.bind("<B1-Motion>",DragMove)
label12.bind("<Button-1>",DragClick)
label12.bind("<B1-Motion>",DragMove)



window.mainloop()
