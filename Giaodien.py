import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import numpy as np
import matplotlib.pyplot as plt

import cv2, os

window = tk.Tk()
window.geometry("1280x720")
frame1 = tk.Frame(window, bg="White")
frame1.place(relx=0.40, rely=0.15, relwidth=0.55, relheight=0.70)
title1 = tk.Label(window, text=" Image ", fg="Black", bg="#a8daed", width=5, heigh=1, font=('Times New Roman', 30,))
title1.place(x=800, y=600)


##### NÚT Nhấn
def show_dialog(message):
    dialog = tk.Toplevel(window)
    dialog.geometry("200x100")
    label = tk.Label(dialog, text=message)
    label.pack()
    ok_button = tk.Button(dialog, text="OK", command=dialog.destroy)
    ok_button.pack()


def Chon():
    file_path = "1.jpg"  # Path to the image file

    if file_path:
        image = Image.open(file_path)
        image = image.resize((int(frame1.winfo_width()), int(frame1.winfo_height())))
        img = ImageTk.PhotoImage(image)
        label = ttk.Label(frame1, image=img)
        label.image = img
        label.pack()


def His():
    file_path = "1.jpg"  # Path to the image file

    if file_path:
        image = Image.open(file_path)
        image = image.convert("L")  # Convert image to grayscale

        # Calculate the histogram
        histogram = np.histogram(image, bins=256, range=[0, 256])

        # Plot the histogram
        plt.figure()
        plt.title("Histogram")
        plt.xlabel("Pixel Value")
        plt.ylabel("Frequency")
        plt.plot(histogram[1][:-1], histogram[0], color='black')

        # Convert the plot to a Tkinter-compatible image
        fig = plt.gcf()
        fig.canvas.draw()
        plot_img = ImageTk.PhotoImage(Image.frombytes('RGB', fig.canvas.get_width_height(), fig.canvas.tostring_rgba()))

        # Display the histogram on frame1
        label = ttk.Label(frame1, image=plot_img)
        label.image = plot_img
        label.pack()


chonanh = tk.Button(window, text="Nhập ảnh ", command=Chon, fg="Black", bg="#72bdf7", width=35, height=1,
                    activebackground="white", font=('times', 15, ' bold '))
chonanh.place(x=50, y=200)
histogram = tk.Button(window, text="Histogram", command=His, fg="Black", bg="#72bdf7", width=35, height=1,
                      activebackground="white", font=('times', 15, ' bold '))
histogram.place(x=50, y=300)
quitWindow = tk.Button(window, text="Thoát", command=window.destroy, fg="black", bg="red", width=15, height=1,
                       activebackground="white", font=('times', 15, ' bold '))
quitWindow.place(x=50, y=550)

window.mainloop()
