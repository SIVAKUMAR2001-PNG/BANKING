from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import pymysql
import tkinter as tk
from PIL import Image, ImageTk

Bank=Tk()
Bank.title("Design")
Bank.geometry("1200x1200")
Bank.config(bg="#97144D")
Bank.resizable(False,False)

####database
connection=pymysql.connect(
    host="localhost",
    user="root",
    password="kabi5016",
    database="kabi"
    )
 
my_database=connection.cursor()
print("database connect")

                                ##page deposit


def destroy3():
    page3.destroy()
        
def savedeposit():
    
    global my_database,count,btd,page3
    
    j = entd.get()
    
    connection_params = {
        'host': 'localhost',
        'user': 'root',
        'password': 'kabi5016',
        'db': 'kabi'
    }

    try:
        
            # Open the connection
        with pymysql.connect(**connection_params) as connection:
                          
            with connection.cursor() as cursor:
                                    
                    # Insert data into the database
                    
                query = "INSERT INTO deposit( amount) VALUES (%s)"
                values = (j)
                cursor.execute(query, values)
##                connection.commit()
                # Inform the user about the successful transaction
                messagebox.showinfo("Info", "Transaction Successfully!")
                

                fetch_query = "SELECT total FROM balance"
                cursor.execute(fetch_query)
                Account_balance = cursor.fetchall()
                count=0
                for i in Account_balance:
                    count+=i[0]

                total=count+int(j)
                record_id=101
                print(record_id)
                query = "UPDATE balance SET total=%s WHERE id=%s"
                values = (total,record_id)
                print(values)
                cursor.execute(query,values)
                connection.commit()
                print("update successfully")
            
             
                fetch_query = "SELECT total FROM  balance"
                cursor.execute(fetch_query)
                Account = cursor.fetchall()
                
                page3=Frame(paged,bg="#97144D",height=1200,width=800)
                page3.pack(fill=X)

                ent1=Label(page3,text="Account Balance",font=("Copperplate Gothic Bold", 20,),bg="#97144D",fg="white")
                ent1.place(x=450,y=250)
 
                ent=Label(page3,text=(Account),font=("Copperplate Gothic Bold", 20,),bg="#97144D",fg="black")
                ent.place(x=550,y=300)
                
                btd=Button(page3,text="X",bg="red",fg="white",command=destroy3,font=(3,),width=3)
                btd.place(x=1160,y=5)                      

                               
    except pymysql.MySQLError as e:
            
            # Handle any errors that occur during the database operations
        messagebox.showerror("Database Error", str(e))
    
                   
                          
def destroyd():
    paged.destroy()
    
def deposit():
    global entd,paged
    
    paged=Frame(page2,bg="#97144D",height=1200,width=1200)
    paged.pack(fill=X)
    img=Image.open('logo.png')   
    img1=ImageTk.PhotoImage(img)
    lab=Label(paged,image=img1,bg="#97144D",bd=0)
    lab.image=img1
    lab.place(x=510,y=50)

    lab4=Label(paged,text="Deposit Amount",font=("Copperplate Gothic Bold", 20,),bg="#97144D",fg="black")
    lab4.place(x=300,y=300)
    entd=Entry(paged,bg="white",font=("Times new roman",20,))
    entd.place(x=600,y=300)
    
    b1=Button(paged,text="SUBMIT",font=("Copperplate Gothic Bold", 20,),command=savedeposit,bg="#97144D",fg="white")
    b1.place(x=650,y=400)

    btnd=Button(paged,text="X",bg="red",fg="white",command=destroyd,font=(3,),width=3)
    btnd.place(x=1160,y=5)
    


                               ##withdraw

def destroym():
    pagem.destroy()



def widraw():
    global pagem,r,Max
    p=entw.get()
    p = int(p)
    
    connection_params = {
        
        'host': 'localhost',
        'user': 'root',
        'password': 'kabi5016',
        'db': 'kabi'
    }
    try:
                # Open the connection
        with pymysql.connect(**connection_params) as connection:
                        
            with connection.cursor() as cursor:
                fetch_query = "SELECT total FROM balance"
                cursor.execute(fetch_query)
                balance = cursor.fetchall()
                Max = 0
                for i in balance:
                    Max+=i[0]  

                if(p<=Max):
                    r=Max-p
                    
                    record_id=101
                    query = "UPDATE balance SET total=%s WHERE id=%s"
                    values = (r,record_id)
                    cursor.execute(query,values)
##                    connection.commit()

                    query = "INSERT INTO deposit( amount) VALUES (%s)"
                    values = (p)
                    cursor.execute(query, values)
                    connection.commit()

                    fetch_query = "SELECT total FROM balance"
                    cursor.execute(fetch_query)
                    Account_balance = cursor.fetchall()
    
                                    
                    pagem=Frame(pagew,bg="#97144D",height=1200,width=800)
                    pagem.pack(fill=X)

                    ent1=Label(pagem,text="Balance Amount",font=("Copperplate Gothic Bold", 20,),bg="#97144D",fg="white")
                    ent1.place(x=450,y=250)

                                        
                    ent=Label(pagem,text=Account_balance,font=("Copperplate Gothic Bold", 20,),bg="#97144D",fg="black")
                    ent.place(x=550,y=300)
                                
                    btd=Button(pagem,text="X",bg="red",fg="white",command=destroym,font=(3,),width=3)
                    btd.place(x=1160,y=5)
                else:
                    messagebox.showerror("error","insufficient balance")
    except pymysql.MySQLError as e:
            
                        # Handle any errors that occur during the database operations
        messagebox.showerror("Database Error", str(e))
                
    

def destroyw():
    pagew.destroy()
    
def withdraw():
    global entw,pagew
    
    pagew=Frame(page2,bg="#97144D",height=1200,width=1200)
    pagew.pack(fill=X)
    img=Image.open('logo.png')   
    img1=ImageTk.PhotoImage(img)
    lab=Label(pagew,image=img1,bg="#97144D",bd=0)
    lab.image=img1
    lab.place(x=510,y=50)
    
    labl4=Label(pagew,text="Withdraw Amount",font=("Copperplate Gothic Bold", 20,),bg="#97144D",fg="black")
    labl4.place(x=300,y=300)
    entw=Entry(pagew,bg="white",font=("Times new roman",20,))
    entw.place(x=600,y=300)
    
    bt1=Button(pagew,text="SUBMIT",font=("Copperplate Gothic Bold", 20,),command=widraw,bg="#97144D",fg="white")
    bt1.place(x=650,y=400)
    btnd=Button(pagew,text="X",bg="red",fg="white",command=destroyw,font=(3,),width=3)
    btnd.place(x=1160,y=5)
    
                                 ##Balance page

def destroybe():
    pagek.destroy()

def showbalance():
    global bal,Sum,pagek
       
    connection_params = {
        'host': 'localhost',
        'user': 'root',
        'password': 'kabi5016',
        'db': 'kabi'
    }
    try:
            # Open the connection
        with pymysql.connect(**connection_params) as connection:
                    
            with connection.cursor() as cursor:
                fetch_query = "SELECT total FROM balance"
                cursor.execute(fetch_query)
                balance = cursor.fetchall()
                            
                pagek=Frame(pageb,bg="#97144D",height=1200,width=800)
                pagek.pack(fill=X)

                ent1=Label(pagek,text="Account Balance",font=("Copperplate Gothic Bold", 20,),bg="#97144D",fg="white")
                ent1.place(x=450,y=250)
                                    
                ent=Label(pagek,text=balance,font=("Copperplate Gothic Bold", 20,),bg="#97144D",fg="black")
                ent.place(x=530,y=300)
                                
                btd=Button(pagek,text="X",bg="red",fg="white",command=destroybe,font=(3,),width=3)
                btd.place(x=1160,y=5)
    except pymysql.MySQLError as e:
        
                      # Handle any errors that occur during the database operations
        messagebox.showerror("Database Error", str(e))
            
    
                    
      
def destroyb():
    pageb.destroy()
def balance():
    global btnd,entb,ent1,pageb
    
    pageb=Frame(page2,bg="#97144D",height=1200,width=1200)
    pageb.pack(fill=X)
    img=Image.open('logo.png')   
    img1=ImageTk.PhotoImage(img)
    lab=Label(pageb,image=img1,bg="#97144D",bd=0)
    lab.image=img1
    lab.place(x=510,y=50)

    entb=Button(pageb,text="Show Balance",bg="#97144D",command=showbalance,fg="white",font=("Copperplate Gothic Bold", 25,))
    entb.place(x=450,y=350)
    
    btnd=Button(pageb,text="X",bg="red",fg="white",command=destroyb,font=(3,),width=3)
    btnd.place(x=1160,y=5)

    

                                   ##Transaction Histroy
def destroyex():
        pageenquiry.destroy()
def showenhistroy():
    global btdenq,entenq,pageenquiry
    Bank=tk.Tk()
    

    connection_params = {
        'host': 'localhost',
        'user': 'root',
        'password': 'kabi5016',
        'db': 'kabi'
    }
    try:
            # Open the connection
        with pymysql.connect(**connection_params) as connection:
                    
            with connection.cursor() as cursor:
                fetch_query = "SELECT * FROM deposit"
                cursor.execute(fetch_query)
                balance = cursor.fetchall()
                
                elist=[int(i[0])for i in balance]               
                
                                    
                pageenquiry=tk.Text(Bank,height=50,width=50,bg="#97144D",fg="white")
                pageenquiry.pack(padx=5,pady=5)

                

                for number in elist:
                    pageenquiry.insert(tk.END,str(number)+ '\n')
                    
                pageenquiry.config(state=tk.DISABLED)
                    

    except pymysql.MySQLError as e:
        
                      # Handle any errors that occur during the database operations
        messagebox.showerror("Database Error", str(e))
        
    
          

                             ##login
    
def destroyl():
##    global record_id
    page2.destroy()
##    record_id+=1
    
    
def login(): 
    global page2
    
    query=en1.get()
    values=en3.get()
    sql=("SELECT * from name where name=%s and pword=%s")
    my_database.execute(sql,(query,values))
    result=my_database.fetchall()
    print(result)
    if(result):
        
        page2=Frame(Bank,bg="#97144D",height=1200,width=1200)
        page2.pack(fill=X)

        img=Image.open('logo.png')   
        img1=ImageTk.PhotoImage(img)
        lab=Button(page2,image=img1,bg="#97144D",bd=0)
        lab.image=img1
        lab.place(x=500,y=50)

            
        img=Image.open('one.jpg')   
        img2=ImageTk.PhotoImage(img)
        but2=Button(page2,image=img2,bg="#97144D",command=deposit,bd=0)
        but2.image=img2
        but2.place(x=50,y=250)
        lab0=Label(page2,text="Deposit",font=("Copperplate Gothic Bold", 25,),bg="#97144D",fg="white")
        lab0.place(x=130,y=450)
                
        img=Image.open('wd.jpg')   
        img3=ImageTk.PhotoImage(img)
        but3=Button(page2,image=img3,bg="#97144D",command=withdraw,bd=0)
        but3.image=img3
        but3.place(x=450,y=250)
        lab1=Label(page2,text="WithDraw",font=("Copperplate Gothic Bold", 25,),bg="#97144D",fg="white")
        lab1.place(x=510,y=450)

        img=Image.open('blc.jpg')   
        img4=ImageTk.PhotoImage(img)
        but4=Button(page2,image=img4,bg="#97144D",command=balance,bd=0)
        but4.image=img4
        but4.place(x=850,y=250)
        lab2=Label(page2,text="Balance",font=("Copperplate Gothic Bold", 25,),bg="#97144D",fg="white")
        lab2.place(x=920,y=450)

        img=Image.open('tra.jpg')   
        img5=ImageTk.PhotoImage(img)
        but5=Button(page2,image=img5,command=showenhistroy,bg="#97144D",bd=0)
        but5.image=img5
        but5.place(x=450,y=500)
        lab3=Label(page2,text="Transaction Histroy",font=("Copperplate Gothic Bold", 25,),bg="#97144D",fg="white")
        lab3.place(x=400,y=700)


        btnd=Button(page2,text="X",bg="red",fg="white",command=destroyl,font=(3,),width=3)
        btnd.place(x=1160,y=5)

        
                      ##createacount save


def save():
    global a,b,c,d,e

    a=e1.get()
    b=e2.get()
    c=e3.get()
    d=e4.get()
    e=e5.get()

    print(a,b,c,d,e)

    if(a=="" or b=="" or c=="" or d=="" or e=="" ):
        messagebox.showerror("error","Enter All Details")
    elif(d!=e):
        messagebox.showerror("error","Check Password")    
    else:
        query="INSERT INTO name(name,age,email,pword,rpword) VALUES (%s,%s,%s,%s,%s)"
        values=(a,b,c,d,e,)
        my_database.execute(query,values)
        connection.commit()
        my_database.close()
        messagebox.showinfo("Info","Successfully Saved..!")
        page1.destroy()

                                   ##create account
        
def destroyc():
    page1.destroy()
def reset():
    e1.delete(0,tk.END)
    e2.delete(0,tk.END)
    e3.delete(0,tk.END)
    e4.delete(0,tk.END)
    e5.delete(0,tk.END)
                         
def createaccount():
    global e1,e2,e3,e4,e5,page1
    
    page1=Frame(Bank,bg="#97144D",height=1200,width=1200)
    page1.pack(fill=X)
    img=Image.open('logo.png')   
    img1=ImageTk.PhotoImage(img)
    lab=Button(page1,image=img1,bg="white",bd=0)
    lab.image=img1
    lab.place(x=500,y=30)
    
    lab0=Label(page1,text="Creat Account",font=("Lucida Calligraphy", 25, "bold"),bg="#97144D",fg="white")
    lab0.place(x=450,y=150)
    
    lab1=Label(page1,text="Name",font=("Times new roman", 20, "bold"),bg="#97144D",fg="black")
    lab1.place(x=425,y=250)

    lab2=Label(page1,text="Age",font=("Times new roman", 20, "bold"),bg="#97144D",fg="black")
    lab2.place(x=425,y=320)

    lab3=Label(page1,text="E-mail",font=("Times new roman", 20, "bold"),bg="#97144D",fg="black")
    lab3.place(x=425,y=390)

    lab5=Label(page1,text="Password",font=("Times new roman", 20, "bold"),bg="#97144D",fg="black")
    lab5.place(x=425,y=460)

    lab6=Label(page1,text="Confrim",font=("Times new roman", 20, "bold"),bg="#97144D",fg="black")
    lab6.place(x=425,y=530)

    e1=Entry(page1,bg="white",font=("Times new roman",))
    e1.place(x=600,y=250)
    e2=Entry(page1,bg="white",font=("Times new roman",))
    e2.place(x=600,y=320)
    e3=Entry(page1,bg="white",font=("Times new roman",))
    e3.place(x=600,y=390)   
    e4=Entry(page1,bg="white",font=("Times new roman",))
    e4.place(x=600,y=460)
    e5=Entry(page1,bg="white",font=("Times new roman",))
    e5.place(x=600,y=530)
    
    btn1=Button(page1,text="SAVE",bg="#97144D",fg="white",font=("Times new roman",15,),command=save)
    btn1.place(x=500,y=670)


    btn2=Button(page1,text="Reset",bg="#97144D",fg="white",font=("Times new roman",15,),command=reset)
    btn2.place(x=630,y=670)
    btnd=Button(page1,text="X",bg="red",fg="white",command=destroyc,font=(3,),width=3)
    btnd.place(x=1160,y=5)



                               ##login page


img=Image.open('logo.png')   
img1=ImageTk.PhotoImage(img)
lab=Button(Bank,image=img1,bg="white",bd=0)
lab.image=img1
lab.place(x=550,y=100)

lab0=Label(Bank,text="Login",font=("Times new roman", 20, "bold"),bg="#97144D",fg="white")
lab0.place(x=600,y=230)
lab1=Label(Bank,text="Name",font=("Times new roman", 20, "bold"),bg="#97144D",fg="black")
lab1.place(x=450,y=300)

lab2=Label(Bank,text="Password",font=("Times new roman", 20, "bold"),bg="#97144D",fg="black")
lab2.place(x=450,y=350)
en1=Entry(Bank,bg="white",font=("Times new roman",))
en1.place(x=600,y=300)
en3=Entry(Bank,bg="white",font=("Times new roman",))
en3.place(x=600,y=350)

b1=Button(Bank,text="Login",bg="#97144D",fg="white",font=("Times new roman", 20, "bold"),command=login)
b1.place(x=450,y=450)
b1=Button(Bank,text="Create Account",bg="#97144D",fg="white",font=("Times new roman", 20, "bold"),command=createaccount)
b1.place(x=700,y=450)


    
Bank.mainloop()




        
        
