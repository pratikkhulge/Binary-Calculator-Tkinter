import tkinter as tk
import math


def clear_display(curr_input, curr_display):
	curr_input.delete(0, tk.END)
	curr_display.set('')
	return


def process_input(curr_input, curr_display):
	ans = math.ceil(eval(curr_input.get()))
	binary_ans = str('{0:b}'.format(ans))
	curr_display.set(binary_ans)
	return


def insert_btn_value(curr_input, numb):
	curr_input.insert(tk.END, numb)
	return


window = tk.Tk()
window.title("Binary Calculator")

content = tk.Frame(master=window,padx=10,pady=10,relief=tk.RAISED,borderwidth=4)
window.geometry("220x345+0+0")
window.resizable(0, 0)
content.grid(row=0, column=0)
content.pack(fill = 'both', expand = True,padx = 10, pady = 10)

label = tk.Label(master=content, borderwidth=1, text='Binary Calculator',font=('Helvetica', '13'))
label.grid(row=0, column=0, columnspan=4)

###########
## operands
###########
frame = tk.Frame(master=content, relief=tk.RAISED, borderwidth=2)
frame.grid(row=2, column=0)
btn = tk.Button(master=frame, text='1',width=4,height=2, command=lambda: insert_btn_value(user_input, 1))
btn.pack()

frame = tk.Frame(master=content, relief=tk.RAISED, borderwidth=2)
frame.grid(row=2, column=1)
btn = tk.Button(master=frame, text='2',width=4,height=2, command=lambda: insert_btn_value(user_input, 2))
btn.pack()

frame = tk.Frame(master=content, relief=tk.RAISED, borderwidth=2)
frame.grid(row=2, column=2)
btn = tk.Button(master=frame, text='3',width=4,height=2, command=lambda: insert_btn_value(user_input, 3))
btn.pack()

frame = tk.Frame(master=content, relief=tk.RAISED, borderwidth=2)
frame.grid(row=3, column=0)
btn = tk.Button(master=frame, text='4',width=4,height=2, command=lambda: insert_btn_value(user_input, 4))
btn.pack()

frame = tk.Frame(master=content, relief=tk.RAISED, borderwidth=2)
frame.grid(row=3, column=1)
btn = tk.Button(master=frame, text='5',width=4,height=2, command=lambda: insert_btn_value(user_input, 5))
btn.pack()

frame = tk.Frame(master=content, relief=tk.RAISED, borderwidth=2)
frame.grid(row=3, column=2)
btn = tk.Button(master=frame, text='6',width=4,height=2, command=lambda: insert_btn_value(user_input, 6))
btn.pack()

frame = tk.Frame(master=content, relief=tk.RAISED, borderwidth=2)
frame.grid(row=4, column=0)
btn = tk.Button(master=frame, text='7',width=4,height=2, command=lambda: insert_btn_value(user_input, 7))
btn.pack()

frame = tk.Frame(master=content, relief=tk.RAISED, borderwidth=2)
frame.grid(row=4, column=1)
btn = tk.Button(master=frame, text='8',width=4,height=2, command=lambda: insert_btn_value(user_input, 8))
btn.pack()

frame = tk.Frame(master=content, relief=tk.RAISED, borderwidth=2)
frame.grid(row=4, column=2)
btn = tk.Button(master=frame, text='9',width=4,height=2, command=lambda: insert_btn_value(user_input, 9))
btn.pack()

frame = tk.Frame(master=content, relief=tk.RAISED, borderwidth=2)
frame.grid(row=5, column=1)
btn = tk.Button(master=frame, text='0',width=4,height=2, command=lambda: insert_btn_value(user_input, 0))
btn.pack()


############
## operators
############
frame = tk.Frame(master=content,relief=tk.RAISED, borderwidth=2)
frame.grid(row=2, column=3)
btn = tk.Button(master=frame, text='+',width=4,height=2, command=lambda: insert_btn_value(user_input, '+'))
btn.pack()

frame = tk.Frame(master=content,relief=tk.RAISED, borderwidth=2)
frame.grid(row=3, column=3)
btn = tk.Button(master=frame, text='-',width=4,height=2, command=lambda: insert_btn_value(user_input, '-'))
btn.pack()

frame = tk.Frame(master=content,relief=tk.RAISED, borderwidth=2)
frame.grid(row=4, column=3)
btn = tk.Button(master=frame, text='*',width=4,height=2, command=lambda: insert_btn_value(user_input, '*'))
btn.pack()

frame = tk.Frame(master=content,relief=tk.RAISED, borderwidth=2)
frame.grid(row=5, column=3)
btn = tk.Button(master=frame, text='/',width=4,height=2, command=lambda: insert_btn_value(user_input, '/'))
btn.pack()


frame = tk.Frame(master=content,relief=tk.RAISED, borderwidth=2)
frame.grid(row=5, column=2)
btn = tk.Button(master=frame, text='=',width=4,height=2, command=lambda: process_input(user_input, user_display))
btn.pack()

frame = tk.Frame(master=content,relief=tk.RAISED, borderwidth=2)
frame.grid(row=5, column=0)
btn = tk.Button(master=frame, text='C',width=4,height=2, command=lambda: clear_display(user_input, user_display))
btn.pack()


frame = tk.Frame(master=content,relief=tk.SOLID,borderwidth=2)
frame.grid(row=1, column=0, columnspan=4,pady=10)
user_input = tk.Entry(master=frame,width=20)
user_input.pack()

frame = tk.Frame(master=content,relief=tk.SOLID,borderwidth=2)
frame.grid(row=6, column=0, columnspan=4,pady=10)
user_display = tk.StringVar()
label = tk.Label(master=frame, textvariable=user_display,width=20)
label.pack()

window.mainloop()