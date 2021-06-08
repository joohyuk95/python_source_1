from tkinter import *

def myFunc():
    if chk.get():
        print("체크버튼 눌림")
    else:           
        print("체크버튼 해제")

window = Tk()
window.title("체크버튼 연습")
window.geometry("200x100")

chk = IntVar()
cb1 = Checkbutton(window, text = "클릭하세요", variable=chk, command=myFunc)

cb1.pack()
window.mainloop()