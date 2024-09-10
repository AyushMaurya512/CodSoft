#Task 2 Given by CodSoft
#Python program to creat a calculator
from tkinter import *

root=Tk()
root.title("Simple Calculator")
root.geometry("565x600+500+100")
root.config(bg='#17161b')
root.resizable(height=False,width=False)

equation=""

def show(value):
    global equation
    equation+=value
    label_result.config(text=equation)
    
def clear():
    global equation
    equation=""
    label_result.config(text=equation)
    
def equal_to():
    global equation
    result=""
    if equation!="":
        try:
            result=eval(equation)
        except:
            result="Error"
            equation="" 
    label_result.config(text=result)

label_result=Label(root,bg="#ADD8E6",width=20,height=2,text="",font=("arial",30))
label_result.pack()

Button(root, text="C",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#3b23d0",command=lambda:clear()).place(x=10,y=100)
Button(root, text="/",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("/")).place(x=150,y=100)
Button(root, text="%",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("%")).place(x=290,y=100)
Button(root, text="x",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("*")).place(x=430,y=100)

Button(root, text="7",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("7")).place(x=10,y=200)
Button(root, text="8",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("8")).place(x=150,y=200)
Button(root, text="9",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("9")).place(x=290,y=200)
Button(root, text="-",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("-")).place(x=430,y=200)

Button(root, text="4",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("4")).place(x=10,y=300)
Button(root, text="5",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("5")).place(x=150,y=300)
Button(root, text="6",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("6")).place(x=290,y=300)
Button(root, text="+",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("+")).place(x=430,y=300)

Button(root, text="1",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("1")).place(x=10,y=400)
Button(root, text="2",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("2")).place(x=150,y=400)
Button(root, text="3",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("3")).place(x=290,y=400)

Button(root, text="0",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("0")).place(x=10,y=500)
Button(root, text="00",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("00")).place(x=150,y=500)
Button(root, text=".",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show(".")).place(x=290,y=500)
Button(root, text="=",width=5,height=3,font=("arial",30,"bold"),bd=3,fg="#fff",bg="#3a3f36",command=lambda:equal_to()).place(x=430,y=400)

root.mainloop()