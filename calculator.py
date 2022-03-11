from email.policy import default
from tkinter import *

from click import option
from soupsieve import select

# A function to get all the thing, button etc a the window

def all_children(window):
    _list = window.winfo_children()

    for item in _list:
        if item.winfo_children():
            _list.extend(item.winfo_children())

    return _list


# Few click button code for handling equals and  Clear.

def click(event):
    global sval
    text=event.widget.cget("text")
    if text=="=":
        try:
            if sval.get().isdigit():
                value=int(sval.get())
            else:
                value=eval(sval.get())
            sval.set(value)
            screen.update()
        except:
            sval.set("Error")
    elif text=="c":
        sval.set("")
        screen.update()
    else:
        sval.set(sval.get()+text)
        screen.update()


# function returning square root
def sq_rt(event):
    global sval
    try:
        if sval.get().isdigit():
            value=int(sval.get())
            a=value**0.5
            return sval.set(a)
        else:
            value=eval(sval.get())
            value=int(value)
            a=value**0.5
            sval.set(a)
            screen.update()
    except:
        sval.set("Error")

# Function returning square
def square(event):
    global sval
    try:
        if sval.get().isdigit():
            value=float(sval.get())
            a=value*value
            return sval.set(a)
            screen.update()
        else:
            value=eval(sval.get())
            value=float(value)
            a=value*value
            sval.set(a)
            screen.update()
    except:
        sval.set("Error")
        screen.update()

# function returning cube
def cube(event):
    global sval
    try:
        if sval.get().isdigit():
            value=int(sval.get())
            a = value*value*value
            return sval.set(a)
            screen.update()
        else:
            value=eval(sval.get())
            value=int(value)
            a=value*value*value
            sval.set(a)
            screen.update()
    except:
        sval.set("Error")
        screen.update()




# main code for managing and creating all functional buttons like numbers, operators, equals, Clear, square and square_root,cube etc. 
def standard():
    # Clearing Screen
    widget_list = all_children(root)
    for item in widget_list:
        item.pack_forget()
    
    # Starting to add buttons and entry on screen
    screen=Entry(root,textvar=sval,font="lucida 40 bold")
    screen.pack(fill="x",ipadx=8,pady=10,padx=10)
    
    f1=Frame(root,bg="yellow")  #Frame For storing buttons

    button_of_calculator=Button(f1,text=".",padx=106.5,pady=2,font="lucida 35 bold")
    button_of_calculator.pack(side=LEFT,anchor=SW)
    button_of_calculator.bind("<Button-1>",click)
    button_of_calculator=Button(f1,text="0",padx=100.4,pady=2,font="lucida 35 bold")
    button_of_calculator.pack(side=LEFT)
    button_of_calculator.bind("<Button-1>",click)
    button_of_calculator=Button(f1,text="cube",padx=58,pady=2,font="lucida 35 bold")
    button_of_calculator.pack(side=LEFT)
    button_of_calculator.bind("<Button-1>",cube)
    button_of_calculator=Button(f1,text="/",padx=111,pady=2,font="lucida 35 bold")
    button_of_calculator.pack(side=LEFT)
    button_of_calculator.bind("<Button-1>",click)
    f1.pack(side=BOTTOM,anchor=SW)


    f1=Frame(root,bg="yellow") #Frame For storing buttons

    button_of_calculator=Button(f1,text="9",padx=100,pady=2,font="lucida 35 bold")
    button_of_calculator.pack(side=LEFT,anchor=SW)
    button_of_calculator.bind("<Button-1>",click)
    button_of_calculator=Button(f1,text="8",padx=100,pady=2,font="lucida 35 bold")
    button_of_calculator.pack(side=LEFT)
    button_of_calculator.bind("<Button-1>",click)
    button_of_calculator=Button(f1,text="7",padx=104.5,pady=2,font="lucida 35 bold")
    button_of_calculator.pack(side=LEFT)
    button_of_calculator.bind("<Button-1>",click)
    button_of_calculator=Button(f1,text="+",padx=100,pady=2,font="lucida 35 bold")
    button_of_calculator.pack(side=LEFT)
    button_of_calculator.bind("<Button-1>",click)
    f1.pack(side=BOTTOM,anchor=SW)

    f1=Frame(root,bg="yellow") #Frame For storing buttons

    button_of_calculator=Button(f1,text="6",padx=100,pady=2,font="lucida 35 bold")
    button_of_calculator.pack(side=LEFT)
    button_of_calculator.bind("<Button-1>",click)
    button_of_calculator=Button(f1,text="5",padx=100,pady=2,font="lucida 35 bold")
    button_of_calculator.pack(side=LEFT)
    button_of_calculator.bind("<Button-1>",click)
    button_of_calculator=Button(f1,text="4",padx=104.5,pady=2,font="lucida 35 bold")
    button_of_calculator.pack(side=LEFT)
    button_of_calculator.bind("<Button-1>",click)
    button_of_calculator=Button(f1,text="-",padx=109.5,pady=2,font="lucida 35 bold")
    button_of_calculator.pack(side=LEFT)
    button_of_calculator.bind("<Button-1>",click)
    f1.pack(side=BOTTOM,anchor=SW)

    f1=Frame(root,bg="yellow") #Frame For storing buttons

    button_of_calculator=Button(f1,text="3",padx=100,pady=2,font="lucida 35 bold")
    button_of_calculator.pack(side=LEFT)
    button_of_calculator.bind("<Button-1>",click)
    button_of_calculator=Button(f1,text="2",padx=100,pady=2,font="lucida 35 bold")
    button_of_calculator.pack(side=LEFT)
    button_of_calculator.bind("<Button-1>",click)
    button_of_calculator=Button(f1,text="1",padx=104.5,pady=2,font="lucida 35 bold")
    button_of_calculator.pack(side=LEFT)
    button_of_calculator.bind("<Button-1>",click)
    button_of_calculator=Button(f1,text="*",padx=106.7,pady=2,font="lucida 35 bold")
    button_of_calculator.pack(side=LEFT)
    button_of_calculator.bind("<Button-1>",click)
    f1.pack(side=BOTTOM,anchor=SW)

    f1=Frame(root,bg="yellow") #Frame For storing buttons

    button_of_calculator=Button(f1,text="√",padx=100,pady=2,font="lucida 35 bold") # for square root
    button_of_calculator.pack(side=LEFT)
    button_of_calculator.bind("<Button-1>",sq_rt)
    button_of_calculator=Button(f1,text="s",padx=102.5,pady=2,font="lucida 35 bold") # for square
    button_of_calculator.pack(side=LEFT)
    button_of_calculator.bind("<Button-1>",square)
    button_of_calculator=Button(f1,text="c",padx=106.45,pady=2,font="lucida 35 bold") # To clear Entry or all calculations
    button_of_calculator.pack(side=LEFT)
    button_of_calculator.bind("<Button-1>",click)
    button_of_calculator=Button(f1,text="=",padx=100,pady=2,font="lucida 35 bold") # to perform calculations
    button_of_calculator.pack(side=LEFT)
    button_of_calculator.bind("<Button-1>",click)
    f1.pack(side=BOTTOM,anchor=SW)




def programmer():
    # Clearing Screen
    widget_list = all_children(root)
    for item in widget_list:
        item.pack_forget()
    
    # Starting to add buttons and entry on screen
    screen=Entry(root,textvar=sval,font="lucida 40 bold")
    screen.pack(fill="x",ipadx=8,pady=10,padx=10)

    optionType = StringVar()

    options = ["Binary", "Decimal", "Octal", "HexaDecimal"]
    optionType.set(options[1])
    Selected = OptionMenu(root, optionType, *options)
    Selected.pack()


if __name__ == "__main__":
    root=Tk()

    # Creating Window
    # root.geometry("1300x700")
    root.title("Simple Calculator")


    sval=StringVar() # Main Entry wigit which takes and stores calculations.
    sval.set("")


# Creating Entry for presenting calculations on screen
    screen = Entry(root,textvar=sval,font="lucida 40 bold")
    screen.pack(fill="x",ipadx=8,pady=10,padx=10)

    standard()
    
    # Menu code for future use mainly for making more than one type of calculator and switching between them
    Main_Menu=Menu(root)

    menu1=Menu(Main_Menu,tearoff=0)
    menu1.add_command(label="Standard", command=standard)
    menu1.add_command(label="Programmer", command=programmer)
    menu1.add_separator()
    root.config(menu=Main_Menu)
    Main_Menu.add_cascade(label="File", menu=menu1)

    root.mainloop()
