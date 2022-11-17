# Importing the Required Libraries
import random
import string
from tkinter import Tk, Label, Entry, Button, Text, Label, END
from PIL import ImageTk, Image
from captcha.image import ImageCaptcha

total = 10
correct = 0
nums = range(1, 11)


def calc(a, ops, b):
    """Returns integer operation result from using : 'a','ops','b'"""
    if ops == "+":
        return a+b
    elif ops == "-":
        return a-b
    elif ops == "*":
        return a*b
    elif ops == "/":
        return a//b   # integer division
    else:
        raise ValueError("Unsupported math operation")


def createImage(flag=0):
    """
    Defining the method createImage() which will create
    and generate a Captcha Image based on a randomly
    generated strings. The Captcha Image generated is then
    incorporated into the GUI window we have designed.
    """
    global math_random
    global image_label
    global image_display
    global entry
    global verify_label
    global answer
    ops = random.choice("+-*/")
    a, b = random.choices(nums, k=2)
    answer = calc(a, ops, b)
    math_random = str(a)+str(ops)+str(b)
    # The if block below works only when we press the
    # Reload Button in the GUI. It basically removes
    # the label (if visible) which shows whether the
    # entered string is correct or incorrect.
    if flag == 1:
        verify_label.grid_forget()
    # Removing the contents of the input box.
    entry.delete(0, END)
    # Generating a random string for the Captcha

    # Create label
    l = Label(root, text=math_random)
    l.config(font=("Courier", 14))
    l.grid(row=1, column=0, columnspan=2, pady=0)


def check(x, y):
    """
    Defining the method check() which will check
    whether the string entered by the user matches
    with the randomly generated string. If there is
    a match then "Verified" pops up in the window.
    Otherwise, "Incorrect!" pops up and a new Captcha
    Image is generated for the user to try again.
    """
    # Making the scope of the below mentioned
    # variables because their values are accessed
    # globally in this script.
    global verify_label
    verify_label.grid_forget()
    if x == y:
        verify_label = Label(master=root,
                             text="Verified",
                             font="Arial 15",
                             bg='#ffe75c',
                             fg="#00a806"
                             )
        verify_label.grid(row=0, column=0, columnspan=2, pady=10)
    else:
        verify_label = Label(master=root,
                             text="Incorrect!",
                             font="Arial 15",
                             bg='#ffe75c',
                             fg="#fa0800"
                             )
        verify_label.grid(row=0, column=0, columnspan=2, pady=10)
        createImage()


if __name__ == "__main__":
    # Initializing Tkinter by creating a root widget,
    # setting Title and Background Color
    root = Tk()
    root.title('Image Captcha')
    root.configure(background='#fff')
    # Initializing the Variables to be defined later
    verify_label = Label(root)
    image_label = Label(root)
    # Defining the Input Box and placing it in the window
    entry = Entry(root, width=10, borderwidth=5,
                  font="Arial 15", justify="center")
    entry.grid(row=2, column=0)
    # Creating an Image for the first time.
    createImage()
    # Defining the path for the reload button image
    # and using it to add the reload button in the
    # GUI window
    path = './refresh.png'
    reload_img = ImageTk.PhotoImage(Image.open(
        path).resize((32, 32), Image.Resampling.LANCZOS))
    reload_button = Button(image=reload_img, command=lambda: createImage(1))
    reload_button.grid(row=2, column=1, pady=10)
    # Defining the submit button
    submit_button = Button(root, text="Submit", font="Arial 10",
                           command=lambda: check(int(entry.get()), answer))
    submit_button.grid(row=3, column=0, columnspan=2, pady=10)
    root.bind('<Return>', func=lambda Event: check(int(entry.get()), answer))
    # This makes the program loops till the user
    # doesn't close the GUI window
    root.mainloop()
