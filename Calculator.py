from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np

root = Tk()
root.title("Graphing Calculator")
root.geometry("359x400")
root.resizable(False,False)
root.config(bg="grey")


e = Entry(root, borderwidth=5, width=50, fg='black', state="disabled")
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

f_num = None
math_operation = None
graph_window = None
fig, ax = None, None
canvas = None
g = None
fig, ax = plt.subplots()
ax.axhline(y=0, color='black', linewidth=1)
ax.axvline(x=0, color='black', linewidth=1)

# Defining Y= function and graph

def trig_graph():
    root.iconify()
    global trig_graph_window, h, canvas, error_label1
    trig_graph_window = Toplevel(root)
    trig_graph_window.title("Graph")
    trig_graph_window.resizable(False, False)
    Label(trig_graph_window, text="Enter Trig Function (e.g. '-2*sin(3*x)'):", padx=10, pady=10).grid(row=0, column=0)
    h = Entry(trig_graph_window, border=5, width=25, fg='black', bg='white')
    h.grid(row=1, column=0)
    error_label1 = Label(trig_graph_window, text="", fg="red")
    error_label1.grid(row=2, column=0)
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_xticks(np.arange(-10, 11, 1))
    ax.set_yticks(np.arange(-10, 11, 1))
    ax.set_aspect('equal')
    ax.grid(True)
    canvas = FigureCanvasTkAgg(fig, master=trig_graph_window)
    canvas.get_tk_widget().grid(row=4, column=0)
    plot_trig_button = Button(trig_graph_window, text="Plot", command=plot_trig_graph)
    plot_trig_button.grid(row=3, column=0, pady=10)

def plot_trig_graph():
    global ax, error_label1
    eqn1 = h.get()
    x1 = np.linspace(-10, 10, 400)
    try:
        eqn1 = eqn1.replace('sin', 'np.sin').replace('cos', 'np.cos').replace('tan', 'np.tan')
        eqn1 = eqn1.replace('log', 'np.log').replace('exp', 'np.exp').replace('sqrt', 'np.sqrt')
        safe_dict = {'np': np, 'x': x1}
        y1 = eval(eqn1, {"__builtins__": None}, safe_dict)
        ax.clear()
        ax.plot(x1, y1)
        ax.set_xlim(-10, 10)
        ax.set_ylim(-10, 10)
        ax.set_xticks(np.arange(-10, 11, 1))
        ax.set_yticks(np.arange(-10, 11, 1))
        ax.grid(True)
        ax.axhline(y=0, color='black', linewidth=1)
        ax.axvline(x=0, color='black', linewidth=1)
        canvas.draw()
        error_label1.config(text="")
    except Exception as e:
        error_label1.config(text=f"Syntax Error: {e}")

def button_graph():
    root.iconify()
    global graph_window, g, canvas, error_label
    graph_window = Toplevel(root)
    graph_window.title("Coordinate Graph")
    graph_window.resizable(False, False)
    Label(graph_window, text="Enter equation (e.g. 'mx+b'):", padx=10, pady=10).grid(row=0, column=0)
    g = Entry(graph_window, border=5, width=25, fg='black', bg='white')
    g.grid(row=1, column=0)
    error_label = Label(graph_window, text="", fg="red")
    error_label.grid(row=2, column=0)
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_xticks(np.arange(-10, 11, 1))
    ax.set_yticks(np.arange(-10, 11, 1))
    ax.set_aspect('equal')
    ax.grid(True)
    canvas = FigureCanvasTkAgg(fig, master=graph_window)
    canvas.get_tk_widget().grid(row=4, column=0)
    plot_button = Button(graph_window, text="Plot", command=plot_graph)
    plot_button.grid(row=3, column=0, pady=10)

def plot_graph():
    global ax, error_label
    eqn = g.get()
    try:
        m, b = [float(x.strip()) for x in eqn.split('x') if x.strip()]
    except:
        error_label.config(text="Invalid input. Please enter an equation in the form of 'mx+b'.")
        return
    x = np.linspace(-10, 10, 100)
    y = m * x + b
    ax.clear()
    ax.plot(x, y)
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_xticks(np.arange(-10, 11, 1))
    ax.set_yticks(np.arange(-10, 11, 1))
    ax.grid(True)
    ax.axhline(y=0, color='black', linewidth=1)
    ax.axvline(x=0, color='black', linewidth=1)
    canvas.draw()
    error_label.config(text="")

# Defining buttons

def button_click(number):
    current = e.get()
    e.config(state="normal")
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
    e.config(state="disabled")


def button_cl():
    e.config(state="normal")
    e.delete(0, END)
    e.config(state="disabled")


def button_ad():
    global f_num
    global math_operation
    math_operation = "addition"
    f_num = float(e.get())
    e.config(state="normal")
    e.delete(0, END)
    e.config(state="disabled")

def button_sub():
    global f_num
    global math_operation
    math_operation = "subtraction"
    f_num = float(e.get())
    e.config(state="normal")
    e.delete(0, END)
    e.config(state="disabled")

def button_multi():
    global f_num
    global math_operation
    math_operation = "multiplication"
    f_num = float(e.get())
    e.config(state="normal")
    e.delete(0, END)
    e.config(state="disabled")

def button_div():
    global f_num
    global math_operation
    math_operation = "division"
    f_num = float(e.get())
    e.config(state="normal")
    e.delete(0, END)
    e.config(state="disabled")

def button_eq():
    try:
        second_number = float(e.get())
        e.config(state="normal")
        e.delete(0, END)
        if math_operation == "addition":
            result = f_num + second_number
        elif math_operation == "subtraction":
            result = f_num - second_number
        elif math_operation == "multiplication":
            result = f_num * second_number
        elif math_operation == "division":
            result = f_num / second_number
        else:
            return
        if result.is_integer():
            e.insert(0, str(int(result)))
        else:
            e.insert(0, str(result))
        e.config(state="disabled")
    except ZeroDivisionError:
        e.config(state="normal")
        e.delete(0, END)
        e.insert(0, "Undefined")
        e.config(state="disabled")


# Making the buttons
button_o = Button(root, bg="light grey", text=".", command=lambda: button_click('.'))
button_1 = Button(root, bg='light grey', text="1", command=lambda: button_click(1))
button_2 = Button(root, bg='light grey', text="2", command=lambda: button_click(2))
button_3 = Button(root, bg='light grey', text="3", command=lambda: button_click(3))
button_4 = Button(root, bg='light grey', text="4", command=lambda: button_click(4))
button_5 = Button(root, bg='light grey', text="5", command=lambda: button_click(5))
button_6 = Button(root, bg='light grey', text="6", command=lambda: button_click(6))
button_7 = Button(root, bg='light grey', text="7", command=lambda: button_click(7))
button_8 = Button(root, bg='light grey', text="8", command=lambda: button_click(8))
button_9 = Button(root, bg='light grey', text="9", command=lambda: button_click(9))
button_0 = Button(root, bg='light grey', text="0", command=lambda: button_click(0))
button_divide = Button(root, bg='light grey', text="/", command=button_div)
button_multiply = Button(root, bg='light grey', text="x", command=button_multi)
button_subtract = Button(root, bg='light grey', text="-", command=button_sub)
button_add = Button(root, bg='light grey', text="+", command=button_ad)
button_clear = Button(root, bg='light grey', text="Clear", command=button_cl)
button_equal = Button(root, bg='light grey', text="=", command=button_eq)
button_y = Button(root, bg='light grey', text='Y=', command=button_graph)
button_trig = Button(root, bg='light grey', text='Trig', command=trig_graph)
button_filler = Button(root, bg='light grey', text=' ')

buttons = [
    [button_7, button_8, button_9, button_multiply],
    [button_4, button_5, button_6, button_subtract],
    [button_1, button_2, button_3, button_add],
    [button_0, button_o, button_clear, button_divide],
    [button_filler, button_y, button_trig, button_equal]
]

for i, row in enumerate(buttons):
    for j, button in enumerate(row):
        button.grid(row=i+1, column=j, padx=1, pady=1, sticky='nsew')

for i in range(5):
    root.grid_rowconfigure(i+1, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

root.mainloop()
#
#           [1] [2] [3] [+]
#           [4] [5] [6] [-]
#           [7] [8] [9] [*]
#           [0] [.] [=] [/]
#           [ ] [Y=] [Trig]
