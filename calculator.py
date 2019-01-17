import tkinter
import math
exp = "" 
def press(num): 
    global exp
    if(str(num).isdigit()):
        exp = exp + str(num)
    elif(num=='π'):
        exp = exp +str(math.pi)
    else:
        if(str(exp[-1]).isdigit()):
            exp = exp+str(num)
        else:
            exp=exp[:-1]+str(num)
    equation.set(exp)
   
def equalpress():
    try: 
  
        global exp 
        total = str(eval(exp))   
        equation.set(total) 
        exp = "" 

    except: 
  
        equation.set(" error ") 
        exp = "" 
   
def clear(): 
    global exp 
    exp = "" 
    equation.set("") 

def delete():
    global exp
    exp=exp[:-1]
    equation.set(exp)
  

root = tkinter.Tk()

root.iconbitmap('favicon.ico')
  
root.title("Calculator") 

root.geometry("325x260")


  
     
equation = tkinter.StringVar() 
exp_field = tkinter.Entry(root, textvariable=equation, width=27, font="5") 

exp_field.place(x=10,y=10)  
  
button1 = tkinter.Button(root, text=' 1 ', command=lambda: press(1), height=2, width=7) 
button1.place(x=10, y=50) 
  
button2 = tkinter.Button(root, text=' 2 ', command=lambda: press(2), height=2, width=7) 
button2.place(x=70, y=50) 
  
button3 = tkinter.Button(root, text=' 3 ', command=lambda: press(3), height=2, width=7) 
button3.place(x=130, y=50) 
  
button4 = tkinter.Button(root, text=' 4 ', command=lambda: press(4), height=2, width=7) 
button4.place(x=10, y=100) 
  
button5 = tkinter.Button(root, text=' 5 ', command=lambda: press(5), height=2, width=7) 
button5.place(x=70, y=100) 
  
button6 = tkinter.Button(root, text=' 6 ', command=lambda: press(6), height=2, width=7) 
button6.place(x=130, y=100) 
  
button7 = tkinter.Button(root, text=' 7 ', command=lambda: press(7), height=2, width=7) 
button7.place(x=10, y=150) 
  
button8 = tkinter.Button(root, text=' 8 ', command=lambda: press(8), height=2, width=7) 
button8.place(x=70, y=150) 
  
button9 = tkinter.Button(root, text=' 9 ', command=lambda: press(9), height=2, width=7) 
button9.place(x=130, y=150) 
  
button0 = tkinter.Button(root, text=' 0 ', command=lambda: press(0), height=2, width=7) 
button0.place(x=70, y=200)
  
plus = tkinter.Button(root, text=' + ', command=lambda: press("+"), height=2, width=7) 
plus.place(x=190, y=100) 
  
minus = tkinter.Button(root, text=' - ', command=lambda: press("-"), height=2, width=7) 
minus.place(x=190, y=150)  
  
multiply = tkinter.Button(root, text=' * ', command=lambda: press("*"), height=2, width=7) 
multiply.place(x=190, y=200)  
  
divide = tkinter.Button(root, text=' / ', command=lambda: press("/"), height=2, width=7) 
divide.place(x=190, y=50) 
  
equal = tkinter.Button(root, text=' = ', command=equalpress, height=5, width=7) 
equal.place(x=250, y=52)

dot=tkinter.Button(root, text=' . ', command=lambda: press("."), height=2, width=7) 
dot.place(x=10, y=200)

pi = tkinter.Button(root, text=' π ', command=lambda: press("π"), height=2, width=7) 
pi.place(x=250, y=150)
  
clear = tkinter.Button(root, text='Clear', command=clear, height=2, width=7) 
clear.place(x=130, y=200) 

delte = tkinter.Button(root, text='<-', command=delete, height=2, width=7) 
delte.place(x=250, y=200)
    
root.mainloop() 
