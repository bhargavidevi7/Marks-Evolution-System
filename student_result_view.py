from tkinter import*
import mysql.connector
def myres():
    con=mysql.connector.connect(host="localhost",user="root",password="Jvps@1495",database="aditya1")
    cur=con.cursor()
    htno=t.get()
    sql="select *from result where htno=%s"
    val=(htno,)
    cur.execute(sql,val)
    myres=cur.fetchone()
    l4.config(text=myres[1])
    l8.config(text=myres[2])
    l10.config(text=myres[3])
    l12.config(text=myres[4])
    l14.config(text=myres[5])
    l16.config(text=myres[6])
    l18.config(text=myres[7])
    print(myres)
stdres=Tk()
stdres.title('Student Semester Result')
stdres.geometry('500x400')
l1=Label(stdres,text='STUDENT RESULT')
l2=Label(stdres,text='Htno:')
t=Entry(stdres)
b=Button(stdres,text='Submit',command=myres)
l3=Label(stdres,text='Name:')
l4=Label(stdres,text="")

l5=Label(stdres,text='Subject')
l6=Label(stdres,text="Marks")

l7=Label(stdres,text="Maths:")
l8=Label(stdres,text="")

l9=Label(stdres,text="Physics:")
l10=Label(stdres,text="")

l11=Label(stdres,text="Computer Science:")
l12=Label(stdres,text="")

l13=Label(stdres,text="Total:")
l14=Label(stdres,text="")

l15=Label(stdres,text="Percentage:")
l16=Label(stdres,text="")

l17=Label(stdres,text="Result:")
l18=Label(stdres,text="")

l1.grid(row=0,column=1)
l2.grid(row=1,column=0)
t.grid(row=1,column=1)
b.grid(row=1,column=2)

l3.grid(row=2,column=1)
l4.grid(row=2,column=2)

l5.grid(row=3,column=1)
l6.grid(row=3,column=2)

l7.grid(row=4,column=1)
l8.grid(row=4,column=2)

l9.grid(row=5,column=1)
l10.grid(row=5,column=2)

l11.grid(row=6,column=1)
l12.grid(row=6,column=2)

l13.grid(row=7,column=1)
l14.grid(row=7,column=2)

l15.grid(row=7,column=3)
l16.grid(row=7,column=4)

l17.grid(row=7,column=5)
l18.grid(row=7,column=6)

mainloop()
