"""
0-600*0%
601--1650*10%-60
1651--3200*15%-142.5
3201--5250*20%-302.5
5251--7800*25%-565
7801--10900*30%-955
over10900*35-1500
basic salary*rate-dedaction


"""
import tkinter
from tkinter import messagebox
import openpyxl    # library that help as to save our file on xl
from openpyxl import load_workbook   # library that help as to save our file on xl
root=tkinter.Tk()
file2_path=r'C:\Users\gasha\OneDrive\Desktop\samuel.xlsx'
T=openpyxl.load_workbook(file2_path)
T2=T['tax']



def btn3f():
    name = name_entry.get()
    phone = phone_entry.get()
    money = money_entry.get()
    position = position_entry.get()
    tax = tax_entry.get()
    if name and phone and money and position and tax:
        T2.append([name,phone,money,position,tax])
        T.save(file2_path)

def btn1f():
        #formula to calculate tax
    income =int(money_entry.get())
    if income <= 600:
        eit = 0


    elif 601 < income <= 1650:
        # eit=employ income tax
        eit = (income* 0.1 - 60)
    elif 1651 < income<= 3200:
        eit = (income * 0.15 - 142.5)
    elif 3201 < income <= 5250:
        eit = (income * 0.2 - 302.5)
    elif 5250 < income <= 7800:
        eit = (income * 0.25 - 565)
    elif 7801 < income <= 10900:
        eit = (income * 0.3 - 955)
    elif income >= 10901:
        eit = (income * 0.35 - 1500)
    tax_entry.insert(0,f'{eit}')
    tax_entry.config(state=tkinter.DISABLED)




    #result_label.config(text=f'{eit}', font=23, bg='#99cfe0', fg='green')




def btn2f ():
    name_entry.delete(0,tkinter.END)
    phone_entry.delete(0, tkinter.END)
    position_entry.delete(0, tkinter.END)
    money_entry.delete(0, tkinter.END)
    tax_entry.config(state=tkinter.NORMAL)
    tax_entry.delete(0, tkinter.END)
   # result_label2 = tkinter.Label(root, text="your income    ", font=23, bg='#99cfe0', fg='light yellow')
   #result_label2.place(x=20, y=300)

#info of the gui
size=root.geometry('390x520')
root.resizable(False,False)
color=root.config(bg='#99cfe0')
title=root.title('CCTC') #CCTC = cyber cookies tax calculator

#enterface of our gui
h1=tkinter.Label(root,text='calculate your tax',font="script 39",bd=4,bg='#99cfe0',fg='#ffbd07').pack(pady=20)
name=tkinter.Label(text='Employee name',font=23,bg='#99cfe0',fg='light yellow').place(x=20,y=100)
phone=tkinter.Label(text='Phone number',font=23,bg='#99cfe0',fg='light yellow').place(x=20,y=150)
position=tkinter.Label(text='position',font=23,bg='#99cfe0',fg='light yellow').place(x=20,y=200)
money=tkinter.Label(text='M per month',font=23,bg='#99cfe0',fg='light yellow').place(x=20,y=250)
result_label =tkinter.Label(root, text="your income ",font=23,bg='#99cfe0',fg='light yellow')
result_label.place(x=20,y=300)


#entry
namevalue=tkinter.StringVar()
phonevalue=tkinter.StringVar()
positionvalue=tkinter.StringVar()
tax=tkinter.StringVar()



name_entry=tkinter.Entry(root,textvariable=namevalue,width=20,bd=1,font=15)
phone_entry=tkinter.Entry(root,textvariable=phonevalue,width=20,bd=1,font=15)
position_entry=tkinter.Entry(root,textvariable=positionvalue,width=20,bd=1,font=15)
money_entry=tkinter.Entry(root,width=20,bd=1,font=15)
tax_entry=tkinter.Entry(root,width=20,bd=1,font=15)
tax_entry.config(state=tkinter.NORMAL)


#entry place
name_entry.place(x=150,y=100)
phone_entry.place(x=150,y=150)
position_entry.place(x=150,y=200)
money_entry.place(x=150,y=250)
tax_entry.place(x=150,y=300)




# button
#comand=lambda:[btn1f] and [btn2f] are used to add diffrent comand
btn=tkinter.Button(text='calculate tax',font='script 19',fg='white',width=13,height=1,bg='grey',command=lambda: [btn1f()]).place(x=70,y=400)
btn2=tkinter.Button(text='clear',font='script 19',fg='white',width=13,height=1,bg='grey',command=lambda: [btn2f()]).place(x=210,y=400)
btn3=tkinter.Button(text='save',font='script 19',fg='white',width=9,height=1,bg='grey',command=lambda: [btn3f()]).place(x=150,y=455)




root.mainloop()