
import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN

window = tk.Tk()
window.title('Calculator')
frame = tk.Frame(master=window, bg="black", padx=10)
frame.pack()
entry = tk.Entry(master=frame, relief=SUNKEN, borderwidth=3, width=30)
entry.grid(row=0, column=0, columnspan=3, ipady=2, pady=2)


def myclick(number):
	entry.insert(tk.END, number)


def equal():
	try:
		y = str(eval(entry.get()))
		entry.delete(0, tk.END)
		entry.insert(0, y)
	except:
		tkinter.messagebox.showinfo("Error", "Syntax Error")


def clear():
	entry.delete(0, tk.END)


btn_1 = tk.Button(master=frame, text='1', padx=15,pady=5, width=3, command=lambda: myclick(1))
btn_1.grid(row=1, column=0, pady=2)

btn_2 = tk.Button(master=frame, text='2', padx=15,pady=5, width=3, command=lambda: myclick(2))
btn_2.grid(row=1, column=1, pady=2)

btn_3 = tk.Button(master=frame, text='3', padx=15,pady=5, width=3, command=lambda: myclick(3))
btn_3.grid(row=1, column=2, pady=2)

btn_4 = tk.Button(master=frame, text='4', padx=15,pady=5, width=3, command=lambda: myclick(4))
btn_4.grid(row=2, column=0, pady=2)

btn_5 = tk.Button(master=frame, text='5', padx=15,pady=5, width=3, command=lambda: myclick(5))
btn_5.grid(row=2, column=1, pady=2)

btn_6 = tk.Button(master=frame, text='6', padx=15,pady=5, width=3, command=lambda: myclick(6))
btn_6.grid(row=2, column=2, pady=2)

btn_7 = tk.Button(master=frame, text='7', padx=15,pady=5, width=3, command=lambda: myclick(7))
btn_7.grid(row=3, column=0, pady=2)

btn_8 = tk.Button(master=frame, text='8', padx=15,pady=5, width=3, command=lambda: myclick(8))
btn_8.grid(row=3, column=1, pady=2)

btn_9 = tk.Button(master=frame, text='9', padx=15,pady=5, width=3, command=lambda: myclick(9))
btn_9.grid(row=3, column=2, pady=2)

btn_0 = tk.Button(master=frame, text='0', padx=15,pady=5, width=3, command=lambda: myclick(0))
btn_0.grid(row=4, column=1, pady=2)

btn_add = tk.Button(master=frame, text="+", padx=15,pady=5, width=3, command=lambda: myclick('+'))
btn_add.grid(row=5, column=0, pady=2)

btn_sub = tk.Button(master=frame, text="-", padx=15, pady=5, width=3, command=lambda: myclick('-'))
btn_sub.grid(row=5, column=1, pady=2)

btn_multi = tk.Button(master=frame, text="*", padx=15, pady=5, width=3, command=lambda: myclick('*'))
btn_multi.grid(row=5, column=2, pady=2)

btn_div = tk.Button(master=frame, text="/", padx=15,pady=5, width=3, command=lambda: myclick('/'))
btn_div.grid(row=6, column=0, pady=2)

btn_clear = tk.Button(master=frame, text="clear",padx=15, pady=5, width=12, command=clear)
btn_clear.grid(row=6, column=1, columnspan=2, pady=2)

btn_equal = tk.Button(master=frame, text="=", padx=15,pady=5, width=9, command=equal)
btn_equal.grid(row=7, column=0, columnspan=3, pady=2)

window.mainloop()
