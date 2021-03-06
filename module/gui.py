from tkinter import *

window = None
canvas = None
x1, y1, x1, y2 = None, None, None, None

def mouseClick(event):
    global x1, y1
    x1 = event.x
    y1 = event.y

def mouseDrop(event):
    global x1, y2, x2, y2
    x2 = event.x
    y2 = event.y
    canvas.create_line(x1,y1,x2,y2, width=5,fill="red")

window = Tk()
window.title("그림판 비슷한 프로그램")
canvas = Canvas(window, height = 200, width = 200)
canvas.bind("<Button -1>", mouseClick)
canvas.bind("<ButtonRelease-1>", mouseDrop)

canvas.pack()
window.mainloop()