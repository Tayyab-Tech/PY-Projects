from tkinter import *

def button_press(num):
    global equation_text
    equation_text = equation_text+str(num)
    equation_label.set(equation_text)
def equals():
    global equation_text
    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
    except ZeroDivisionError:
        equation_label.set("Arithmetic Error")
        equation_text = ""
    except SyntaxError:
        equation_label.set("Syntax error")
        equation_text = ""

    
def clear():
    global equation_text
    equation_label.set("")
    equation_text = ""

window = Tk()

window.title("Calculator")
window.geometry("500x490")

equation_text = ""

equation_label = StringVar()

label = Label(window,textvariable=equation_label,font=("Helvetica",32),padx=5,pady=5,bg="white",width=500)
label.pack()
 
frame =Frame(window)
frame.pack()

button = Button(frame,text=1,width=17,height=5,command=lambda: button_press(1)).grid(row=0,column=0)
button = Button(frame,text=2,width=17,height=5,command=lambda: button_press(2)).grid(row=0,column=1)
button = Button(frame,text=3,width=17,height=5,command=lambda: button_press(3)).grid(row=0,column=2)
button = Button(frame,text='+',width=17,height=5,command=lambda: button_press('+')).grid(row=0,column=3)
button = Button(frame,text=4,width=17,height=5,command=lambda: button_press(4)).grid(row=1,column=0)
button = Button(frame,text=5,width=17,height=5,command=lambda: button_press(5)).grid(row=1,column=1)
button = Button(frame,text=6,width=17,height=5,command=lambda: button_press(6)).grid(row=1,column=2)
button = Button(frame,text='-',width=17,height=5,command=lambda: button_press('-')).grid(row=1,column=3)
button = Button(frame,text=7,width=17,height=5,command=lambda: button_press(7)).grid(row=2,column=0)
button = Button(frame,text=8,width=17,height=5,command=lambda: button_press(8)).grid(row=2,column=1)
button = Button(frame,text=9,width=17,height=5,command=lambda: button_press(9)).grid(row=2,column=2)
button = Button(frame,text='*',width=17,height=5,command=lambda: button_press('*')).grid(row=2,column=3)
button = Button(frame,text='.',width=17,height=5,command=lambda: button_press('.')).grid(row=3,column=0)
button = Button(frame,text=0,width=17,height=5,command=lambda: button_press(0)).grid(row=3,column=1)
button = Button(frame,text='/',width=17,height=5,command=lambda: button_press('/')).grid(row=3,column=2)
button = Button(frame,text='=',width=17,height=5,command=equals).grid(row=3,column=3)
button = Button(frame,text='Clear',width=17,height=5,command=clear).grid(row=4,columnspan=4)

window.mainloop()