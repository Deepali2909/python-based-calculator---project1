import tkinter as tk

# main window
root = tk.Tk()
root.title("Deepali Calculator")

# StringVar to hold the input and output
expression = ""

# Function to update the input field
def press(num):
    global expression
    expression += str(num)
    input_text.set(expression)

# Function to evaluate the expression
def equalpress():
    try:
        global expression
        total = str(eval(expression))
        input_text.set(total)
        expression = total
    except Exception as e:
        input_text.set("Error")
        expression = ""

# Function to clear the input field
def clear():
    global expression
    expression = ""
    input_text.set("")

# a StringVar for input field
input_text = tk.StringVar()

# an input field
input_frame = tk.Frame(root, width=312, height=50, bd=2, highlightbackground="black", highlightcolor="black", highlightthickness=1)
input_frame.pack(side=tk.TOP)

input_field = tk.Entry(input_frame, font=('times new roman', 22, 'bold'), textvariable=input_text, width=40, bg="#eee", bd=2, justify=tk.RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)  # Internal padding for better display view

# frame for buttons
btns_frame = tk.Frame(root, width=312, height=272.5, bg="grey")
btns_frame.pack()

# 1st row
clear = tk.Button(btns_frame, text="AC", fg="black", width=21, height=3, bd=2, bg="#1bd2e3", cursor="hand2", command=clear)
clear.grid(row=0, column=0, columnspan=2, padx=1, pady=1)

divide = tk.Button(btns_frame, text="/", fg="black", width=10, height=3, bd=2, bg="#c8dbe0", cursor="hand2", command=lambda: press("/"))
divide.grid(row=0, column=3, padx=1, pady=1)

# 2nd row
seven = tk.Button(btns_frame, text="7", fg="black", width=10, height=3, bd=2, bg="#adbab3", cursor="hand2", command=lambda: press(7))
seven.grid(row=1, column=0, padx=1, pady=1)

eight = tk.Button(btns_frame, text="8", fg="black", width=10, height=3, bd=2, bg="#adbab3", cursor="hand2", command=lambda: press(8))
eight.grid(row=1, column=1, padx=1, pady=1)

nine = tk.Button(btns_frame, text="9", fg="black", width=10, height=3, bd=2, bg="#adbab3", cursor="hand2", command=lambda: press(9))
nine.grid(row=1, column=2, padx=1, pady=1)

multiply = tk.Button(btns_frame, text="*", fg="black", width=10, height=3, bd=2, bg="#c8dbe0", cursor="hand2", command=lambda: press("*"))
multiply.grid(row=1, column=3, padx=1, pady=1)

# 3rd row
four = tk.Button(btns_frame, text="4", fg="black", width=10, height=3, bd=2, bg="#adbab3", cursor="hand2", command=lambda: press(4))
four.grid(row=2, column=0, padx=1, pady=1)

five = tk.Button(btns_frame, text="5", fg="black", width=10, height=3, bd=2, bg="#adbab3", cursor="hand2", command=lambda: press(5))
five.grid(row=2, column=1, padx=1, pady=1)

six = tk.Button(btns_frame, text="6", fg="black", width=10, height=3, bd=2, bg="#adbab3", cursor="hand2", command=lambda: press(6))
six.grid(row=2, column=2, padx=1, pady=1)

subtract = tk.Button(btns_frame, text="-", fg="black", width=10, height=3, bd=2, bg="#c8dbe0", cursor="hand2", command=lambda: press("-"))
subtract.grid(row=2, column=3, padx=1, pady=1)

# 4th row
one = tk.Button(btns_frame, text="1", fg="black", width=10, height=3, bd=2, bg="#adbab3", cursor="hand2", command=lambda: press(1))
one.grid(row=3, column=0, padx=1, pady=1)

two = tk.Button(btns_frame, text="2", fg="black", width=10, height=3, bd=2, bg="#adbab3", cursor="hand2", command=lambda: press(2))
two.grid(row=3, column=1, padx=1, pady=1)

three = tk.Button(btns_frame, text="3", fg="black", width=10, height=3, bd=2, bg="#adbab3", cursor="hand2", command=lambda: press(3))
three.grid(row=3, column=2, padx=1, pady=1)

add = tk.Button(btns_frame, text="+", fg="black", width=10, height=3, bd=2, bg="#c8dbe0", cursor="hand2", command=lambda: press("+"))
add.grid(row=3, column=3, padx=1, pady=1)

# 5th row
zero = tk.Button(btns_frame, text="0", fg="black", width=21, height=3, bd=2, bg="#adbab3", cursor="hand2", command=lambda: press(0))
zero.grid(row=4, column=0, columnspan=2, padx=1, pady=1)

decimal = tk.Button(btns_frame, text=".", fg="black", width=10, height=3, bd=2, bg="#adbab3", cursor="hand2", command=lambda: press("."))
decimal.grid(row=4, column=2, padx=1, pady=1)

equals = tk.Button(btns_frame, text="=", fg="black", width=10, height=3, bd=2, bg="#c8dbe0", cursor="hand2", command=equalpress)
equals.grid(row=4, column=3, padx=1, pady=1)

roots = tk.Button(btns_frame, text="x^n", fg="black", width=10, height=3, bd=2, bg="#c8dbe0", cursor="hand2", command=lambda: press("**"))
roots.grid(row=0, column=2, padx=1, pady=1)

# GUI loop
root.mainloop()
