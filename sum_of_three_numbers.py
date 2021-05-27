from tkinter import *


# Function
def add_func():
    num1 = text_lbl1.get()
    num2 = text_lbl2.get()
    num3 = text_lbl3.get()

    result = float(num1) + float(num2) + float(num3)
    text_lbl_result.insert(0, result)


# GUI
root = Tk()
root.title("Sum of three numbers")
root.geometry("360x340")
root.resizable(0, 0)
root.config(bg="black")

lbl1 = Label(root, text="First Number", bg="grey")
lbl1.place(x=10, y=10, width=100, height=40)

text_lbl1 = Entry(root)
text_lbl1.place(x=130, y=10, width=100, height=40)

lbl2 = Label(root, text="Second Number", bg="grey")
lbl2.place(x=10, y=60 + 14, width=100, height=40)

text_lbl2 = Entry(root)
text_lbl2.place(x=130, y=60 + 14, width=100, height=40)

btn_add = Button(root, text="ADD", command=add_func) # single button
btn_add.place(x=130 + 120, y=60 + 14, width=100, height=40)

lbl3 = Label(root, text="Third Number", bg="grey")
lbl3.place(x=10, y=110 + 14 * 2, width=100, height=40)

text_lbl3 = Entry(root)
text_lbl3.place(x=130, y=110 + 14 * 2, width=100, height=40)

lbl_result = Label(root, text="Result", bg="grey")
lbl_result.place(x=10, y=2 * (110 + 14 * 2), width=100, height=40)

text_lbl_result = Entry(root, bg="aqua")
text_lbl_result.place(x=130, y=2 * (110 + 14 * 2), width=100, height=40)

# start
root.mainloop()
