import tkinter
from tkinter import messagebox
import math
exp = ""
first=float()
but=0
flag=0
def press(num): 
    global exp
    global flag
    if(str(num).isdigit()):
        exp = exp +str(num)
    elif(num=='π'):
        exp = exp +str(math.pi)
    elif(num=='.'):
        for i in exp:
            if(i=='.'):
                flag=1
        if(flag==1):
            pass
        else:
            exp=exp+'.'
    equation.set(exp)
   
def equal():
    try: 
  
        global exp
        second=float(exp)
        if(but==1):
            result=first+second
        elif(but==2):
            result=first-second
        elif(but==3):
            result=first*second
        elif(but==4):
            result=first/second
        elif(but==5):
            result=first**second
        exp=result
        equation.set(exp)

    except: 
        equation.set(" error ") 
        exp = "" 
   
def clr(): 
    global exp 
    exp = "" 
    equation.set("") 

def delete():
    global exp
    exp=exp[:-1]
    equation.set(exp)

def add_num():
    global exp
    global first
    global but
    first=float(exp)
    exp=""
    equation.set(exp)
    but=1
def subs_num():
    global exp
    global first
    global but
    first=float(exp)
    exp=""
    equation.set(exp)
    but=2
def mul_num():
    global exp
    global first
    global but
    first=float(exp)
    exp=""
    equation.set(exp)
    but=3
def div_num():
    global exp
    global first
    global but
    first=float(exp)
    exp=""
    equation.set(exp)
    but=4
def pow_num():
    global exp
    global first
    global but
    first=float(exp)
    exp=""
    equation.set(exp)
    but=5
def fact_num():
    global exp
    global first
    global but
    first=float(exp)
    try:
        result=math.factorial(first)
        exp=result
        equation.set(exp)
    except:
        messagebox.showerror("Invalid Input","Input for factorial should be a non-negative Integer")
        clr()        

root = tkinter.Tk()

root.iconbitmap('favicon.ico')
  
root.title("Calculator") 

root.geometry("325x325")

equation = tkinter.StringVar() 
exp_field = tkinter.Entry(root, textvariable=equation, width=25, font="5") 

exp_field.place(x=10,y=10)
exp_field.configure(font=("Calibri",17))
  
button1 = tkinter.Button(root, text=' 1 ', command=lambda: press(1), height=1, width=4) 
button1.place(x=10, y=50)
button1.configure(font=("Calibri",17))
  
button2 = tkinter.Button(root, text=' 2 ', command=lambda: press(2), height=1, width=4) 
button2.place(x=70, y=50)
button2.configure(font=("Calibri",17))
  
button3 = tkinter.Button(root, text=' 3 ', command=lambda: press(3), height=1, width=4) 
button3.place(x=130, y=50)
button3.configure(font=("Calibri",17))
  
button4 = tkinter.Button(root, text=' 4 ', command=lambda: press(4), height=1, width=4) 
button4.place(x=10, y=100)
button4.configure(font=("Calibri",17))
  
button5 = tkinter.Button(root, text=' 5 ', command=lambda: press(5), height=1, width=4) 
button5.place(x=70, y=100) 
button5.configure(font=("Calibri",17))

button6 = tkinter.Button(root, text=' 6 ', command=lambda: press(6), height=1, width=4) 
button6.place(x=130, y=100) 
button6.configure(font=("Calibri",17))

button7 = tkinter.Button(root, text=' 7 ', command=lambda: press(7), height=1, width=4) 
button7.place(x=10, y=150)
button7.configure(font=("Calibri",17))
  
button8 = tkinter.Button(root, text=' 8 ', command=lambda: press(8), height=1, width=4) 
button8.place(x=70, y=150)
button8.configure(font=("Calibri",17))
  
button9 = tkinter.Button(root, text=' 9 ', command=lambda: press(9), height=1, width=4) 
button9.place(x=130, y=150)
button9.configure(font=("Calibri",17))
  
button0 = tkinter.Button(root, text=' 0 ', command=lambda: press(0), height=1, width=4) 
button0.place(x=70, y=200)
button0.configure(font=("Calibri",17))
  
plus = tkinter.Button(root, text=' + ', command=add_num, height=1, width=4) 
plus.place(x=190, y=100)
plus.configure(font=("Calibri",17))
  
minus = tkinter.Button(root, text=' - ', command=subs_num, height=1, width=4) 
minus.place(x=190, y=150)
minus.configure(font=("Calibri",17))
  
multiply = tkinter.Button(root, text=' x ', command=mul_num, height=1, width=4)
multiply.place(x=190, y=200)
multiply.configure(font=("Calibri",17))
  
divide = tkinter.Button(root, text=' ÷ ', command=div_num, height=1, width=4)
divide.place(x=190, y=50)
divide.configure(font=("Calibri",17))

power = tkinter.Button(root, text=" ^ ", command=pow_num, height=1, width=4)
power.place(x=250, y=50)
power.configure(font=("Calibri",17))

equal = tkinter.Button(root, text=' = ', command=equal, height=1, width=4) 
equal.place(x=250, y=100)
equal.configure(font=("Calibri",17))

dot=tkinter.Button(root, text=' . ', command=lambda: press("."), height=1, width=4) 
dot.place(x=10, y=200)
dot.configure(font=("Calibri",17))

pi = tkinter.Button(root, text=' π ', command=lambda: press("π"), height=1, width=4) 
pi.place(x=250, y=150)
pi.configure(font=("Calibri",17))

clear = tkinter.Button(root, text='C', command=clr, height=1, width=4) 
clear.place(x=130, y=200) 
clear.configure(font=("Calibri",17))

delte = tkinter.Button(root, text='<-', command=delete, height=1, width=4) 
delte.place(x=250, y=200)
delte.configure(font=("Calibri",17))

facto = tkinter.Button(root, text='n!', command=fact_num, height=1, width=4) 
facto.place(x=10, y=250)
facto.configure(font=("Calibri",17))

root.mainloop() 
