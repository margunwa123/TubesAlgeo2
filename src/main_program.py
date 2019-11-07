import tkinter as tk
from tkinter import *
from tkinter.ttk import Frame, Button, Label, Style
from tkinter import filedialog, Text, BOTH, W, N, E, S
from PIL import Image, ImageTk
import cv2
import similarity
import extract
import img


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
        self.Euclidean.grid(row=1,column=3, pady = 10)
        self.Cosine = tk.Button(self)
        self.Cosine["text"] = "Cosine"
        self.Cosine["bd"] =3
        self.Cosine["command"] = self.Cosdist #match_cosine(self.openFile())
        self.Cosine.grid(row=2,column = 3)
        self.find = tk.Button(self)
        #Membuat Label Bawah
        self.label = tk.Label(self)
        self.label.grid(sticky=W, pady=4, padx=5)
        #Button untuk isian label bawah
        self.quit = tk.Button(self, text="QUIT", fg="red",
                             command=self.master.destroy)
        self.quit.grid(column =3, row=5, padx=5)
        #Tampilan awal foto
        self.image = Image.open("..\\doc\\tubesalgeo.jpg")
        self.image = self.image.resize((267,265), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.image)
        self.area.create_image(1,0, image = self.img, anchor=NW)
        
    def match_cosine(self,path):
        paths = extract.closest_match_cosine(path,5)
        
        cv2.waitKey()
    def match_euc(self,path):
        paths = extract.closest_match_euc(path,5)
        
        cv2.waitKey()


    def Eucdist(self):
        self.getImgOpen('Ecu')
        self.prev = tk.Button(self, text="Prev", bd =3)
        self.prev.grid(column =0, row=5, padx = 15)
        self.prev["command"] =lambda : self.getImgOpen('prev')
        self.next = tk.Button(self, text = "Next", bd = 3)
        self.next["command"] =lambda : self.getImgOpen('next')
        self.next.place(x=70,y=268)
        self.matcher = tk.Button(self,text = "Matcher :", bg ="blue", fg ="white", bd = 3)
        self.matcher["command"] =lambda : self.getImgOpen('next')
        self.matcher.grid(row = 5, column = 1)
    

    def Cosdist(self):
        self.getImgOpen('Cos')
        self.prev = tk.Button(self, text="Prev", bd =3)
        self.prev.grid(column =0, row=5, padx = 15)
        self.prev["command"] =lambda : self.getImgOpen('prev')
        self.next = tk.Button(self, text = "Next", bd = 3)
        self.next["command"] =lambda : self.getImgOpen('next')
        self.next.place(x=70,y=270)
        self.matcher = tk.Button(self,text = "Matcher :", bg ="blue", fg ="white", bd = 3)
        self.matcher["command"] =lambda : self.getImgOpen('next')
        self.matcher.grid(row = 5, column = 1)
    
    def getImgOpen(self,seq):
        #self.paths = extract.closest_match_cosine(self.filename,5)
        if seq=='Ecu':
            self.filename = filedialog.askopenfilename(initialdir= "/", title= "Select Picture", filetype = (("jpeg", "*.jpg"), ("All File", "*,*")))
            self.paths = extract.closest_match_euc(self.filename,5)
            print(self.paths)
            self.imgIndex = -1
        elif seq=='Cos':
            self.filename = filedialog.askopenfilename(initialdir= "/", title= "Select Picture", filetype = (("jpeg", "*.jpg"), ("All File", "*,*")))
            self.paths = extract.closest_match_cosine(self.filename,5)
            print(self.paths)
            self.imgIndex = -1
        elif (seq == 'prev'):
            if (self.imgIndex > 0):
                self.imgIndex -= 1
        elif(seq == 'next'):
            if(self.imgIndex < 4):
                self.imgIndex += 1
        if(self.imgIndex == 0):
            self.lbl = tk.Label(self,text = "  Match 1  ", bg = "red")
            self.lbl.grid(row = 5, column = 1)
        elif(self.imgIndex == 1):
            self.lbl = tk.Label(self,text = "  Match 2  ", bg = "orange red")
            self.lbl.grid(row = 5, column = 1)
        elif(self.imgIndex == 2):
            self.lbl = tk.Label(self,text = "  Match 3  ", bg = "orange")
            self.lbl.grid(row = 5, column = 1)
        elif(self.imgIndex == 3):
            self.lbl = tk.Label(self,text = "  Match 4  ", bg = "yellow" )
            self.lbl.grid(row = 5, column = 1)
        elif(self.imgIndex == 4):
            self.lbl = tk.Label(self,text = "  Match 5  ", bg = "green2")
            self.lbl.grid(row = 5, column = 1)
        if(self.imgIndex != -1):
            print(self.imgIndex)
            self.image = Image.open(self.paths[self.imgIndex][0])
            self.image = self.image.resize((267,265), Image.ANTIALIAS)
            self.img = ImageTk.PhotoImage(self.image)
            self.area.create_image(1,0, image = self.img, anchor=NW)
        elif(self.imgIndex == -1):
            self.image = Image.open(self.filename)
            self.image = self.image.resize((267,265), Image.ANTIALIAS)
            self.img = ImageTk.PhotoImage(self.image)
            self.area.create_image(1,0, image = self.img, anchor=NW)
        

root = tk.Tk()
root.geometry("350x300+300+300")
app = Application(master=root)
app.mainloop()
