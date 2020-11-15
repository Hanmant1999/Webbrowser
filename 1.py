from tkinter import *
import webbrowser
b=webbrowser.get()
root=Tk()
root.title("Web Browser")
root.geometry("500x300")
root.configure(bg="#eedad1")
har=Label(root,text="Harry's Browser",fg="#3aa1d8")
har.place(x=125,y=5)
mylabel2=Label(root,text="Search Here")
mylabel2.place(x=10,y=40)
e=Entry(root,width=15)
e.place(x=150,y=40,width=200)
def cric():
 b.open("https://www.cricbuzz.com/")
def amaz():
 b.open("https://www.amazon.in")
def search():
 website=e.get()
 if website.startswith("https://"):
  b.open(website)
 else:
  b.open("https://www.google.com/search?q="+website)
 e.delete(0,END)
mybutton3=Button(root,text="Search",fg="black",bg="green",command=search)
mybutton3.place(x=125,y=70)
mylabel=Label(root,text="Your Website Options:")
mylabel.place(x=30,y=130)
#photo=PhotoImage(file=r"/hanmant/Downloads")
mybutton=Button(root,text="Cricbuzz",fg="black",bg="blue",padx=20,pady=20,command=cric)
mybutton1=Button(root,text="Amazon",fg="black",bg="yellow",padx=20,pady=20,command=amaz)
mybutton.place(x=10,y=180)
mybutton1.place(x=200,y=180)
mybutton4=Button(root,text="Exit",padx=2,pady=2,fg="black",bg="green",command=root.quit)
mybutton4.place(x=120,y=270)

root.mainloop()
