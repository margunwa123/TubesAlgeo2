import tkinter as tk
from tkinter import *
from tkinter.ttk import Frame, Button, Label, Style
from tkinter import filedialog, Text, BOTH, W, N, E, S
from PIL import Image, ImageTk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.create_widgets()
        self.databaseFoto()
        self.place()
       # self.openImage()
    def create_widgets(self):
        #Konfigurasi frame
        self.master.title("FACE RECOGNITZON")
        self.pack(fill=BOTH, expand=True)
        #Konfigurasi label untuk background 
        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        self.rowconfigure(3,weight=1)
        self.rowconfigure(5, pad=7)
        #konfigurasi area untuk meletakan foto
        self.area = tk.Canvas(self, bg = "red")
        self.area.grid(row=1, column=0, columnspan=2, rowspan=4, padx=5, sticky = E+W+S+N)
        #Konfigurasi Button
        self.Ecluidean = tk.Button(self,text = "Ecluidean")
        self.Ecluidean["bd"] =3
        self.Ecluidean["command"] = self.say_hi
        self.Ecluidean.grid(row=2,column=3)
        self.Cosine = tk.Button(self)
        self.Cosine["text"] = "Cosine"
        self.Cosine["bd"] =3
        self.Cosine["command"] = self.say_hi
        self.Cosine.place(x=285,y=85)
        self.find = tk.Button(self)
        self.find["text"] = ("Find File")
        self.find["command"] = self.openFile
        self.find.grid(row=1, column=3, pady = 10)
        #Membuat Label Bawah
        self.label = tk.Label(self)
        self.label.grid(sticky=W, pady=4, padx=5)
        #Button untuk isian label bawah
        self.quit = tk.Button(self, text="QUIT", fg="red",
                             command=self.master.destroy)
        self.quit.grid(column =3, row=5, padx=5)

        
     
    def openFile(self):
        self.area = tk.Canvas(self, bg = "blue")
        self.area.grid(row=1, column=0, columnspan=2, rowspan=4, padx=5, sticky = E+W+S+N)
        self.filename = filedialog.askopenfilename(initialdir= "/", title= "Select Picture", filetype = (("jpeg", "*.jpg"), ("All File", "*,*")))
        self.image = Image.open(self.filename)
        self.image = self.image.resize((267,265), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.image)
        self.area.create_image(1,0, image = self.img, anchor=NW)
        print(self.filename)
    def databaseFoto(self):
        self.next = tk.Button(self, text="Next", bd =3)
        self.next.grid(column =0, row=5, padx = 15)
        self.prev = tk.Button(self, text = "Prev", bd = 3)
        self.prve = 0
        print(self.prev)
        self.prev.place(x=70,y=268)
    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
root.geometry("350x300+300+300")
app = Application(master=root)
app.mainloop()