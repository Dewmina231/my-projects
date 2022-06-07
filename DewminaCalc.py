

from tkinter import *



window = Tk()

window.title('Calculator')
window.geometry('350x520')

window.config(bg="red")


btn_h, btn_w = 2,10

expresion = ''

operators = ["+","-","*","/"]

def pressBackspace():
    global expresion

    expresion = expresion[:-1]
    label.config(text = expresion)
    print(expresion)




def press(key):

    global expresion

    if key in operators:
        for o in operators:
            if o in expresion:
                pressEquals()

    expresion = expresion + key
    


    label.config(text = expresion)



    print(expresion)

def pressWithEwuals(key):
    press(key)
    pressEquals()

def pressEquals():
    global expresion
    expresion = str(eval(expresion))
    label.config(text = expresion)
    print(expresion)

def clear():
    global expresion
    expresion=''
    label.config(text=expresion)

label = Label(window,text = expresion, height = 3, width = 4*btn_w+5)
label.grid(column=0, row=0,columnspan=4, rowspan=1)

btn = Button(window, text = "%", bg ="grey", height = btn_h, width = btn_w, command=lambda: press("%"))
btn.grid(column= 0, row=1)

btn = Button(window, text = "CE", bg ="grey", height = btn_h, width = btn_w, command=lambda: clear())
btn.grid(column= 1, row=1)

btn = Button(window, text = "C", bg ="grey", height = btn_h, width = btn_w,command=lambda: clear())
btn.grid(column= 2, row=1)

btn = Button(window, text = "<x", bg ="grey", height = btn_h, width = btn_w,command=lambda: pressBackspace())
btn.grid(column= 3, row=1)

btn = Button(window, text = "1/x", bg ="grey", height = btn_h, width = btn_w,command=lambda: pressWithEwuals("**(-1)"))
btn.grid(column= 0, row=2)

btn = Button(window, text = "x^2", bg ="grey", height = btn_h, width = btn_w,command=lambda: pressWithEwuals("**2"))
btn.grid(column= 1, row=2)

btn = Button(window, text = "2√x", bg ="grey", height = btn_h, width = btn_w,command=lambda: pressWithEwuals("**(1/2)"))
btn.grid(column= 2, row=2)

btn = Button(window, text = "/", bg ="grey", height = btn_h, width = btn_w,command=lambda: press("/"))
btn.grid(column= 3, row=2)

btn = Button(window, text = "7", bg ="grey", height = btn_h, width = btn_w,command=lambda: press("7"))
btn.grid(column= 0, row=3)


btn = Button(window, text = "8", bg ="grey", height = btn_h, width = btn_w,command=lambda: press("8"))
btn.grid(column= 1, row=3)

btn = Button(window, text = "9", bg ="grey", height = btn_h, width = btn_w,command=lambda: press("9"))
btn.grid(column= 2, row=3)

btn = Button(window, text = "*", bg ="grey", height = btn_h, width = btn_w,command=lambda: press("*"))
btn.grid(column= 3, row=3)

btn = Button(window, text = "4", bg ="grey", height = btn_h, width = btn_w,command=lambda: press("4"))
btn.grid(column= 0, row=4)

btn = Button(window, text = "5", bg ="grey", height = btn_h, width = btn_w,command=lambda: press("5"))
btn.grid(column= 1, row=4)

btn = Button(window, text = "6", bg ="grey", height = btn_h, width = btn_w,command=lambda: press("6"))
btn.grid(column= 2, row=4)

btn = Button(window, text = "-", bg ="grey", height = btn_h, width = btn_w,command=lambda: press("-"))
btn.grid(column= 3, row=4)

btn = Button(window, text = "1", bg ="grey", height = btn_h, width = btn_w,command=lambda: press("1"))
btn.grid(column= 0, row=5)

btn = Button(window, text = "2", bg ="grey", height = btn_h, width = btn_w,command=lambda: press("2"))
btn.grid(column= 1, row=5)

btn = Button(window, text = "3", bg ="grey", height = btn_h, width = btn_w,command=lambda: press("3"))
btn.grid(column= 2, row=5)

btn = Button(window, text = "+", bg ="grey", height = btn_h, width = btn_w,command=lambda: press("+"))
btn.grid(column= 3, row=5)


btn = Button(window, text = "+/-", bg ="grey", height = btn_h, width = btn_w,command=lambda: pressWithEwuals("*-1"))
btn.grid(column= 0, row=6)


btn = Button(window, text = "0", bg ="grey", height = btn_h, width = btn_w,command=lambda: press("0"))
btn.grid(column= 1, row=6)


btn = Button(window, text = ".", bg ="grey", height = btn_h, width = btn_w,command=lambda: press("."))
btn.grid(column= 2, row=6)


btn = Button(window, text = "=", bg ="#0b6aa2", height = btn_h, width = btn_w,command=lambda: pressEquals())
btn.grid(column= 3, row=6)














window.mainloop()


