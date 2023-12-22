#MY COMPUTER PROJECT
#TOPIC ---> INSTITUTE MANAGEMENT SYSTEM
#SUBBMITTED TO ---> MR. ANIL BHALOTIA SIR
#SUBBMITTED BY ---> ANSHUL JOHARI
#CLASS ---> XII-A



from tkinter import *
import mysql.connector as msc
from tkinter import messagebox



#ADD STUDENT
def m1():
    
    def addstu():
        admno=t1.get()
        sname=t2.get()
        cls=t3.get()
        fn=t4.get()
        mn=t5.get()
        dob=t6.get()
        phn=t7.get()
        course=t8.get()

        con=msc.connect(host="localhost",user="root",password="anshul2102",database="ims")
        query1="select * from students where admno={}".format(admno)
        cur=con.cursor()
        cur.execute(query1)
        rec=cur.fetchall()
        if len(rec)==0:

            query2="insert into students values({},'{}','{}','{}','{}','{}','{}','{}')".format(admno,sname,cls,fn,mn,phn,dob,course)
            cur.execute(query2)
            con.commit()
            con.close()
            messagebox.showinfo("Success","Student details have been saved successfully")

            t1.delete(0,'end')
            t2.delete(0,'end')
            t3.delete(0,'end')
            t4.delete(0,'end')
            t5.delete(0,'end')
            t6.delete(0,'end')
            t7.delete(0,'end')
            t8.delete(0,'end')
        else:
            messagebox.showinfo("Success","Student admission number already exists.")
            t1.delete(0,'end')
            t2.delete(0,'end')
            t3.delete(0,'end')
            t4.delete(0,'end')
            t5.delete(0,'end')
            t6.delete(0,'end')
            t7.delete(0,'end')
            t8.delete(0,'end')


    stu=Tk()
    stu.geometry("550x550")
    stu.config(background="black")
    stu.title("Add Student")

    l1=Label(stu,text="FILL DETAILS TO ADD STUDENT")
    l1.config(font=("courier",16),bg="yellow")
    l1.place(x=90,y=10)

    l2=Label(stu,text="Admission No.-->",bg="green",font=("comic sans ms",14))
    l2.place(x=40,y=70)
    l3=Label(stu,text="Student Name-->",bg="green",font=("comic sans ms",14))
    l3.place(x=40,y=120)
    l4=Label(stu,text="Class-->",bg="green",font=("comic sans ms",14))
    l4.place(x=40,y=170)
    l5=Label(stu,text="Fathers Name-->",bg="green",font=("comic sans ms",14))
    l5.place(x=40,y=220)
    l6=Label(stu,text="Mothers Name-->",bg="green",font=("comic sans ms",14))
    l6.place(x=40,y=270)
    l7=Label(stu,text="DOB-->",bg="green",font=("comic sans ms",14))
    l7.place(x=40,y=320)
    l8=Label(stu,text="Phone No.-->",bg="green",font=("comic sans ms",14))
    l8.place(x=40,y=370)
    l8=Label(stu,text="Course-->",bg="green",font=("comic sans ms",14))
    l8.place(x=40,y=420)

    t1=Entry(stu,width=40)
    t1.place(x=230,y=70)
    t2=Entry(stu,width=40)
    t2.place(x=230,y=120)
    t3=Entry(stu,width=40)
    t3.place(x=230,y=170)
    t4=Entry(stu,width=40)
    t4.place(x=230,y=220)
    t5=Entry(stu,width=40)
    t5.place(x=230,y=270)
    t6=Entry(stu,width=40)
    t6.place(x=230,y=320)
    t7=Entry(stu,width=40)
    t7.place(x=230,y=370)
    t8=Entry(stu,width=40)
    t8.place(x=230,y=420)

    b1=Button(stu,text="ADD",width=10,height=1,command=addstu,bg="blue",fg="white",font=(7))
    b1.place(x=400,y=470)

    stu.mainloop()

#REMOVE STUDENT
def m2():
    
    def remstu():
        admno=t1.get()
        sname=t2.get()
        cls=t3.get()
        
        con=msc.connect(host="localhost",user="root",password="anshul2102",database="ims")
        query="delete from students where admno={} and sname='{}' and class={}".format(admno,sname,cls)
        cur=con.cursor()
        cur.execute(query)
        con.commit()
        con.close()
        messagebox.showinfo("Success","Student details have been removed successfully")
        t1.delete(0,'end')
        t2.delete(0,'end')
        t3.delete(0,'end')

    stu=Tk()
    stu.geometry("700x400")
    stu.config(background="black")
    l1=Label(stu,text="FILL DETAILS AND CLICK REMOVE TO REMOVE STUDENT")
    l1.config(font=("courier",18),bg="yellow")
    l1.place(x=25,y=40)
    l2=Label(stu,text="Admission No.-->",bg="green",font=("comic sans ms",14))
    l2.place(x=120,y=110)
    l3=Label(stu,text="Student Name-->",bg="green",font=("comic sans ms",14))
    l3.place(x=120,y=160)
    l4=Label(stu,text="Class-->",bg="green",font=("comic sans ms",14))
    l4.place(x=120,y=210)

    t1=Entry(stu,width=40)
    t1.place(x=320,y=110)
    t2=Entry(stu,width=40)
    t2.place(x=320,y=160)
    t3=Entry(stu,width=40)
    t3.place(x=320,y=210)

    b1=Button(stu,text="REMOVE",width=12,height=2,command=remstu,bg="blue",fg="white",font=(7))
    b1.place(x=300,y=300)

    stu.mainloop()

#SHOW STUDENT DETAILS
def m3():
    
    def showstu():
        admno=t1.get()
        
        con=msc.connect(host="localhost",user="root",password="anshul2102",database="ims")
        query="select * from students where admno={}".format(admno)
        cur=con.cursor()
        cur.execute(query)
        records=cur.fetchall()
        
        if len(records)==0:
            messagebox.showinfo("Sorry","no student available of admission no. {}".format(admno))
        else:
            row=records[0]
            t2.delete(0,'end')
            t3.delete(0,'end')
            t4.delete(0,'end')
            t5.delete(0,'end')
            t6.delete(0,'end')
            t7.delete(0,'end')
            t8.delete(0,'end')

            t2.insert(0,row[1])
            t3.insert(0,row[2])
            t4.insert(0,row[3])
            t5.insert(0,row[4])
            t6.insert(0,row[6])
            t7.insert(0,row[5])
            t8.insert(0,row[7])
        con.close()
        
    stu=Tk()
    stu.geometry("700x650")
    stu.config(background="black")
    l1=Label(stu,text="FILL ADMISSION NO. TO GET DETAILS OF STUDENT")
    l1.config(font=("courier",16),bg="yellow")
    l1.place(x=70,y=10)
    l2=Label(stu,text="Admission No.-->",bg="green",font=("comic sans ms",14))
    l2.place(x=100,y=70)
    l3=Label(stu,text="Student Name-->",bg="green",font=("comic sans ms",14))
    l3.place(x=50,y=220)
    l4=Label(stu,text="Class-->",bg="green",font=("comic sans ms",14))
    l4.place(x=50,y=270)
    l5=Label(stu,text="Fathers Name-->",bg="green",font=("comic sans ms",14))
    l5.place(x=50,y=320)
    l6=Label(stu,text="Mothers Name-->",bg="green",font=("comic sans ms",14))
    l6.place(x=50,y=370)
    l7=Label(stu,text="DOB-->",bg="green",font=("comic sans ms",14))
    l7.place(x=50,y=420)
    l8=Label(stu,text="Phone No.-->",bg="green",font=("comic sans ms",14))
    l8.place(x=50,y=470)
    l9=Label(stu,text="Course-->",bg="green",font=("comic sans ms",14))
    l9.place(x=50,y=520)

    l9=Label(stu,text="---------------DETAILS---------------",bg="black",fg="white",font=("courier",16))
    l9.place(x=100,y=150)

    t1=Entry(stu,width=40)
    t1.place(x=300,y=75)
    t2=Entry(stu,width=40)
    t2.place(x=240,y=220)
    t3=Entry(stu,width=40)
    t3.place(x=240,y=270)
    t4=Entry(stu,width=40)
    t4.place(x=240,y=320)
    t5=Entry(stu,width=40)
    t5.place(x=240,y=370)
    t6=Entry(stu,width=40)
    t6.place(x=240,y=420)
    t7=Entry(stu,width=40)
    t7.place(x=240,y=470)
    t8=Entry(stu,width=40)
    t8.place(x=240,y=520)

    b1=Button(stu,text="SHOW",width=12,height=1,command=showstu,bg="blue",fg="white",font=(7))
    b1.place(x=500,y=570)

    stu.mainloop()

#ADD FACULTY
def m4():
    
    def addfac():
        fid=t1.get()
        fname=t2.get()
        exp=t3.get()
        qualifications=t4.get()
        courses=t5.get()
        salary=t6.get()
        phn=t7.get()
        
        con=msc.connect(host="localhost",user="root",password="anshul2102",database="ims")
        query="insert into faculties values({},'{}','{}','{}','{}',{},'{}')".format(fid,fname,exp,qualifications,courses,salary,phn)
        cur=con.cursor()
        cur.execute(query)
        con.commit()
        con.close()
        messagebox.showinfo("Success","faculty details have been saved successfully")

        t1.delete(0,'end')
        t2.delete(0,'end')
        t3.delete(0,'end')
        t4.delete(0,'end')
        t5.delete(0,'end')
        t6.delete(0,'end')
        t7.delete(0,'end')

    fac=Tk()
    fac.geometry("500x500")
    fac.config(background="black")
    fac.title("Add Faculty")

    l1=Label(fac,text="FILL DETAILS TO ADD FACULTY")
    l1.config(font=("courier",16),bg="yellow")
    l1.place(x=90,y=10)

    l2=Label(fac,text="Faculty ID-->",bg="green",font=("comic sans ms",14))
    l2.place(x=40,y=70)
    l3=Label(fac,text="Faculty Name-->",bg="green",font=("comic sans ms",14))
    l3.place(x=40,y=120)
    l4=Label(fac,text="Experience(in yrs)-->",bg="green",font=("comic sans ms",14))
    l4.place(x=40,y=170)
    l5=Label(fac,text="Qualifications-->",bg="green",font=("comic sans ms",14))
    l5.place(x=40,y=220)
    l6=Label(fac,text="Courses-->",bg="green",font=("comic sans ms",14))
    l6.place(x=40,y=270)
    l7=Label(fac,text="Salary-->",bg="green",font=("comic sans ms",14))
    l7.place(x=40,y=320)
    l8=Label(fac,text="Phone No.-->",bg="green",font=("comic sans ms",14))
    l8.place(x=40,y=370)

    t1=Entry(fac,width=40)
    t1.place(x=230,y=70)
    t2=Entry(fac,width=40)
    t2.place(x=230,y=120)
    t3=Entry(fac,width=40)
    t3.place(x=230,y=170)
    t4=Entry(fac,width=40)
    t4.place(x=230,y=220)
    t5=Entry(fac,width=40)
    t5.place(x=230,y=270)
    t6=Entry(fac,width=40)
    t6.place(x=230,y=320)
    t7=Entry(fac,width=40)
    t7.place(x=230,y=370)

    b1=Button(fac,text="ADD",width=10,height=1,command=addfac,bg="blue",fg="white",font=(7))
    b1.place(x=370,y=430)

    fac.mainloop()

#REMOVE FACULTY
def m5():
    
    def remfac():
        fid=t1.get()
        fname=t2.get()
        
        

        con=msc.connect(host="localhost",user="root",password="anshul2102",database="ims")
        query="delete from faculties where fid={} and fname='{}'".format(fid,fname)
        cur=con.cursor()
        cur.execute(query)
        con.commit()
        con.close()
        messagebox.showinfo("Success","Faculty details have been removed successfully")
        t1.delete(0,'end')
        t2.delete(0,'end')
        
    fac=Tk()
    fac.geometry("700x400")
    fac.config(background="black")
    l1=Label(fac,text="FILL DETAILS AND CLICK REMOVE TO REMOVE FACULTY")
    l1.config(font=("courier",18),bg="yellow")
    l1.place(x=25,y=40)
    l2=Label(fac,text="Faculty ID-->",bg="green",font=("comic sans ms",14))
    l2.place(x=120,y=110)
    l3=Label(fac,text="Faculty Name-->",bg="green",font=("comic sans ms",14))
    l3.place(x=120,y=160)

    t1=Entry(fac,width=40)
    t1.place(x=320,y=110)
    t2=Entry(fac,width=40)
    t2.place(x=320,y=160)

    b1=Button(fac,text="REMOVE",width=12,height=2,command=remfac,bg="blue",fg="white",font=(7))
    b1.place(x=300,y=300)

    fac.mainloop()

#SHOW FACULTY DETAILS
def m6():
    
    def clear():
        t1.delete(0,'end')
        t2.delete(0,'end')
        t3.delete(0,'end')
        t4.delete(0,'end')
        t5.delete(0,'end')
        t6.delete(0,'end')
        t7.delete(0,'end')

    def showfac():
        fid=t1.get()
        
        con=msc.connect(host="localhost",user="root",password="anshul2102",database="ims")
        query="select * from faculties where fid={}".format(fid)
        cur=con.cursor()
        cur.execute(query)
        records=cur.fetchall()
        
        if len(records)==0:
            messagebox.showinfo("Sorry","no faculty available of ID {}".format(fid))
        else:
            row=records[0]
            t2.delete(0,'end')
            t3.delete(0,'end')
            t4.delete(0,'end')
            t5.delete(0,'end')
            t6.delete(0,'end')
            t7.delete(0,'end')
            
            t2.insert(0,row[1])
            t3.insert(0,row[2])
            t4.insert(0,row[3])
            t5.insert(0,row[4])
            t6.insert(0,row[5])
            t7.insert(0,row[6])
            
        con.close()

    fac=Tk()
    fac.geometry("700x650")
    fac.config(background="black")

    l1=Label(fac,text="FILL FACULTY ID TO GET DETAILS OF FACULTY")
    l1.config(font=("courier",16),bg="yellow")
    l1.place(x=70,y=10)
    l2=Label(fac,text="Faculty ID-->",bg="green",font=("comic sans ms",14))
    l2.place(x=100,y=70)
    l3=Label(fac,text="Faculty Name-->",bg="green",font=("comic sans ms",14))
    l3.place(x=50,y=220)
    l4=Label(fac,text="Experience-->",bg="green",font=("comic sans ms",14))
    l4.place(x=50,y=270)
    l5=Label(fac,text="Qualifications-->",bg="green",font=("comic sans ms",14))
    l5.place(x=50,y=320)
    l6=Label(fac,text="Courses-->",bg="green",font=("comic sans ms",14))
    l6.place(x=50,y=370)
    l7=Label(fac,text="Salary-->",bg="green",font=("comic sans ms",14))
    l7.place(x=50,y=420)
    l8=Label(fac,text="Phone No.-->",bg="green",font=("comic sans ms",14))
    l8.place(x=50,y=470)

    l9=Label(fac,text="---------------DETAILS---------------",bg="black",fg="white",font=("courier",16))
    l9.place(x=100,y=150)

    t1=Entry(fac,width=40)
    t1.place(x=300,y=75)
    t2=Entry(fac,width=40)
    t2.place(x=240,y=220)
    t3=Entry(fac,width=40)
    t3.place(x=240,y=270)
    t4=Entry(fac,width=40)
    t4.place(x=240,y=320)
    t5=Entry(fac,width=40)
    t5.place(x=240,y=370)
    t6=Entry(fac,width=40)
    t6.place(x=240,y=420)
    t7=Entry(fac,width=40)
    t7.place(x=240,y=470)

    b1=Button(fac,text="SHOW",width=12,height=1,command=showfac,bg="blue",fg="white",font=(7))
    b1.place(x=500,y=570)
    b2=Button(fac,text="CLEAR",width=12,height=1,command=clear,bg="blue",fg="white",font=(7))
    b2.place(x=300,y=570)

    fac.mainloop()

#SHOW/ADD FEE DETAILS
def m7():
    
    def showfee():
        admno=t1.get()
                
        con=msc.connect(host="localhost",user="root",password="anshul2102",database="ims")
        query="select course from fees where admno={}".format(admno)
        cur=con.cursor()
        cur.execute(query)
        records=cur.fetchall()
        row=records[0]
        t4.insert(0,row[0])
        q1="select sum(feepaid) from fees where admno={}".format(admno)
        cur.execute(q1)
        fp=cur.fetchall()
        t2.insert(0,fp[0][0])
        q2="select min(remainingfee) from fees where admno={}".format(admno)
        cur.execute(q2)
        rf=cur.fetchall()
        t3.insert(0,rf[0][0])
        con.commit()
        con.close()

    def clear1():
        t1.delete(0,'end')
        t2.delete(0,'end')
        t3.delete(0,'end')
        t4.delete(0,'end')        

    def clear2():
        t5.delete(0,'end')
        t6.delete(0,'end')
        t7.delete(0,'end')
        t8.delete(0,'end')
        t9.delete(0,'end')

    def addfee():
        admno=t5.get()
        feepaid=t6.get()
        dateoffee=t8.get()
        remainingfee=t7.get()
        course=t9.get()
                
        con=msc.connect(host="localhost",user="root",password="anshul2102",database="ims")
        query="insert into fees values({},{},'{}',{},'{}')".format(admno,feepaid,dateoffee,remainingfee,course)
        cur=con.cursor()
        cur.execute(query)
        messagebox.showinfo("Success","Fee Details have been saved successfully")
        con.commit()
        con.close()
        
        t5.delete(0,'end')
        t6.delete(0,'end')
        t7.delete(0,'end')
        t8.delete(0,'end')
        
    fee=Tk()
    fee.geometry("1200x500")
    fee.config(background="black")
    fee.title("Add Fee")

    l1=Label(fee,text="FILL ADMISSION NO. TO GET FEE DETAILS")
    l1.config(font=("courier",18),bg="yellow")
    l1.place(x=50,y=20)

    l2=Label(fee,text="Admission No.-->",bg="green",font=("comic sans ms",14))
    l2.place(x=60,y=80)
    l3=Label(fee,text="Fee Paid-->",bg="green",font=("comic sans ms",14))
    l3.place(x=60,y=180)
    l4=Label(fee,text="Remaining Fee-->",bg="green",font=("comic sans ms",14))
    l4.place(x=60,y=230)
    l5=Label(fee,text="Course-->",bg="green",font=("comic sans ms",14))
    l5.place(x=60,y=280)

    l6=Label(fee,text="----------DETAILS----------",bg="black",fg="white",font=("courier",16))
    l6.place(x=100,y=130)

    t1=Entry(fee,width=40)
    t1.place(x=250,y=80)
    t2=Entry(fee,width=40)
    t2.place(x=250,y=180)
    t3=Entry(fee,width=40)
    t3.place(x=250,y=230)
    t4=Entry(fee,width=40)
    t4.place(x=250,y=280)

    b1=Button(fee,text="SHOW",width=14,height=2,command=showfee,bg="blue",fg="white",font=(7))
    b1.place(x=300,y=360)
    b2=Button(fee,text="CLEAR",width=12,height=2,command=clear1,bg="blue",fg="white",font=(7))
    b2.place(x=100,y=360)

    l7=Label(fee,text="FILL DETAILS TO ADD FEE DETAILS")
    l7.config(font=("courier",18),bg="yellow")
    l7.place(x=690,y=20)

    l8=Label(fee,text="Admission No.-->",bg="green",font=("comic sans ms",14))
    l8.place(x=700,y=100)
    l9=Label(fee,text="Fee Paid Now-->",bg="green",font=("comic sans ms",14))
    l9.place(x=700,y=150)
    l10=Label(fee,text="Fee Left Now-->",bg="green",font=("comic sans ms",14))
    l10.place(x=700,y=200)
    l11=Label(fee,text="Date Of Fee-->",bg="green",font=("comic sans ms",14))
    l11.place(x=700,y=250)
    l12=Label(fee,text="Course-->",bg="green",font=("comic sans ms",14))
    l12.place(x=700,y=300)

    l13=Label(fee,text="------>",bg="black",fg="white",font=("courier",20))
    l13.place(x=550,y=170)
    l14=Label(fee,text="------>",bg="black",fg="white",font=("courier",20))
    l14.place(x=550,y=200)
    l15=Label(fee,text="------>",bg="black",fg="white",font=("courier",20))
    l15.place(x=550,y=230)

    t5=Entry(fee,width=40)
    t5.place(x=890,y=100)
    t6=Entry(fee,width=40)
    t6.place(x=890,y=150)
    t7=Entry(fee,width=40)
    t7.place(x=890,y=200)
    t8=Entry(fee,width=40)
    t8.place(x=890,y=250)
    t9=Entry(fee,width=40)
    t9.place(x=890,y=300)

    b3=Button(fee,text="ADD",width=14,height=2,command=addfee,bg="blue",fg="white",font=(7))
    b3.place(x=940,y=360)
    b4=Button(fee,text="CLEAR",width=12,height=2,command=clear2,bg="blue",fg="white",font=(7))
    b4.place(x=740,y=360)

    fee.mainloop()

#REMOVE FEE DETAILS
def m8():
    
    def remfee():
        admno=t1.get()
        course=t2.get()

        con=msc.connect(host="localhost",user="root",password="anshul2102",database="ims")
        query="delete from fees where admno={} and course='{}'".format(admno,course)
        cur=con.cursor()
        cur.execute(query)
        con.commit()
        con.close()
        messagebox.showinfo("Success","Fee details have been removed successfully")
        t1.delete(0,'end')
        t2.delete(0,'end')
        
    fee=Tk()
    fee.geometry("700x400")
    fee.config(background="black")
    l1=Label(fee,text="FILL DETAILS TO REMOVE FEE DETAILS")
    l1.config(font=("courier",18),bg="yellow")
    l1.place(x=110,y=40)
    l2=Label(fee,text="Addmission No.-->",bg="green",font=("comic sans ms",14))
    l2.place(x=120,y=110)
    l3=Label(fee,text="Course-->",bg="green",font=("comic sans ms",14))
    l3.place(x=120,y=160)

    t1=Entry(fee,width=40)
    t1.place(x=320,y=110)
    t2=Entry(fee,width=40)
    t2.place(x=320,y=160)

    b1=Button(fee,text="REMOVE",width=12,height=2,command=remfee,bg="blue",fg="white",font=(7))
    b1.place(x=300,y=300)

    fee.mainloop()



#IMS MAIN PAGE


ims=Tk()
ims.geometry("700x400")
ims.config(bg="black")
ims.title("Institute Management System")
bgimage=PhotoImage(file=r"image.png")
Label(ims,image=bgimage).place(relwidth=1,relheight=1.5)

la1=Label(ims,text="EDUCATION IS THE KEY TO YOUR SUCCESS",background="black",fg="blue",font=("verdan 15",20,'underline'))
la1.place(x=50,y=30)
button1=Button(ims,text="Add Student",command=m1,bg="black",fg="yellow",font=("comic sans ms",14))
button1.place(x=60,y=100)
button2=Button(ims,text="Remove Student",command=m2,bg="black",fg="yellow",font=("comic sans ms",14))
button2.place(x=260,y=100)
button3=Button(ims,text="Student Details",command=m3,bg="black",fg="yellow",font=("comic sans ms",14))
button3.place(x=490,y=100)
button4=Button(ims,text="Add Faculty",command=m4,bg="black",fg="yellow",font=("comic sans ms",14))
button4.place(x=60,y=160)
button5=Button(ims,text="Remove Faculty",command=m5,bg="black",fg="yellow",font=("comic sans ms",14))
button5.place(x=260,y=160)
button6=Button(ims,text="Faculty Details",command=m6,bg="black",fg="yellow",font=("comic sans ms",14))
button6.place(x=490,y=160)
button7=Button(ims,text="Add/Show Fee Details",command=m7,bg="black",fg="yellow",font=("comic sans ms",14))
button7.place(x=110,y=220)
button8=Button(ims,text="Remove Fee Details",command=m8,bg="black",fg="yellow",font=("comic sans ms",14))
button8.place(x=390,y=220)

ims.mainloop()


#PROJECT COMPLETED
#THANK YOU
