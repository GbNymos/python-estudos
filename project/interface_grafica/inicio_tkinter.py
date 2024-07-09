from tkinter import *

app=Tk()
app.title("Hello world")
app.geometry("700x500")
app.configure(background="#4BE5EB",cursor="hand2")

txt1=Label(app,text="Bem_vindo ao programa",bg="#4BEBBA",fg="#000")
txt1.place(x=10,y=20,width=200,height=30)

txt2=Label(app,bg="#265E27")
txt2.pack(ipadx=20,ipady=20,padx=10,pady=10,side="bottom",fill=X,expand=True)




app.mainloop()