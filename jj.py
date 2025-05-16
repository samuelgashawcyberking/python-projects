from tkinter import *
root = Tk()

# title on the head of gui
root.title('Registration Form')

#size of  gui
root.geometry("600x470")
root.resizable(False,False)
#def on the button to wirte on the note pad

def btnR ():
    name_info = namevalue.get()
    phone_info= phonevalue.get()
    email_info= emailvalue.get()
    file=open(name_info + '.txt','w')
    file.write(name_info +"\n")
    file.write(phone_info + "\n")
    file.write(email_info + "\n")
    file.close()
    name_entry.delete(0,END)
    email_entry.delete(0,END)
    phone_entry.delete(0,END)
    Label(text="Registration sucess", fg='green', font=('calibri',11 )).place(x=250,y=430)





#header for the gui
h1=Label(root, text='Registration info',font='arial 25', fg='gray').pack(pady=50)

# registration info guide like (name ,phone etc...)
name=Label(text='Name', font= 26, fg='#556B2F').place(x=100,y=150)
phone=Label(text='Phone number', font= 26, fg='#556B2F').place(x=100,y=200)
email=Label(text='Email', font= 26, fg='#556B2F').place(x=100,y=250)

#entry
namevalue=StringVar()
phonevalue=StringVar()
emailvalue=StringVar()

name_entry=Entry(root,textvariable=namevalue ,width=35,bd=3,font=21)
phone_entry=Entry(root,textvariable=phonevalue ,width=35,bd=3,font=21)
email_entry=Entry(root,textvariable=emailvalue,width=35,bd=3,font=21)

#entry place
name_entry.place(x=210,y=150)
phone_entry.place(x=210,y=200)
email_entry.place(x=210,y=250)

# cheek box
checkvalue=IntVar()
checkbtn=Checkbutton(text="Remamber me",fg='#556B2F' , variable=checkvalue)
checkbtn.place(x=200, y=340)
# registration button
regsterbtn=Button(text='register', fg='#556B2F', font=20, width=10,height=2, command=btnR)
regsterbtn.place(x=250,y=380)


root.mainloop()
