from tkinter import*
import mysql.connector
def myresult():
    con=mysql.connector.connect(host="localhost",user="root",password="Jvps@1495",database="aditya1")
    cur=con.cursor()
    ht=t2.get()
    sname=t3.get()
    s1=int(t4.get())
    s2=int(t5.get())
    s3=int(t6.get())
    total=s1+s2+s3
    avg=total/3
    if avg>=90:
        res="Distinction"
    elif avg>=70:
        res="First Class"
    elif avg>=50:
        res="Second Class"
    elif avg>=40:
        res="Pass"
    else:
        res="Fail"
    sql="insert into result(htno,name,s1,s2,s3,total,avg,grade)values(%s,%s,%s,%s,%s,%s,%s,%s)"
    val=(ht,sname,s1,s2,s3,total,avg,res)
    cur.execute(sql,val)
    con.commit()
    l7.config(text="Student details stored successfully")
sem=Tk()
sem.geometry('500x500')
sem.title('UG Second Semester Result Database')
l1=Label(sem,text="STUDENT DATABASE",font=("Times New Roman",20))
l2=Label(sem,text="Enter HTNO:",font=("Times New Roman",18))
t2=Entry(sem)
l3=Label(sem,text="Enter Name:",font=("Times New Roman",18))
t3=Entry(sem)
l4=Label(sem,text="Enter Maths:",font=("Times New Roman",18))
t4=Entry(sem)
l5=Label(sem,text="Enter Physics:",font=("Times New Roman",18))
t5=Entry(sem)
l6=Label(sem,text="Enter CS:",font=("Times New Roman",18))
t6=Entry(sem)
b=Button(sem,text="Submit",font=("Times New Roman",18),command=myresult)
l7=Label(sem,text="",font=("Times New Roman",16))

l1.grid(row=0,column=1)

l2.grid(row=1,column=0)
t2.grid(row=1,column=1)

l3.grid(row=2,column=0)
t3.grid(row=2,column=1)

l4.grid(row=3,column=0)
t4.grid(row=3,column=1)

l5.grid(row=4,column=0)
t5.grid(row=4,column=1)

l6.grid(row=5,column=0)
t6.grid(row=5,column=1)

b.grid(row=6,column=0)
l7.grid(row=6,column=1)
mainloop()
