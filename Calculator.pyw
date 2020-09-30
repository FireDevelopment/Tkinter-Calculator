#imports
try:
    from tkinter import *
except ImportError:
    from Tkinter import *


import os, math

"""
NOTES:
Unlike many previous projects,
I am gonna try to comment the whole code
"""

#windows set up
root = Tk()

for x in range(4):
    root.columnconfigure(x, weight=1)

for y in range(7):
    root.rowconfigure(y, weight=1)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#varibles

"""
These variables are for knowing if a value in the equation bar or input box
needs to be replaced on pressing a button
"""
global numr
numr = False

global er
er = False

global dp
dp = False

global history #this one contains claculator history (It's cleared after you exit)
history = ['None']

#functions
def numpress(num): #When you press a number
    global numr, er, dp
    cinput = inputb.get() #get the current input
    if er == True: #If the text can be replaced
        equationbar.config(text = '')
    if numr == True: #If the text can be replaced
        inputb.delete(0, END)
        if num == '.': #If the new input selection is .
            inputb.insert(0, '0') #add a zero (which will make it 0. after
        numr = False #turn numr off
    if num != '.':
        if cinput == '0':
            inputb.delete(0, END)
            cinput = ''
    cinputl = 0
    for i in cinput:
        cinputl = cinputl + 1 #gets the each charecter
        if i == '.': #if there is already a decimal point...
            dp = True
        else: #if there is not a decimal point...
            if dp != True:
                dp = False
    if num == '.':
        if dp != True: #dp is so you cant add two decimal points
            inputb.insert(cinputl, '{}'.format(num))
    else:
        inputb.insert(cinputl, '{}'.format(num))

def nswitch():
    cinput = inputb.get() #get the current input
    if cinput != '0': #if the number is not 0
        if cinput[0] != '-': #If the enumber is not already negative
            cinput = '-{}'.format(cinput)
            inputb.insert(0, '-') #add it
        else:
            inputb.delete(0, 1)#delete it

def operation(op):
    global numr, er
    if er == True:
        equationbar.config(text = '')
        er = False
    if op == '+':
        cequation = equationbar.cget("text")
        equation = inputb.get()
        try:
            inttest = float(equation)
            equationbar.config(text = cequation+equation+'+')
            cequation = equationbar.cget("text")
            inputb.delete(0, END)
            inputb.insert(0, eval(cequation + '0'))
            numr = True
        except:
            inputb.delete(0, END)
            inputb.insert(0, 'Error')
            numr = True
    if op == '-':
        cequation = equationbar.cget("text")
        equation = inputb.get()
        try:
            inttest = float(equation)
            equationbar.config(text = cequation+equation+'-')
            cequation = equationbar.cget("text")
            inputb.delete(0, END)
            inputb.insert(0, eval(cequation + '0'))
            numr = True
        except:
            inputb.delete(0, END)
            inputb.insert(0, 'Error')
            numr = True
    if op == '*':
        cequation = equationbar.cget("text")
        equation = inputb.get()
        try:
            inttest = float(equation)
            equationbar.config(text = cequation+equation+'*')
            cequation = equationbar.cget("text")
            inputb.delete(0, END)
            inputb.insert(0, eval(cequation + '1'))
            numr = True
        except:
            inputb.delete(0, END)
            inputb.insert(0, 'Error')
            numr = True
    if op == '/':
        cequation = equationbar.cget("text")
        equation = inputb.get()
        try:
            inttest = float(equation)
            equationbar.config(text = cequation+equation+'/')
            cequation = equationbar.cget("text")
            inputb.delete(0, END)
            inputb.insert(0, eval(cequation + '1'))
            numr = True
        except:
            inputb.delete(0, END)
            inputb.insert(0, 'Error')
            numr = True

def clear():
    #clear everything (input box and equation bar)
    inputb.delete(0, END)
    inputb.insert(0, '0')
    equationbar.config(text = '')

def cleare():
    #clear the input box only
    inputb.delete(0, END)
    inputb.insert(0, '0')

def backs():
    cinput = inputb.get() #get the current input
    cinputl = 0 #initiate variable
    for i in cinput: #for each letter in the current input
        cinputl = cinputl + 1 #add 1 to cinputl
    inputb.delete(cinputl - 1, END) #delete the last character in teh input
    cinput = inputb.get() #refresh the current input variable
    if cinput == '' or cinput == '-': #if there is no input left besides a negative sign
        inputb.delete(0, END) #delete it
        inputb.insert(0, '0') #add a zero

def solve():
    global er, numr, history
    cequation = equationbar.cget("text")
    equation = inputb.get()
    try:
        inttest = float(equation)
        equationbar.config(text = cequation+equation)
        cequation = equationbar.cget("text")
        inputb.delete(0, END)
        inputb.insert(0, eval(cequation))
        answer = eval(cequation)
        equationbar.config(text = cequation+'=')
        if history[0] == 'None':
            history = []
        history.append(cequation+'={}'.format(answer))
        numr = True
        er = True
    except:
        inputb.delete(0, END)
        inputb.insert(0, 'Error')
        equationbar.config(text = '')
        numr = True
        


def hoverbutton(b):
    b.config(bg = 'white')

def hoverbuttonleave(b, c):
    b.config(bg = c)

def about():
    root.unbind("0")
    root.unbind("1")
    root.unbind("2")
    root.unbind("3")
    root.unbind("4")
    root.unbind("5")
    root.unbind("6")
    root.unbind("7")
    root.unbind("8")
    root.unbind("9")
    root.unbind(".")
    root.unbind("+")
    root.unbind("-")
    root.unbind("*")
    root.unbind("/")
    root.unbind("=")
    root.unbind("<BackSpace>")
    standardcalc.grid_forget()
    equationbar.grid_forget()
    inputb.grid_forget()
    historypage.grid_forget()
    aboutpage.grid(columnspan = 4, rowspan = 7, sticky=N+S+E+W)

def standcalc():
    root.bind("0", lambda e: numpress(0))
    root.bind("1", lambda e: numpress(1))
    root.bind("2", lambda e: numpress(2))
    root.bind("3", lambda e: numpress(3))
    root.bind("4", lambda e: numpress(4))
    root.bind("5", lambda e: numpress(5))
    root.bind("6", lambda e: numpress(6))
    root.bind("7", lambda e: numpress(7))
    root.bind("8", lambda e: numpress(8))
    root.bind("9", lambda e: numpress(9))
    root.bind(".", lambda e: numpress('.'))
    root.bind("+", lambda e: operation('+'))
    root.bind("-", lambda e: operation('-'))
    root.bind("*", lambda e: operation('*'))
    root.bind("/", lambda e: operation('/'))
    root.bind("=", lambda e: solve())
    root.bind("<BackSpace>", lambda e: backs())
    
    aboutpage.grid_forget()
    historypage.grid_forget()
    equationbar.grid(column = 0, row = 0, columnspan = 4, sticky=N+S+E+W)
    inputb.grid(column = 0, columnspan = 4, row = 1, sticky=N+S+E+W)
    standardcalc.grid(columnspan = 4, rowspan = 7, sticky=N+S+E+W)

def historyf():
    hupdate()
    standardcalc.grid_forget()
    equationbar.grid_forget()
    inputb.grid_forget()
    aboutpage.grid_forget()
    historypage.grid(columnspan = 4, rowspan = 7, sticky=N+S+E+W)
    root.unbind("0")
    root.unbind("1")
    root.unbind("2")
    root.unbind("3")
    root.unbind("4")
    root.unbind("5")
    root.unbind("6")
    root.unbind("7")
    root.unbind("8")
    root.unbind("9")
    root.unbind(".")
    root.unbind("+")
    root.unbind("-")
    root.unbind("*")
    root.unbind("/")
    root.unbind("=")
    root.unbind("<BackSpace>")

def delhistory():
    global history, noh
    history = ['None']
    noh = Label(historypage, text = 'No History', font = ('arial', 20), justify = CENTER, bg = '#DFF0E0')
    noh.grid(column = 0, columnspan = 4, row = 1, sticky=N+E+S+W)
    hlist.grid_forget()
    hscrollx.grid_forget()
    hscroll.grid_forget()
    hclear.grid_forget()
    hclears.grid_forget()

def hupdate():
    global noh
    hlist.delete(0, END)
    for hitem in history:
        if hitem != 'None':
            hlist.insert(END, hitem)
            hlist.grid(column = 0, columnspan = 4, row = 1, sticky=N+E+S+W)
            hscrollx.grid(column = 0, columnspan = 4, row = 2, sticky=N+E+W)
            hscroll.grid(column = 4, columnspan = 1, row = 1, sticky=N+S+E+W)
            hclear.grid(column = 1, row = 6, sticky = N+E+S+W)
            hclears.grid(column = 2, row = 6, sticky = N+E+S+W)
            try:
                noh.grid_forget()
            except:
                print('')
        else:
            noh = Label(historypage, text = 'No History', font = ('arial', 20), justify = CENTER, bg = '#DFF0E0')
            noh.grid(column = 0, columnspan = 4, row = 1, sticky=N+E+S+W)

def clears():
    global history, noh
    cselect = hlist.curselection()
    if not cselect == ():
        hlist.delete(cselect[0])
        del history[cselect[0]]
    size = hlist.size()
    print(size)
    if size == 0:
        history = ['None']
        noh = Label(historypage, text = 'No History', font = ('arial', 20), justify = CENTER, bg = '#DFF0E0')
        noh.grid(column = 0, columnspan = 4, row = 1, sticky=N+E+S+W)
        hlist.grid_forget()
        hscrollx.grid_forget()
        hscroll.grid_forget()
        hclear.grid_forget()
        hclears.grid_forget()

#starting screen

"""
n1 - n0 are number buttons
inputb is teh input box
np is point
nper is percent
nss is to switch the type of number (negative/positive)
nc and nce are clear and clear equation
npl - ne are operations
standardcalc is a frame that the buttons are in
"""
equationbar = Label(root, font = ('arial', 20), text = '', justify = RIGHT, fg = 'black', bg = '#DFF0E0')
equationbar.grid(column = 0, row = 0, columnspan = 4, sticky=N+S+E+W)

inputb = Entry(root, font = ('arial', 40), justify = RIGHT, bd = 19, fg = 'black', bg = '#DFF0E0', relief = RAISED)
inputb.grid(column = 0, columnspan = 4, row = 1, sticky=N+S+E+W)
inputb.insert(0, '0')

standardcalc = Frame(root, bg = '#DFF0E0')
standardcalc.grid(columnspan = 4, rowspan = 7, sticky=N+S+E+W)

for x in range(4):
    standardcalc.columnconfigure(x, weight=1)

for y in range(7):
    standardcalc.rowconfigure(y, weight=1)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


n1 = Button(standardcalc, text = '1', bg = "light green", fg = 'Black', font = ('airal', 30), command = lambda:numpress(1))
n1.grid(column = 0, row = 2, sticky=N+S+E+W, padx = 5, pady = 5)

n2 = Button(standardcalc, text = '2', bg = "light green", fg = 'Black', font = ('airal', 30), command = lambda:numpress(2))
n2.grid(column = 1, row = 2, sticky=N+S+E+W, padx = 5, pady = 5)

n3 = Button(standardcalc, text = '3', bg = "light green", fg = 'Black', font = ('airal', 30), command = lambda:numpress(3))
n3.grid(column = 2, row = 2, sticky=N+S+E+W, padx = 5, pady = 5)

n4 = Button(standardcalc, text = '4', bg = "light green", fg = 'Black', font = ('airal', 30), command = lambda:numpress(4))
n4.grid(column = 0, row = 3, sticky=N+S+E+W, padx = 5, pady = 5)

n5 = Button(standardcalc, text = '5', bg = "light green", fg = 'Black', font = ('airal', 30), command = lambda:numpress(5))
n5.grid(column = 1, row = 3, sticky=N+S+E+W, padx = 5, pady = 5)

n6 = Button(standardcalc, text = '6', bg = "light green", fg = 'Black', font = ('airal', 30), command = lambda:numpress(6))
n6.grid(column = 2, row = 3, sticky=N+S+E+W, padx = 5, pady = 5)

n7 = Button(standardcalc, text = '7', bg = "light green", fg = 'Black', font = ('airal', 30), command = lambda:numpress(7))
n7.grid(column = 0, row = 4, sticky=N+S+E+W, padx = 5, pady = 5)

n8 = Button(standardcalc, text = '8', bg = "light green", fg = 'Black', font = ('airal', 30), command = lambda:numpress(8))
n8.grid(column = 1, row = 4, sticky=N+S+E+W, padx = 5, pady = 5)

n9 = Button(standardcalc, text = '9', bg = "light green", fg = 'Black', font = ('airal', 30), command = lambda:numpress(9))
n9.grid(column = 2, row = 4, sticky=N+S+E+W, padx = 5, pady = 5)

n0 = Button(standardcalc, text = '0', bg = "light green", fg = 'Black', font = ('airal', 30), command = lambda:numpress(0))
n0.grid(column = 0, row = 5, sticky=N+S+E+W, padx = 5, pady = 5)

np = Button(standardcalc, text = '.', bg = "light green", fg = 'Black', font = ('airal', 30), command = lambda:numpress('.'))
np.grid(column = 1, row = 5, sticky=N+S+E+W, padx = 5, pady = 5)

nss = Button(standardcalc, text = '+/-', bg = "light green", fg = 'Black', font = ('airal', 30), command = nswitch)
nss.grid(column = 2, row = 5, sticky=N+S+E+W, padx = 5, pady = 5)

nper = Button(standardcalc, text = 'CE', bg = "light green", fg = 'Black', font = ('airal', 30), command = cleare)
nper.grid(column = 1, row = 6, sticky=N+S+E+W, padx = 5, pady = 5)

nc = Button(standardcalc, text = 'C', bg = "light green", fg = 'Black', font = ('airal', 30), command = clear)
nc.grid(column = 0, row = 6, sticky=N+S+E+W, padx = 5, pady = 5)

nb = Button(standardcalc, text = '⌫', bg = "light green", fg = 'Black', font = ('airal', 30), command = backs)
nb.grid(column = 2, row = 6, sticky=N+S+E+W, padx = 5, pady = 5)

npl = Button(standardcalc, text = '+', bg = "light green", fg = 'Black', font = ('airal', 30), command = lambda:operation('+'))
npl.grid(column = 3, row = 2, sticky=N+S+E+W, padx = 5, pady = 5)

nsu = Button(standardcalc, text = '-', bg = "light green", fg = 'Black', font = ('airal', 30), command = lambda:operation('-'))
nsu.grid(column = 3, row = 3, sticky=N+S+E+W, padx = 5, pady = 5)

nmu = Button(standardcalc, text = '×', bg = "light green", fg = 'Black', font = ('airal', 30), command = lambda:operation('*'))
nmu.grid(column = 3, row = 4, sticky=N+S+E+W, padx = 5, pady = 5)

nd = Button(standardcalc, text = '÷', bg = "light green", fg = 'Black', font = ('airal', 30), command = lambda:operation('/'))
nd.grid(column = 3, row = 5, sticky=N+S+E+W, padx = 5, pady = 5)

ne = Button(standardcalc, text = '=', bg = "#DFF0E0", fg = 'Black', font = ('airal', 30), command = solve)
ne.grid(column = 3, row = 6, sticky=N+S+E+W, padx = 5, pady = 5)

#about page
aboutpage = Frame(root, bg = '#DFF0E0')

aboutl = Label(aboutpage, text = 'About', font = ('arial', 40), bg = '#DFF0E0', fg = '#26c31b')
aboutl.grid(column = 0, columnspan = 4, row = 0, sticky=N+S+E+W)

aboutt = Message(aboutpage, text = 'Welcome to the Calendar by Fire Dev! Do not distribute closed source versions of this and please give credit to the original maker.\n Version 1.0.23.1', bg = '#DFF0E0', fg = 'black', font = ('arial', 20))
aboutt.grid(column = 0, columnspan = 4, row = 2, rowspan = 3,  sticky=N+S+E+W)

devpic = PhotoImage(file = r'./Images/dev.gif')

devpicl = Label(aboutpage, image = devpic, bg = '#DFF0E0')
devpicl.grid(column = 0, columnspan = 4, row = 7, sticky=N+S+E+W)

for x in range(4):
    aboutpage.columnconfigure(x, weight=1)

for y in range(7):
    aboutpage.rowconfigure(y, weight=1)

aboutpage.columnconfigure(0, weight=1)
aboutpage.rowconfigure(0, weight=1)

#history page
historypage = Frame(root, bg = '#DFF0E0')

historyl = Label(historypage, text = 'History', font = ('arial', 40), bg = '#DFF0E0', fg = '#26c31b')
historyl.grid(column = 0, columnspan = 4, row = 0, sticky=N+S+E+W)

hscroll = Scrollbar(historypage)

hscrollx = Scrollbar(historypage, orient=HORIZONTAL)

hlist = Listbox(historypage, yscrollcommand = hscroll.set, xscrollcommand = hscrollx.set, font = ('arial', 20))      

hclear = Button(historypage, text = 'Clear All History', font = ('arial', 15), bg = 'light green', fg = 'black', command = delhistory)

hclears = Button(historypage, text = 'Clear Selection', font = ('arial', 15), bg = 'light green', fg = 'black', command = clears)

hscroll.config(command = hlist.yview)
hscrollx.config(command = hlist.xview)

for x in range(4):
    historypage.columnconfigure(x, weight=1)

for y in range(7):
    historypage.rowconfigure(y, weight=1)

historypage.columnconfigure(0, weight=1)
historypage.rowconfigure(0, weight=1)



#cool button light up stuff for the standard calc
n1.bind("<Enter>", lambda e: hoverbutton(n1))
n1.bind("<Leave>", lambda e: hoverbuttonleave(n1, 'light green'))
n2.bind("<Enter>", lambda e: hoverbutton(n2))
n2.bind("<Leave>", lambda e: hoverbuttonleave(n2, 'light green'))
n3.bind("<Enter>", lambda e: hoverbutton(n3))
n3.bind("<Leave>", lambda e: hoverbuttonleave(n3, 'light green'))
n4.bind("<Enter>", lambda e: hoverbutton(n4))
n4.bind("<Leave>", lambda e: hoverbuttonleave(n4, 'light green'))
n5.bind("<Enter>", lambda e: hoverbutton(n5))
n5.bind("<Leave>", lambda e: hoverbuttonleave(n5, 'light green'))
n6.bind("<Enter>", lambda e: hoverbutton(n6))
n6.bind("<Leave>", lambda e: hoverbuttonleave(n6, 'light green'))
n7.bind("<Enter>", lambda e: hoverbutton(n7))
n7.bind("<Leave>", lambda e: hoverbuttonleave(n7, 'light green'))
n8.bind("<Enter>", lambda e: hoverbutton(n8))
n8.bind("<Leave>", lambda e: hoverbuttonleave(n8, 'light green'))
n9.bind("<Enter>", lambda e: hoverbutton(n9))
n9.bind("<Leave>", lambda e: hoverbuttonleave(n9, 'light green'))
n0.bind("<Enter>", lambda e: hoverbutton(n0))
n0.bind("<Leave>", lambda e: hoverbuttonleave(n0, 'light green'))
np.bind("<Enter>", lambda e: hoverbutton(np))
np.bind("<Leave>", lambda e: hoverbuttonleave(np, 'light green'))
nss.bind("<Enter>", lambda e: hoverbutton(nss))
nss.bind("<Leave>", lambda e: hoverbuttonleave(nss, 'light green'))
nper.bind("<Enter>", lambda e: hoverbutton(nper))
nper.bind("<Leave>", lambda e: hoverbuttonleave(nper, 'light green'))
nc.bind("<Enter>", lambda e: hoverbutton(nc))
nc.bind("<Leave>", lambda e: hoverbuttonleave(nc, 'light green'))
nb.bind("<Enter>", lambda e: hoverbutton(nb))
nb.bind("<Leave>", lambda e: hoverbuttonleave(nb, 'light green'))
npl.bind("<Enter>", lambda e: hoverbutton(npl))
npl.bind("<Leave>", lambda e: hoverbuttonleave(npl, 'light green'))
nsu.bind("<Enter>", lambda e: hoverbutton(nsu))
nsu.bind("<Leave>", lambda e: hoverbuttonleave(nsu, 'light green'))
nmu.bind("<Enter>", lambda e: hoverbutton(nmu))
nmu.bind("<Leave>", lambda e: hoverbuttonleave(nmu, 'light green'))
nd.bind("<Enter>", lambda e: hoverbutton(nd))
nd.bind("<Leave>", lambda e: hoverbuttonleave(nd, 'light green'))
ne.bind("<Enter>", lambda e: hoverbutton(ne))
ne.bind("<Leave>", lambda e: hoverbuttonleave(ne, '#DFF0E0'))
root.bind("0", lambda e: numpress(0))
root.bind("1", lambda e: numpress(1))
root.bind("2", lambda e: numpress(2))
root.bind("3", lambda e: numpress(3))
root.bind("4", lambda e: numpress(4))
root.bind("5", lambda e: numpress(5))
root.bind("6", lambda e: numpress(6))
root.bind("7", lambda e: numpress(7))
root.bind("8", lambda e: numpress(8))
root.bind("9", lambda e: numpress(9))
root.bind(".", lambda e: numpress('.'))
root.bind("+", lambda e: operation('+'))
root.bind("-", lambda e: operation('-'))
root.bind("*", lambda e: operation('*'))
root.bind("/", lambda e: operation('/'))
root.bind("=", lambda e: solve())
root.bind("<BackSpace>", lambda e: backs())

#menubar
menubar = Menu(root)

menubar.add_command(label = 'Calculator', command = standcalc)

menubar.add_command(label = 'About', command = about)

menubar.add_command(label = 'History', command = historyf)

root.geometry('550x575')
root.config(menu = menubar)
root.iconbitmap('./Images/Icon.ico')
root.minsize(470, 475)
root.title('Calculator')
root.config(bg = '#DFF0E0')
root.mainloop()
