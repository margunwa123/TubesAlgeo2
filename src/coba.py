import tkinter as tk
from tkinter import *
from tkinter.ttk import Frame, Button, Label, Style
from tkinter import filedialog, Text, BOTH, W, N, E, S
from PIL import Image, ImageTk
import cv2
import similarity
import extract
import img
import facerecog as fr


class Application(tk.Frame):
    global pathcos
    global patheuc
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.create_widgets()
        #self.databaseFoto()
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
        self.Euclidean = tk.Button(self,text = "Euclidean")
        self.Euclidean["bd"] =3
        self.Euclidean["command"] = self.Eucdist
        self.Euclidean.grid(row=2,column=3)
        self.Cosine = tk.Button(self)
        self.Cosine["text"] = "Cosine"
        self.Cosine["bd"] =3
        self.Cosine["command"] = self.Cosdist #match_cosine(self.openFile())
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

        
    def match_cosine(self,path):
        paths = extract.closest_match_cosine(path,5)
        
        cv2.waitKey()
    def match_euc(self,path):
        paths = extract.closest_match_euc(path,5)
        
        cv2.waitKey()


    def Eucdist(self):
        self.area = tk.Canvas(self, bg = "blue")
        self.area.grid(row=1, column=0, columnspan=2, rowspan=4, padx=5, sticky = E+W+S+N)
        self.filename = filedialog.askopenfilename(initialdir= "/", title= "Select Picture", filetype = (("jpeg", "*.jpg"), ("All File", "*,*")))
        self.image = Image.open(self.filename)
        self.image = self.image.resize((267,265), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.image)
        self.area.create_image(1,0, image = self.img, anchor=NW)
        self.match_euc(self.filename)

    def Cosdist(self):
        self.area = tk.Canvas(self, bg = "blue")
        self.area.grid(row=1, column=0, columnspan=2, rowspan=4, padx=5, sticky = E+W+S+N)
        self.filename = filedialog.askopenfilename(initialdir= "/", title= "Select Picture", filetype = (("jpeg", "*.jpg"), ("All File", "*,*")))
        self.image = Image.open(self.filename)
        self.image = self.image.resize((267,265), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.image)
        self.area.create_image(1,0, image = self.img, anchor=NW)
        paths = extract.closest_match_cosine(self.filename,5)
        files = []
        for j in paths:
            files.append(j[0])
            #berarti semua filename di paths dimasukin ke array files
        self.next = tk.Button(self, text="Next", bd =3)
        self.next.grid(column =0, row=5, padx = 15)
        self.next["command"] =lambda : self.getImgOpen('next')
        self.prev = tk.Button(self, text = "Prev", bd = 3)
        self.prev = 0
        self.prev["command"] =lambda : self.getImgOpen('prev')
        self.prev.place(x=70,y=268)
    
    def getImgOpen(self,seq):
        print ('Opening %s' % seq)
        if seq=='ZERO':
            self.imgIndex = 0
        elif (seq == 'prev'):
            if (self.imgIndex == 0):
                self.imgIndex = len(self.images)-1
            else:
                self.imgIndex -= 1
        elif(seq == 'next'):
            if(self.imgIndex == len(self.images)-1):
                self.imgIndex = 0
            else:
                self.imgIndex += 1
        self.masterImg = Image.open(self.images[self.imgIndex]) 
        self.master.title(self.images[self.imgIndex])
        self.masterImg.thumbnail((400,400))
        self.img = ImageTk.PhotoImage(self.masterImg)
        self.lbl['image'] = self.img
        return
    
    def openFile(self):
        self.area = tk.Canvas(self, bg = "blue")
        self.area.grid(row=1, column=0, columnspan=2, rowspan=4, padx=5, sticky = E+W+S+N)
        self.filename = filedialog.askopenfilename(initialdir= "/", title= "Select Picture", filetype = (("jpeg", "*.jpg"), ("All File", "*,*")))
        self.image = Image.open(self.filename)
        self.image = self.image.resize((267,265), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.image)
        self.area.create_image(1,0, image = self.img, anchor=NW)
    
    def openimg(self,path):
        self.image = Image.open(path)
        self.image = self.image.resize((267,265), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.image)
        self.area.create_image(1,0, image = self.img, anchor=NW)
    """
    def databaseFoto(self):
        self.next = tk.Button(self, text="Next", bd =3)
        self.next.grid(column =0, row=5, padx = 15)
        self.next["command"] = self.openimg()
        self.prev = tk.Button(self, text = "Prev", bd = 3)
        self.prev = 0
        self.prev.place(x=70,y=268)
    """
    def say_hi(self):
        print("hi there, everyone!")


root = tk.Tk()
root.geometry("350x300+300+300")
app = Application(master=root)
app.mainloop()