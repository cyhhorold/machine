
# |  _ \|  _ \ / _ \ / ___|  _ \    / \  |  \/  |  \/  | ____|  _ \
# | |_) | |_) | | | | |  _| |_) |  / _ \ | |\/| | |\/| |  _| | |_) |
# |  __/|  _ <| |_| | |_| |  _ <  / ___ \| |  | | |  | | |___|  _ <
# |_|   |_| \_\\___/ \____|_| \_\/_/   \_\_|  |_|_|  |_|_____|_| \_\
#  _     ___ ____ _____
# | |   |_ _/ ___|_   _|
# | |    | |\___ \ | |
# | |___ | | ___) || |
# |_____|___|____/ |_|


#  ابوالفضل چرختاب اسد پور (سرگروه)
#  حسین حیرانی 



from tkinter import *
import math
import tkinter.messagebox

root = Tk()
root.title("ماشین حساب سیمرغ")
root.configure(background = 'green')
root.resizable(width=False, height=False)
root.geometry("596x525+450+90")



calc = Frame(root)
calc.grid()



class Calc():
    def __init__(self):
        self.total=00
        self.current=''
        self.input_value=True
        self.check_sum=False
        self.op=''
        self.result=False

    def numberEnter(self, num):
        self.result=False
        firstnum=txtDisplay.get()
        secondnum=str(num)
        if self.input_value:
            self.current = secondnum
            self.input_value=False
        else:
            if secondnum == '.':
                if secondnum in firstnum:
                    return
            self.current = firstnum+secondnum
        self.display(self.current)

    def sum_of_total(self):
        self.result=True
        self.current=float(self.current)
        if self.check_sum==True:
            self.valid_function()
        else:
            self.total=float(txtDisplay.get())

    def display(self, value):
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, value)

    def valid_function(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "sub":
            self.total -= self.current
        if self.op == "multi":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        if self.op == "mod":
            self.total %= self.current
        self.input_value=True
        self.check_sum=False
        self.display(self.total)

    def operation(self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total=self.current
            self.input_value=True
        self.check_sum=True
        self.op=op
        self.result=False

    def Clear_Entry(self):
        self.result = False
        self.current = "0"
        self.display(0)
        self.input_value=True

    def All_Clear_Entry(self):
        self.Clear_Entry()
        self.total=0

    def pi(self):
        self.result =  False
        self.current = math.pi
        self.display(self.current)



    def tau(self):
        self.result =  False
        self.current = math.tau
        self.display(self.current)


    def valiuse2(self):

        self.result = False
        user = float(txtDisplay.get())
        if user >= 0:
            user=user
        else:
            user=user  * (-1)
        self.current = user
        self.display(self.current)


    def Pow2(self):
        self.result = False
        user = float(txtDisplay.get())
        user = user * user
        self.current = user
        self.display(self.current)



    def Pow3(self):
        self.result = False
        user = float(txtDisplay.get())
        user = user * user * user
        self.current = user
        self.display(self.current)


    def mathPM(self):
        self.result = False
        self.current = -(float(txtDisplay.get()))
        self.display(self.current)

    def squared(self):
        self.result = False
        self.current = math.sqrt(float(txtDisplay.get()))
        self.display(self.current)

    def log10(self):
        self.result = False
        self.current = math.log10(float(txtDisplay.get()))
        self.display(self.current)



added_value = Calc()


txtDisplay = Entry(calc, font=('Helvetica',20,'bold'),bg='blue',fg='white', bd=30,
                   width=28,justify=RIGHT)
txtDisplay.grid(row=0,column=0, columnspan=4, pady=1)
txtDisplay.insert(0,"0")

# ====================================================================================================== #


numberpad = "789456123"
i=0
btn = []
for j in range(2,5):
    for k in range(3):
        btn.append(Button(calc, width=6, height=2, bg='white',fg='green', font=('Helvetica',25,'bold'),
                          bd=4,text=numberpad[i]))
        btn[i].grid(row=j, column= k, pady = 1)
        btn[i]["command"]=lambda x=numberpad[i]:added_value.numberEnter(x)
        i+=1

# ====================================================================================================== #


btnClear = Button(calc, text=chr(67),width=6, height=2,bg='red',fg='white', font=('Helvetica',20,'bold')
                  ,bd=4, command=added_value.Clear_Entry).grid(row=1, column= 0, pady = 1)

btnAllClear = Button(calc, text=chr(67)+chr(69),width=6, height=2,bg='red',fg='white', font=('Helvetica'
            ,20,'bold'),bd=4,command=added_value.All_Clear_Entry).grid(row=1, column= 1, pady = 1)





btnAbso = Button(calc, text="| x |",width=6, height=2,bg='black',fg='white', font=('Helvetica',20,'bold'),
                  bd=4,command=added_value.valiuse2).grid(row=3, column= 4, pady = 1)








btnsq = Button(calc, text="\u221A",width=6, height=2,bg='black',fg='white', font=('Helvetica',20,'bold'),
                  bd=4,command=added_value.squared).grid(row=1, column= 2, pady = 1)

btnAdd = Button(calc, text="+",width=6, height=2,bg='black',fg='white', font=('Helvetica',20,'bold'),
                  bd=4,command=lambda:added_value.operation("add")
                ).grid(row=1, column= 3, pady = 1)

btnSub = Button(calc, text="-",width=6, height=2,bg='black',fg='white', font=('Helvetica',20,'bold'),
                  bd=4,command=lambda:added_value.operation("sub")
                ).grid(row=2, column= 3, pady = 1)

btnMul = Button(calc, text="*",width=6, height=2,bg='black',fg='white', font=('Helvetica',20,'bold'),
                  bd=4,command=lambda:added_value.operation("multi")
                ).grid(row=3, column= 3, pady = 1)



btnDiv = Button(calc, text="/",width=6, height=2,bg='black',fg='white', font=('Helvetica',20,'bold'),
                  bd=4,command=lambda:added_value.operation("divide")
                ).grid(row=4, column= 3, pady = 1)

btnZero = Button(calc, text="0",width=6, height=2,bg='white',fg='green', font=('Helvetica',20,'bold'),
                  bd=4,command=lambda:added_value.numberEnter(0)
                 ).grid(row=5, column= 0, pady = 1)

btnDot = Button(calc, text=".",width=6, height=2,bg='black',fg='white', font=('Helvetica',20,'bold'),
                  bd=4,command=lambda:added_value.numberEnter(".")
                ).grid(row=5, column= 1, pady = 1)
btnPM = Button(calc, text=chr(177),width=6, height=2,bg='black',fg='white', font=('Helvetica',20,'bold'),
                  bd=4,command=added_value.mathPM).grid(row=5, column= 2, pady = 1)

btnEquals = Button(calc, text="=",width=6, height=2,bg='green',fg='white', font=('Helvetica',20,'bold'),
                  bd=4,command=added_value.sum_of_total).grid(row=5, column= 3, pady = 1)



btnPi = Button(calc, text="pi",width=6, height=2,bg='black',fg='white', font=('Helvetica',20,'bold'),
                  bd=4,command=added_value.pi).grid(row=1, column= 4, pady = 1)


btnlog10 = Button(calc, text="log10",width=6, height=2,bg='black',fg='white', font=('Helvetica',20,'bold')
                ,bd=4,command=added_value.log10).grid(row=2, column= 4, pady = 1)


btnPow2 = Button(calc, text="X2",width=6, height=2,bg='black',fg='white', font=('Helvetica',20,'bold'),
                  bd=4,command=added_value.Pow2).grid(row=4, column= 4, pady = 1)



btnPow3 = Button(calc, text="X3",width=6, height=2,bg='black',fg='white', font=('Helvetica',20,'bold'),
                  bd=4,command=added_value.Pow3).grid(row=5, column= 4, pady = 1)




lblDisplay = Label(calc, text = "Calculator",font=('Helvetica',15,'bold'),
                   bg='black',fg='white',justify=CENTER)
lblDisplay.grid(row=0, column= 4,columnspan=4)

# ====================================================================================================== #

def iExit():
    iExit = tkinter.messagebox.askyesno("Scientific Calculator","Do you want to exit ?")
    if iExit>0:
        root.destroy()
        return

def Scientific():
    root.resizable(width=False, height=False)
    root.geometry("944x568+0+0")


def Standard():
    root.resizable(width=False, height=False)
    root.geometry("480x568+0+0")

# ====================================================================================================== #

menubar = Menu(calc)


root.config(menu=menubar)

root.mainloop()
