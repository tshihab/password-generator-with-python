# importing modules
from tkinter import *
import random, string, pyperclip

# creating window
root = Tk()
root.geometry("500x350")
root.resizable(0, 0)
root.title("Password Generator")
root.configure(bg='thistle')


# creating functions
def Generator():
    # initialize a variable to add characters one by one
    password = ''
    for i in range(pass_len.get()):
        password = password + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
        # choose only one elements among these four random choice and take until the length

    pass_str.set(password)


def Copy():
    pyperclip.copy(pass_str.get())



# creating Labels
head_label = Label(root, text="Generate The Strongest Password For Social Your Account", font='Times 15 bold', bg='thistle', fg='darkviolet').pack(pady=10)
pass_label = Label(root, text='Select Your Password Length', font='Times 15', bg='thistle', fg='blueviolet').pack(pady=15)
pass_len = IntVar()
length = Spinbox(root, from_=8, to_=32, font='times 15', width=10, textvariable=pass_len).pack()

# generator button
gen_button = Button(root, text='Generate Password', font='Veranda 12', width=16, bg='midnightblue', fg='slateblue', command=Generator).pack(pady=10)

# creating an extra label to get some space
Label(root, bg='thistle').pack(pady=5)

pass_label2 = Label(root, text='Your Password', font='Times 15', bg='thistle', fg='blueviolet').pack()

# creating a string variable to show in the entry label
pass_str = StringVar()
pass_label3 = Entry(root, textvariable=pass_str, font='Helvetica 15', width=35).pack()

# copy button
cpy_button = Button(root, text='Copy To Clipboard', state='normal', font='Times 15', width=15, command=Copy).pack(pady=15)


root.mainloop()
