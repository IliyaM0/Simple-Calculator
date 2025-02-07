from tkinter import *
import tkinter.messagebox

# =============================== Setting ===============================

root = Tk()
root.geometry("400x200")
root.resizable(width=False, height=False)
root.title("Calculator")
color = 'gray'
root.configure(background=color)
# ========================== Variables =================================

number1 = StringVar()
number2 = StringVar()
result = StringVar()
# =============================== Frames ===============================

topFirst = Frame(root, width=400, height=50, bg=color)
topFirst.pack(side=TOP)

topSecond = Frame(root, width=400, height=50, bg=color)
topSecond.pack(side=TOP)

topThird = Frame(root, width=400, height=50, bg=color)
topThird.pack(side=TOP)

topForth = Frame(root, width=400, height=50, bg=color)
topForth.pack(side=TOP)


# ========================== Functions =================================

def errorMSG(msg):
    tkinter.messagebox.showerror("Error!", msg)


def calculate(operation):
    try:
        num1 = float(number1.get())
        num2 = float(number2.get())

        if operation == "+":
            result.set(num1 + num2)
        elif operation == "-":
            result.set(num1 - num2)
        elif operation == "*":
            result.set(num1 * num2)
        elif operation == "/":
            if num2 == 0:
                errorMSG("Division by zero is not allowed!")
            else:
                result.set(num1 / num2)
    except ValueError:
        errorMSG("Invalid input! Please enter valid numbers.")


# =============================== Buttons ===============================

btnPlus = Button(topThird, text="+", width=10, command=lambda: calculate('+'))
btnPlus.pack(side=LEFT)

btnMinus = Button(topThird, text="-", width=10, command=lambda: calculate('-'))
btnMinus.pack(side=LEFT)

btnMulti = Button(topThird, text="*", width=10, command=lambda: calculate('*'))
btnMulti.pack(side=LEFT)

btnDivision = Button(topThird, text="/", width=10, command=lambda: calculate('/'))
btnDivision.pack(side=LEFT)
# ========================== Entries and Labels ==========================

labelFirstNumber = Label(topFirst, text="Input First Number :", bg=color)
labelFirstNumber.pack(side=LEFT, padx=10, pady=10)

firstNumber = Entry(topFirst, textvariable=number1)
firstNumber.pack(side=LEFT)

labelSecondNumber = Label(topSecond, text="Input Second Number :", bg=color)
labelSecondNumber.pack(side=LEFT, padx=10, pady=10)

secondNumber = Entry(topSecond, textvariable=number2)
secondNumber.pack(side=LEFT)

labelResult = Label(topForth, text="The Result :", bg=color)
labelResult.pack(side=LEFT, padx=10, pady=10)

resultNumber = Entry(topForth, textvariable=result, state='readonly')
resultNumber.pack(side=LEFT)

root.mainloop()
