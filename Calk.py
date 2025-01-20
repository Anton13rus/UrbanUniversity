import tkinter as tk


def get_values():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    return num1, num2


def insert_values(value):
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, value)


def add():
    num1, num2 = get_values()
    res = num1 + num2
    insert_values(res)

def sub():
    num1, num2 = get_values()
    res = num1 - num2
    insert_values(res)

def div():
    num1, num2 = get_values()
    res = num1 / num2
    insert_values(res)

def mul():
    num1, num2 = get_values()
    res = num1 * num2
    insert_values(res)


window = tk.Tk()
window.title('Калькулятор')
window.geometry("350x350")
window.resizable(False, False)


number1_entry = tk.Entry(window, width=28)
number1_entry.place(x=100, y=75)

number2_entry = tk.Entry(window, width=28)
number2_entry.place(x=100, y=150)

answer_entry = tk.Entry(window, width=28)
answer_entry.place(x=100, y=300)

tk.Label(window, text="Введите первое число:").place(x=100, y=50)
tk.Label(window, text="Введите второе число:").place(x=100, y=125)
tk.Label(window, text="Ответ:").place(x=100, y=275)

tk.Button(window, text="+", width=2, height=2, command=add).place(x=100, y=200)
tk.Button(window, text="-", width=2, height=2, command=sub).place(x=150, y=200)
tk.Button(window, text="*", width=2, height=2, command=mul).place(x=200, y=200)
tk.Button(window, text="/", width=2, height=2, command=div).place(x=250, y=200)


window.mainloop()