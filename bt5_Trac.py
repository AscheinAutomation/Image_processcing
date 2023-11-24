from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import cv2

top = Tk()
top.title('Võ Ngọc Trác')
top.geometry('900x600')
top['bg'] = '#CCFFFF'

name = Label(top, text='Bài 5', font=('sans-serif', 18, 'bold'), bg='yellow', fg='red')
name.place(x=450, y=0)


def anvao():
    global image, img
    path = filedialog.askopenfilename()
    if path:
        image = cv2.imread(path)
        img = cv2.resize(image, (250, 250))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        img = ImageTk.PhotoImage(img)
        label = Label(top, image=img)
        label.place(x=200, y=60)
        x = Label(top, text='Ảnh gốc', font=('sans-serif', 14), bg='yellow', fg='black')
        x.place(x=300, y=30)


def his():
    global img
    if image is not None:
        img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        img = cv2.equalizeHist(img)
        img = cv2.resize(img, (250, 250))
        img = Image.fromarray(img)
        img = ImageTk.PhotoImage(img)
        label = Label(top, image=img)
        label.place(x=500, y=60)
        x1 = Label(top, text='equali_histogram', font=('sans-serif', 14), bg='yellow', fg='black')
        x1.place(x=550, y=30)


def loc_trung_vi():
    global img
    if 'image' in globals():
        img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        img = cv2.medianBlur(img, 5)
        img = cv2.resize(img, (250, 250))
        img = Image.fromarray(img)
        img = ImageTk.PhotoImage(img)
        label = Label(top, image=img)
        label.place(x=200, y=350)
        x1 = Label(top, text='Loc_tv', font=('sans-serif', 14), bg='yellow', fg='black')
        x1.place(x=280, y=330)


def loc_trung_binh():
    global img
    if 'image' in globals():
        img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        img = cv2.blur(img, (5, 5))
        img = cv2.resize(img, (250, 250))
        img = Image.fromarray(img)
        img = ImageTk.PhotoImage(img)
        label = Label(top, image=img)
        label.place(x=500, y=350)
        x1 = Label(top, text='Loc_tb', font=('sans-serif', 14), bg='yellow', fg='black')
        x1.place(x=600, y=330)


def tach_bien():
    global img
    if 'image' in globals():
        img = cv2.resize(image, (250, 250))
        img = cv2.Canny(img, 10, 250, apertureSize=3, L2gradient=True)
        img = Image.fromarray(img)
        img = ImageTk.PhotoImage(img)
        label = Label(top, image=img)
        label.place(x=400, y=200)
        x1 = Label(top, text='Tach_bien', font=('sans-serif', 14), bg='yellow', fg='black')
        x1.place(x=450, y=200)


but = Button(top, text='Mở file', width=12, height=1, bg='yellow', font=('Arial', 13), fg='blue', command=anvao)
but.place(x=5, y=50)

but = Button(top, text='Histogram', width=12, height=1, bg='yellow', font=('Arial', 13), fg='blue', command=his)
but.place(x=5, y=100)

but = Button(top, text='Lọc Trung Vị', width=12, height=1, bg='yellow', font=('Arial', 13), fg='blue',
             command=loc_trung_vi)
but.place(x=5, y=150)

but = Button(top, text='Lọc Trung Bình', width=12, height=1, bg='yellow', font=('Arial', 13), fg='blue',
             command=loc_trung_binh)
but.place(x=5, y=200)

but = Button(top, text='Tách Biên ', width=12, height=1, bg='yellow', font=('Arial', 13), fg='blue', command=tach_bien)
but.place(x=5, y=250)

but = Button(top, text='Off ', width=12, height=1, bg='yellow', font=('Arial', 13), fg='blue', command=exit)
but.place(x=5, y=300)
top.mainloop()
