import email
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import random as r
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
from fpdf import FPDF
import os
import n
from tkcalendar import Calendar, DateEntry


import mysql.connector

LARGEFONT = ("Verdana", 15)
userid = 1


def otpgen():
    otp = ""
    for i in range(4):
        otp += str(r.randint(1, 9))
    return otp


finalotp = otpgen()


class tkinterApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (
        StartPage, Adminlogi, Doctorlogin, Pateint, Admindash, Dotordash, Sdoctor, Pateintdetail, OtpCon, APPbook,clicinfo,callclinic,
        sawantINFO, patilINFO, karadINFO, muleIINFO, shubhamak, mahesh, anjali, ganesh,devloper):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        style = ttk.Style()
        style.map("C.TButton",
                  foreground=[('pressed', 'yellow'), ('active', 'red')],
                  background=[('pressed', '!disabled', '#00FF00'), ('active', '#00FF7F')]

                  )
        tk.Frame.__init__(self, parent, bg="green")

        labelw = tk.Label(self, text="WELCOME TO CLINIC MANAGMENT SYSTEM", font=40, bg="#B22222", fg="white", borderwidth=15,
                         padx=400)
        labelw.place(x=0, y=5)
        img = Image.open('dddd.png')
        self.tkimage = ImageTk.PhotoImage(img)
        tk.Label(self, image=self.tkimage, bg='skyblue').place(x=0, y=59)
        label = tk.Label(self,
                         text="We know you. We care for you. We’re with you.",
                         font=30, bg="#FF7F50", fg="white", padx=420)
        label.place(x=0, y=680)
        imgd = Image.open('doctorrpng.png')
        self.tkimaged = ImageTk.PhotoImage(imgd)
        imgp = Image.open('pateintpngg.png')
        self.tkimagep = ImageTk.PhotoImage(imgp)
        imga = Image.open('adminnpng.png')
        self.tkimagea = ImageTk.PhotoImage(imga)
        imgddd = Image.open('doctordetailspng.png')
        self.tkimageddd = ImageTk.PhotoImage(imgddd)
        imgin = Image.open('info.png')
        self.tkimagein = ImageTk.PhotoImage(imgin)

        button1 = tk.Button(self, bg='#B22222', image=self.tkimagein,command=lambda: controller.show_frame(APPbook)
                             )

        button1.place(x=83, y=15)
        imgicall = Image.open('call.png')
        self.tkimagecall = ImageTk.PhotoImage(imgicall)

        buttoncall = tk.Button(self, bg='#B22222', image=self.tkimagecall,command=lambda: controller.show_frame(callclinic)
                            )

        buttoncall.place(x=50, y=15)

        imgidev = Image.open('devloper.png')
        self.tkimagedev = ImageTk.PhotoImage(imgidev)

        buttondev = tk.Button(self, bg='#B22222', image=self.tkimagedev,command=lambda: controller.show_frame(devloper)
                               )

        buttondev.place(x=17, y=15)


        button1 = ttk.Button(self, text="ADMIN",image=self.tkimagea,
                             command=lambda: controller.show_frame(Adminlogi), style="C.TButton")

        button1.place(x=830, y=140, width=190, height=90)

        button2 = ttk.Button(self, text="DOCTOR", image=self.tkimaged,command=lambda: controller.show_frame(Doctorlogin), style="C.TButton")

        button2.place(x=830, y=270, width=190, height=90)

        button2 = ttk.Button(self, text="PATIENT",image=self.tkimagep,
                             command=lambda: controller.show_frame(Pateint), style="C.TButton")
        button2.place(x=830, y=400, width=190, height=90)

        button3 = ttk.Button(self, text="DOCTORS DETAILS",image=self.tkimageddd,
                             command=lambda: changerame(self, controller), style="C.TButton")
        button3.place(x=830, y=530, width=190, height=90)

        def changerame(self, controller):
            if 9 < 10:
                controller.show_frame(Sdoctor)

class devloper(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#FFA07A")
        label = tk.Label(self, text="DEVLOPER DETAILS", font=40, bg="#B22222", fg="white", borderwidth=5,
                         padx=550)
        label.place(x=0, y=5)
        img = Image.open('devlopers.png')
        self.tkimage = ImageTk.PhotoImage(img)
        tk.Label(self, image=self.tkimage, bg='#FFA07A').place(x=0, y=40)
        imgin = Image.open('homepngbutton.png')
        self.tkimagein = ImageTk.PhotoImage(imgin)
        tk.Button(self, image=self.tkimagein, bg='#ff9999', command=lambda: controller.show_frame(StartPage)).place(x=15, y=7)
        tk.Label(self,text="VISHNUKANT MULE",font=30,bg="#ffebcc").place(x=750,y=225)
        tk.Label(self,text="AVINASH ANDHALE",font=30,bg="#ffe0b3").place(x=750,y=260)
        tk.Label(self,text="PRATHAMESH NAIK",font=30,bg="#ffe0b3").place(x=750,y=295)
        tk.Label(self,text="JEMIN BHANUSHALI",font=30,bg="#ffe0b3").place(x=750,y=330)



class Adminlogi(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="skyblue")
        label = tk.Label(self, text="ADMIN LOGIN", font=40, bg="red", fg="white", borderwidth=5,
                         padx=550)
        label.place(x=0, y=5)
        tk.Button(self, text="⌂", bg='white', command=lambda: controller.show_frame(StartPage)).place(x=10, y=12)

        img = Image.open('adminloginbg.png')
        self.tkimage = ImageTk.PhotoImage(img)
        tk.Label(self, image=self.tkimage, bg='#FFA07A').place(x=0, y=40)
        label = tk.Label(self, text="if you want to become admin please contact devloper",
                         font=40, bg="orange", fg="white", padx=500)
        label.place(x=0, y=680)

        self.adminid = tk.StringVar()
        self.password = tk.StringVar()

        self.idname = tk.Entry(self, font=("calibre", 16), borderwidth=1, bg='lightyellow',width=22,
                               textvariable=self.adminid).place(x=810, y=328,height=40)
        self.passwordentry = tk.Entry(self, font=("calibre", 16), borderwidth=1, bg='lightyellow', show='*',width=22,
                                      textvariable=self.password).place(x=810, y=455,height=40)
        self.submit = ttk.Button(self, text="LOGIN", style="C.TButton",
                                 command=lambda: self.check_function(controller)).place(x=820, y=558, width=248,
                                                                                        height=45)

    def check_function(self, controller):

        if self.adminid.get() == "" or self.password.get() == "":
            messagebox.showerror("Error", "All fields are required")
        elif self.adminid.get() != "abc" or self.password.get() != "123":
            messagebox.showerror("Error", "Invalid Username or Password")
        else:
            controller.show_frame(Admindash)


class Doctorlogin(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="skyblue")
        label = tk.Label(self, text="DOCTOR LOGIN ...", font=40, bg="red", fg="white", borderwidth=5,
                         padx=550)
        label.place(x=0, y=5)
        img = Image.open('Doctorloginpng.png')
        self.tkimage = ImageTk.PhotoImage(img)
        tk.Label(self, image=self.tkimage, bg='#FFA07A').place(x=0, y=40)
        tk.Button(self, text="⌂", bg='white', command=lambda: controller.show_frame(StartPage)).place(x=10, y=12)



        self.adminid = tk.StringVar()
        self.password = tk.StringVar()

        self.idname = tk.Entry(self, font=("calibre", 16), borderwidth=1, bg='lightyellow',width=22,
                               textvariable=self.adminid).place(x=810, y=328,height=40)
        self.passwordentry = tk.Entry(self, font=("calibre", 16), borderwidth=1, bg='lightyellow', show='*',width=22,
                                      textvariable=self.password).place(x=810, y=455,height=40)
        self.submit = ttk.Button(self, text="LOGIN", style="C.TButton",
                                 command=lambda: self.check_function(controller)).place(x=820, y=585,
                                                                                        width=248,
                                                                                        height=45)

    def check_function(self, controller):

        if self.adminid.get() == "shubhamak" or self.password.get() == "shubhamak":
            controller.show_frame(shubhamak)
        elif self.adminid.get() == "mahesh" or self.password.get() == "mahesh":
            controller.show_frame(mahesh)
        elif self.adminid.get() == "anjali" or self.password.get() == "anjali":
            controller.show_frame(anjali)
        elif self.adminid.get() == "ganesh" or self.password.get() == "ganesh":
            controller.show_frame(ganesh)
        else:
            messagebox.showerror("Error", "Invalid Username or Password")


class shubhamak(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="skyblue")
        label = tk.Label(self, text="DR. SHUBHAMAK SAWANT", font=40, bg="red", fg="white", borderwidth=5, padx=790)
        tk.Button(self, text="⌂", bg='white', command=lambda: controller.show_frame(StartPage)).grid(row=0, column=0)

        self.EmailCom = tk.StringVar()
        f_nameE = tk.Entry(self, width=10, font=5, textvariable=self.EmailCom)

        label.grid(row=0, column=0, columnspan=12)
        tk.Label(self, text="Token NO", bg='yellow', width=20).grid(row=1, column=0)
        tk.Label(self, text="First Name", bg='pink', width=20).grid(row=1, column=1)
        tk.Label(self, text="Last Name", bg='pink', width=20).grid(row=1, column=2)
        tk.Label(self, text="Gender", bg='pink', width=20).grid(row=1, column=3)
        tk.Label(self, text="DOB", bg='pink', width=20).grid(row=1, column=4)
        tk.Label(self, text="Email Id", bg='pink', width=20).grid(row=1, column=5)
        tk.Label(self, text="Mobile-NO", bg='pink', width=20).grid(row=1, column=6)
        tk.Label(self, text="Day", bg='pink', width=20).grid(row=1, column=7)
        tk.Label(self, text="Month", bg='pink', width=20).grid(row=1, column=8)
        tk.Label(self, text="Year", bg='pink', width=20).grid(row=1, column=9)
        tk.Label(self, text="Sloat", bg='pink', width=20).grid(row=1, column=10)
        tk.Label(self, text="Status", bg='pink', width=20).grid(row=1, column=11)
        complete = tk.Button(self, text="DONE", bg="red", command=lambda: [self.updatetalble()])

        conn = mysql.connector.connect(
            user='root', password='', host='127.0.0.1', database='clinic_managment_system')
        my_conn = conn.cursor()
        my_conn.execute("SELECT * FROM `dr_shubhamak_sawant`")
        i = 2
        for pateint_details in my_conn:
            for j in range(len(pateint_details)):
                e = tk.Label(self, text=pateint_details[j], width=20, fg='black', bg='lightyellow', border=3)
                e.grid(row=i, column=j)

                complete.grid(row=j, column=11)
                f_nameE.grid(row=j, column=10)
            i = i + 1

    def updatetalble(self):
        Token = self.EmailCom.get()
        print(Token)
        insert_stmta = (" UPDATE dr_shubhamak_sawant SET Status = %s WHERE TokenNo = %s ")
        com = "completed"
        dataa = (com, Token)
        try:
            conna = mysql.connector.connect(user='root', password='', host='127.0.0.1',
                                            database='clinic_managment_system')
            my_conna = conna.cursor()

            my_conna.execute(insert_stmta, dataa)
            conna.commit()
        except:
            messagebox.showerror("Error", "dont know error")


class mahesh(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="skyblue")
        label = tk.Label(self, text="DR. MAHESH PATIL", font=40, bg="red", fg="white", borderwidth=5, padx=790)
        tk.Button(self, text="⌂", bg='white', command=lambda: controller.show_frame(StartPage)).grid(row=0, column=0)
        self.EmailCom = tk.StringVar()
        f_nameE = tk.Entry(self, width=10, font=5, textvariable=self.EmailCom)

        label.grid(row=0, column=0, columnspan=12)
        tk.Label(self, text="Token NO", bg='yellow', width=20).grid(row=1, column=0)
        tk.Label(self, text="First Name", bg='pink', width=20).grid(row=1, column=1)
        tk.Label(self, text="Last Name", bg='pink', width=20).grid(row=1, column=2)
        tk.Label(self, text="Gender", bg='pink', width=20).grid(row=1, column=3)
        tk.Label(self, text="DOB", bg='pink', width=20).grid(row=1, column=4)
        tk.Label(self, text="Email Id", bg='pink', width=20).grid(row=1, column=5)
        tk.Label(self, text="Mobile-NO", bg='pink', width=20).grid(row=1, column=6)
        tk.Label(self, text="Day", bg='pink', width=20).grid(row=1, column=7)
        tk.Label(self, text="Month", bg='pink', width=20).grid(row=1, column=8)
        tk.Label(self, text="Year", bg='pink', width=20).grid(row=1, column=9)
        tk.Label(self, text="Sloat", bg='pink', width=20).grid(row=1, column=10)
        tk.Label(self, text="Status", bg='pink', width=20).grid(row=1, column=11)
        complete = tk.Button(self, text="DONE", bg="red", command=lambda: [self.updatetalble()])

        conn = mysql.connector.connect(
            user='root', password='', host='127.0.0.1', database='clinic_managment_system')
        my_conn = conn.cursor()
        my_conn.execute("SELECT * FROM `dr_mahesh_patil`")
        complete = tk.Button(self, text="DONE", width=10, bg="lightgreen", command=lambda: self.updatetalble())
        i = 2
        for pateint_details in my_conn:
            for j in range(len(pateint_details)):
                e = tk.Label(self, text=pateint_details[j], width=20, fg='black', bg='lightyellow', border=3)
                e.grid(row=i, column=j)

                complete.grid(row=j, column=11)
                f_nameE.grid(row=j, column=10)

            i = i + 1

    def updatetalble(self):
        Token = self.EmailCom.get()
        print(Token)
        insert_stmta = (" UPDATE dr_mahesh_patil SET Status = %s WHERE TokenNo = %s ")
        com = "completed"
        dataa = (com, Token)
        try:
            conna = mysql.connector.connect(user='root', password='', host='127.0.0.1',
                                            database='clinic_managment_system')
            my_conna = conna.cursor()

            my_conna.execute(insert_stmta, dataa)
            conna.commit()
        except:
            messagebox.showerror("Error", "dont know error")


class anjali(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="skyblue")
        label = tk.Label(self, text="DR. ANJALI MULE", font=40, bg="red", fg="white", borderwidth=5, padx=790)
        tk.Button(self, text="⌂", bg='white', command=lambda: controller.show_frame(StartPage)).grid(row=0, column=0)

        self.EmailCom = tk.StringVar()
        f_nameE = tk.Entry(self, width=10, font=5, textvariable=self.EmailCom)

        label.grid(row=0, column=0, columnspan=12)
        tk.Label(self, text="Token NO", bg='yellow', width=20).grid(row=1, column=0)
        tk.Label(self, text="First Name", bg='pink', width=20).grid(row=1, column=1)
        tk.Label(self, text="Last Name", bg='pink', width=20).grid(row=1, column=2)
        tk.Label(self, text="Gender", bg='pink', width=20).grid(row=1, column=3)
        tk.Label(self, text="DOB", bg='pink', width=20).grid(row=1, column=4)
        tk.Label(self, text="Email Id", bg='pink', width=20).grid(row=1, column=5)
        tk.Label(self, text="Mobile-NO", bg='pink', width=20).grid(row=1, column=6)
        tk.Label(self, text="Day", bg='pink', width=20).grid(row=1, column=7)
        tk.Label(self, text="Month", bg='pink', width=20).grid(row=1, column=8)
        tk.Label(self, text="Year", bg='pink', width=20).grid(row=1, column=9)
        tk.Label(self, text="Sloat", bg='pink', width=20).grid(row=1, column=10)
        tk.Label(self, text="Status", bg='pink', width=20).grid(row=1, column=11)
        complete = tk.Button(self, text="DONE", bg="red", command=lambda: [self.updatetalble])
        conn = mysql.connector.connect(
            user='root', password='', host='127.0.0.1', database='clinic_managment_system')
        my_conn = conn.cursor()
        my_conn.execute("SELECT * FROM `dr_anjali_mule`")
        i = 2
        for pateint_details in my_conn:
            for j in range(len(pateint_details)):
                e = tk.Label(self, text=pateint_details[j], width=20, fg='black', bg='lightyellow', border=3)
                e.grid(row=i, column=j)

                complete.grid(row=j, column=11)
                f_nameE.grid(row=j, column=10)
            i = i + 1

    def updatetalble(self):
        Token = self.EmailCom.get()
        print(Token)
        insert_stmta = (" UPDATE dr_anjali_mule SET Status = %s WHERE TokenNo = %s ")
        com = "completed"
        dataa = (com, Token)
        try:
            conna = mysql.connector.connect(user='root', password='', host='127.0.0.1',
                                            database='clinic_managment_system')
            my_conna = conna.cursor()

            my_conna.execute(insert_stmta, dataa)
            conna.commit()
        except:
            messagebox.showerror("Error", "dont know error")


class ganesh(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="skyblue")
        label = tk.Label(self, text="DR. GANESH KARAD", font=40, bg="red", fg="white", borderwidth=5, padx=790)
        tk.Button(self, text="⌂", bg='white', command=lambda: controller.show_frame(StartPage)).grid(row=0, column=0)

        self.EmailCom = tk.StringVar()
        f_nameE = tk.Entry(self, width=10, font=5, textvariable=self.EmailCom)

        label.grid(row=0, column=0, columnspan=12)
        tk.Label(self, text="Token NO", bg='yellow', width=20).grid(row=1, column=0)
        tk.Label(self, text="First Name", bg='pink', width=20).grid(row=1, column=1)
        tk.Label(self, text="Last Name", bg='pink', width=20).grid(row=1, column=2)
        tk.Label(self, text="Gender", bg='pink', width=20).grid(row=1, column=3)
        tk.Label(self, text="DOB", bg='pink', width=20).grid(row=1, column=4)
        tk.Label(self, text="Email Id", bg='pink', width=20).grid(row=1, column=5)
        tk.Label(self, text="Mobile-NO", bg='pink', width=20).grid(row=1, column=6)
        tk.Label(self, text="Day", bg='pink', width=20).grid(row=1, column=7)
        tk.Label(self, text="Month", bg='pink', width=20).grid(row=1, column=8)
        tk.Label(self, text="Year", bg='pink', width=20).grid(row=1, column=9)
        tk.Label(self, text="Sloat", bg='pink', width=20).grid(row=1, column=10)
        tk.Label(self, text="Status", bg='pink', width=20).grid(row=1, column=11)
        complete = tk.Button(self, text="DONE", bg="red", command=lambda: [self.updatetalble(controller)])

        conn = mysql.connector.connect(
            user='root', password='', host='127.0.0.1', database='clinic_managment_system')
        my_conn = conn.cursor()
        my_conn.execute("SELECT * FROM `dr_ganesh_karad`")
        i = 2
        for pateint_details in my_conn:
            for j in range(len(pateint_details)):
                e = tk.Label(self, text=pateint_details[j], width=20, fg='black', bg='lightyellow', border=3)
                e.grid(row=i, column=j)

                complete.grid(row=j, column=11)
                f_nameE.grid(row=j, column=10)
            i = i + 1

    def updatetalble(self, controller):
        Token = self.EmailCom.get()
        print(Token)
        insert_stmta = (" UPDATE dr_ganesh_karad SET Status = %s WHERE TokenNo = %s ")
        com = "completed"
        dataa = (com, Token)
        try:
            conna = mysql.connector.connect(user='root', password='', host='127.0.0.1',
                                            database='clinic_managment_system')
            my_conna = conna.cursor()

            my_conna.execute(insert_stmta, dataa)
            conna.commit()
            controller.show_frame(ganesh)

        except:
            messagebox.showerror("Error", "dont know error")


class Pateint(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="skyblue")
        label = tk.Label(self, text="PATEINT REGISTRATION FORM ...", font=40, bg="green", fg="white", borderwidth=5,
                         padx=470)
        label.place(x=0, y=5)
        img = Image.open('bgforreg.png')
        self.tkimage = ImageTk.PhotoImage(img)
        tk.Label(self, image=self.tkimage, bg='skyblue').place(x=0, y=33)
        tk.Button(self, text="⌂", bg='white', command=lambda: controller.show_frame(StartPage)).place(x=10, y=12)
        connection = mysql.connector.connect(user='root', password='', host='127.0.0.1',
                                             database='clinic_managment_system')
        cursor = connection.cursor()
        sql_select_query = ("select * from current_user_data")
        connection.commit()
        cursor.execute(sql_select_query)
        records = cursor.fetchall()
        if len(records) == 0:
            cursor.close()
            connection.close()
        self.f_name = tk.StringVar()
        self.l_name = tk.StringVar()
        self.e_mail = tk.StringVar()
        self.m_no = tk.StringVar()
        self.DOB = tk.StringVar()
        self.address = tk.StringVar()
        self.pincode = tk.StringVar()
        self.state = tk.StringVar()
        self.var = tk.StringVar()

        self.f_nameE = tk.Entry(self, width=18, font=5, textvariable=self.f_name ,bg='#FEF5B2')
        self.l_nameE = tk.Entry(self, width=18, font=5, textvariable=self.l_name,bg='#FEF5B2')
        self.e_mailE = tk.Entry(self, width=30, font=5, textvariable=self.e_mail,bg='#FEF5B2')
        self.m_noE = tk.Entry(self, width=30, font=5, textvariable=self.m_no,bg='#FEF5B2')
        self.DOBE = tk.Entry(self, width=30, font=5, textvariable=self.DOB,bg='#FEF5B2')
        self.addressE = tk.Entry(self, width=30, font=5, textvariable=self.address,bg='#FEF5B2')
        self.pincodeE = tk.Entry(self, width=30, font=5, textvariable=self.pincode,bg='#FEF5B2')
        self.cityE = tk.Entry(self, width=30, font=5, textvariable=self.state,bg='#FEF5B2')
        self.Radio_button_maleE = tk.Radiobutton(self, text='', fg='black', value="Male", font=20,bg='white',
                                                 variable=self.var).place(x=640, y=233)
        self.Radio_button_femaleE = tk.Radiobutton(self, text='', fg='black', value="Female",bg='white',
                                                   font=20, variable=self.var).place(x=790, y=233)

        self.f_nameE.place(x=640, y=150)
        self.l_nameE.place(x=858, y=150)
        self.e_mailE.place(x=634, y=295)
        self.m_noE.place(x=633, y=354)
        self.DOBE.place(x=633, y=414)
        self.addressE.place(x=635, y=506)
        self.pincodeE.place(x=634, y=624)
        self.cityE.place(x=635, y=565)



        self.submit = ttk.Button(self, text="Next", style="C.TButton",
                                 command=lambda: [self.sendmail(controller), self.currentdata(), self.dataB()]).place(
            x=840, y=690, width=200, height=50)

    def currentdata(self):
        username = self.f_name.get()
        userlname = self.l_name.get()
        usergender = self.var.get()
        useremailid = self.e_mail.get()
        userdob = self.DOB.get()
        usermob = self.m_no.get()

        conn = mysql.connector.connect(
            user='root', password='', host='127.0.0.1', database='clinic_managment_system')
        insert_stmt = (
            "INSERT INTO current_user_data(id, username, usersurname, gender, useremail, userdbo, usermob)"
            "VALUES (%s, %s, %s, %s, %s ,%s ,%s )"
        )
        data = (userid, username, userlname, usergender, useremailid, userdob, usermob)
        cursor = conn.cursor()
        cursor.execute(insert_stmt, data)
        conn.commit()
        conn.close()

    def dataB(self):

        conn = mysql.connector.connect(
            user='root', password='', host='127.0.0.1', database='clinic_managment_system')

        emailid = self.e_mail.get()
        fname = self.f_name.get()
        lname = self.l_name.get()
        gender = self.var.get()
        mob = self.m_no.get()
        dob = self.DOB.get()
        address = self.address.get()
        pincode = self.pincode.get()
        state = self.state.get()




        insert_stmt = (
            "INSERT INTO pateint_details( First_Name,Last_Name, Gender, Mobile, Email, D_O_B, Address, Pincode, State)"
            "VALUES (%s, %s, %s, %s, %s ,%s ,%s ,%s ,%s)"
        )
        data = (fname, lname, gender, mob, emailid, dob, address, pincode, state)
        cursor = conn.cursor()
        cursor.execute(insert_stmt, data)
        conn.commit()
        conn.close()

    def sendmail(self, controller):
        emailid = self.e_mail.get()
        if ((self.f_name.get() == "") and (self.l_name.get() == "") and (self.e_mail.get() == "") and (self.address.get() == "")):
            messagebox.showerror("Error", "All feilds are required")
        else:
            try:
                s = smtplib.SMTP('smtp.gmail.com', 587)
                s.starttls()
                s.login("vishnukantmule@gmail.com", "cgezqyarhsxghdfy")
                SUBJECT = "Verify your Email address"
                TEXT = f"""TO book your appointment with doctor ,we just need to make sure that this email address is yours.

               To verify your email address,use this security code:{finalotp}

               if you didnt request this code. you can safely ignore this email.Someone else might have typed youremail address by mistake.

               Thanks,
               The Clinic Managment Team"""

                message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)

                s.sendmail("vishnukantmule@gmail.com", emailid, message, )
                s.quit()
                controller.show_frame(OtpCon)

            except:
                controller.show_frame(Pateint)
                messagebox.showerror("Error", "YOU ENTER WRONG EMAIL-ID PLEASE TRY TO CORRECT")


class Admindash(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent, bg="skyblue")
        label = tk.Label(self, text="ADMIN DASHBORD", font=40, bg="red", fg="white", borderwidth=5,
                         padx=750)
        tk.Button(self, text="⌂", bg='white', command=lambda: controller.show_frame(StartPage)).grid(row=0, column=0)

        label.grid(row=0, column=0, columnspan=10)
        tk.Label(self, text="First Name", bg='pink', width=24).grid(row=1, column=0)
        tk.Label(self, text="Last Name", bg='pink', width=24).grid(row=1, column=1)
        tk.Label(self, text="Gender", bg='pink', width=24).grid(row=1, column=2)
        tk.Label(self, text="Mobile No", bg='pink', width=24).grid(row=1, column=3)
        tk.Label(self, text="Email Id", bg='pink', width=24).grid(row=1, column=4)
        tk.Label(self, text="D-O-B", bg='pink', width=24).grid(row=1, column=5)
        tk.Label(self, text="Address", bg='pink', width=24).grid(row=1, column=6)
        tk.Label(self, text="Pincode", bg='pink', width=24).grid(row=1, column=7)
        tk.Label(self, text="City", bg='pink', width=24).grid(row=1, column=8)

        conn = mysql.connector.connect(
            user='root', password='', host='127.0.0.1', database='clinic_managment_system')
        my_conn = conn.cursor()
        my_conn.execute("SELECT * FROM `pateint_details`")
        i = 2
        for pateint_details in my_conn:
            for j in range(len(pateint_details)):
                e = tk.Entry(self, width=28, fg='black', bg='#F0FFFF')
                e.grid(row=i, column=j)
                e.insert(tk.END, pateint_details[j])
            i = i + 1


class Dotordash(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page 2", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)


class Sdoctor(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="skyblue")
        label = tk.Label(self, text="OUR BEST DOCTORS", font=40, bg="red", fg="white", borderwidth=5,
                         padx=550)
        label.place(x=0, y=5)

        tk.Button(self, text="⌂", bg='white', command=lambda: controller.show_frame(StartPage)).place(x=10, y=12)
        tk.Button(self, text="🢀", bg='white').place(x=30, y=12)

        img3 = Image.open('mahesh.jpg')
        self.tkimage3 = ImageTk.PhotoImage(img3)
        tk.Label(self, image=self.tkimage3, bg='red').place(x=770, y=70)

        img2 = Image.open('shubhamak.jpg')
        self.tkimage2 = ImageTk.PhotoImage(img2)
        tk.Label(self, image=self.tkimage2, bg='red').place(x=150, y=70)

        img1 = Image.open('ganesh.jpg')
        self.tkimage1 = ImageTk.PhotoImage(img1)
        tk.Label(self, image=self.tkimage1, bg='red').place(x=150, y=380)

        img = Image.open('vijita.jpg')
        self.tkimage = ImageTk.PhotoImage(img)
        tk.Label(self, image=self.tkimage, bg='red').place(x=770, y=380)

        img4 = Image.open('showd.png')
        self.tkimage4 = ImageTk.PhotoImage(img4)
        tk.Label(self, image=self.tkimage4, bg='skyblue').place(x=410, y=200)
        tk.Label(self, text="Keeping You Well", bg="skyblue", font=30).place(x=500, y=450)

        self.dr_a = ttk.Button(self, text="Dr.Shubhamak SawantT", style="C.TButton",
                               command=lambda: controller.show_frame(sawantINFO)).place(x=160, y=330, width=155,
                                                                                        height=32)
        self.dr_b = ttk.Button(self, text="Dr.Mahesh Patil", style="C.TButton",
                               command=lambda: controller.show_frame(patilINFO)).place(x=800, y=330, width=155,
                                                                                       height=32)
        self.dr_c = ttk.Button(self, text="Dr.Ganesh Karad", style="C.TButton",
                               command=lambda: controller.show_frame(karadINFO)).place(x=160, y=640, width=155,
                                                                                       height=32)
        self.dr_d = ttk.Button(self, text="Dr.Anjali Mule", style="C.TButton",
                               command=lambda: controller.show_frame(muleIINFO)).place(x=800, y=640, width=155,
                                                                                       height=32)


class Pateintdetail(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="skyblue")
        label = tk.Label(self, text="THANKYOU SO MUCH", font=40, bg="lightgreen", fg="white", borderwidth=5,
                         padx=550)
        label.place(x=0, y=5)
        img = Image.open('done.png')
        self.tkimage = ImageTk.PhotoImage(img)
        tk.Label(self, image=self.tkimage, background="skyblue").place(x=500, y=150)
        tk.Label(self, text="YOUR APPOINTMENT HAS BOOKED !PLZZ CHECK YOUR MAIL ONCE", font=80, fg="green",
                 borderwidth=10, background="skyblue").place(x=200, y=380)

class clicinfo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="skyblue")

        label = tk.Label(self, text="CLINIC DETAILS", font=40, bg="#FF7F50", fg="white", borderwidth=5,
                         padx=550)
        label.place(x=0, y=5)
        img = Image.open('cliniinfo.png')
        self.tkimage = ImageTk.PhotoImage(img)
        tk.Label(self, image=self.tkimage, bg='skyblue').place(x=0, y=31)
        tk.Button(self, text="⌂", bg='white', command=lambda: controller.show_frame(StartPage)).place(x=10, y=12)
class callclinic(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="skyblue")

        label = tk.Label(self, text="CONTACT DETAILS", font=40, bg="#FF7F50", fg="white", borderwidth=5,
                         padx=550)
        label.place(x=0, y=5)
        img = Image.open('callpng.png')
        self.tkimage = ImageTk.PhotoImage(img)
        tk.Label(self, image=self.tkimage, bg='skyblue').place(x=0, y=31)
        tk.Button(self, text="⌂", bg='white', command=lambda: controller.show_frame(StartPage)).place(x=10, y=12)
class OtpCon(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="skyblue")

        label = tk.Label(self, text="OTP CONFIRMATION ...", font=40, bg="green", fg="white", borderwidth=5,
                         padx=500)
        label.place(x=0, y=5)
        img = Image.open('otpconbg.png')
        self.tkimage = ImageTk.PhotoImage(img)
        tk.Label(self, image=self.tkimage, bg='skyblue').place(x=0, y=34)
        tk.Button(self, text="⌂", bg='white', command=lambda: controller.show_frame(StartPage)).place(x=10, y=12)

        self.VALUE = tk.IntVar()
        self.OTP = tk.Entry(self, width=33, font=20,bg='#d9d9d9' ,textvariable=self.VALUE).place(x=698, y=285, height=40)
        self.GENERATE = ttk.Button(self, text="Confirm", style="C.TButton",
                                   command=lambda: self.confirmfn(controller)).place(x=730, y=500, width=300, height=45)

    def confirmfn(self, controller):
        otpsended = int(finalotp)
        # int(otpsended)
        print(otpsended)
        inotp = int(self.VALUE.get())
        # int(inotp)
        print(inotp)

        if inotp == otpsended:
            controller.show_frame(APPbook)
            messagebox.showinfo("showinfo", "E-MAIL IS CONFIRM")
        elif inotp ==" ":
            controller.show_frame(OtpCon)
            messagebox.showerror("Error", "INVALID OTP")

        else:
            controller.show_frame(OtpCon)
            messagebox.showerror("Error", "INVALID OTP")


class APPbook(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="skyblue")

        self.label = tk.Label(self, text="Book Appointment ...", font=40, bg="red", fg="white", borderwidth=5,
                              padx=570)
        tk.Button(self, text="⌂", bg='white', command=lambda: controller.show_frame(StartPage)).place(x=10, y=12)

        self.label.place(x=0, y=5)

        self.Docter = tk.Label(self, text="Docter:", bg='skyblue', font='Verdana 15 bold')
        self.Docter.place(x=450, y=200)

        self.Day = tk.Label(self, text="Date:", bg='skyblue', font='Verdana 15 bold')
        self.Day.place(x=450, y=250)

        self.slot_l = tk.Label(self, text="Sloat:", bg='skyblue', font='Verdana 15 bold')
        self.slot_l.place(x=450, y=300)

        self.Month = tk.Label(self, text="Month:", bg='skyblue', font='Verdana 15 bold')
        self.Month.place(x=450, y=350)

        self.Year = tk.Label(self, text="Year:", bg='skyblue', font='Verdana 15 bold')
        self.Year.place(x=450, y=400)

        self.docter_var = tk.StringVar()
        self.day = tk.StringVar()
        self.Slot_v = tk.StringVar()
        self.month = tk.StringVar()
        self.year = tk.StringVar()

        self.Docter_box = ttk.Combobox(self, width=25, font=20, textvariable=self.docter_var, state='readonly')
        self.Docter_box['values'] = ('Dr.SHUBHAMAK SAWANT', 'Dr.MAHESH PATIL', 'Dr.GANESH KARAD', 'Dr.ANJALI MULE')
        self.Docter_box.current(0)
        self.Docter_box.place(x=550, y=200)

      #  self.Day = ttk.Entry(self, width=25, font=20, textvariable=self.day)
      #  self.Day.place(x=550, y=250)

        self.Slot = ttk.Combobox(self, width=25, font=20, textvariable=self.Slot_v, state='readonly')
        self.Slot['values'] = ('Morning-(10AM-2PM)', 'Evening-(4PM-7PM)')
        self.Slot.current(0)
        self.Slot.place(x=550, y=300)

        self.Month_Box = ttk.Combobox(self, width=25, font=20, textvariable=self.month, state='readonly')
        self.Month_Box['values'] = (
            'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
            'November',
            'December')
        self.Month_Box.current(0)
        self.Month_Box.place(x=550, y=350)

        tk.Button(self, text='Select DOB', width=5, command=self.calendar_view).place(x=740,y=250,height=25)


        self.Year = ttk.Entry(self, width=25, font=20, textvariable=self.year)
        self.Year.place(x=550, y=400)
        self.submit = ttk.Button(self, text="BOOK OPPOINTMENT", style="C.TButton",
                                 command=lambda: self.dataBook(controller)).place(x=550, y=500, width=250, height=60)

    def calendar_view(self):
        def print_sel():
            DoctorName = self.docter_var.get()
            e2 = tk.Entry(self, width=30)
            e2.insert(tk.END, cal.selection_get())
            e2.place(x=550,y=250,height=25)

            date=cal.selection_get()
            if DoctorName == "Dr.SHUBHAMAK SAWANT":
                conn = mysql.connector.connect(
                    user='root', password='', host='127.0.0.1', database='clinic_managment_system')
                insert_stmt = (
                    "INSERT INTO dr_shubhamak_sawant(Day)"
                    "VALUES (%s )"
                )
                data = (date)
                cursor = conn.cursor()
                cursor.execute(insert_stmt, data)
                conn.commit()
                conn.close()
            elif self.docter_var.get() == "Dr.MAHESH PATIL":
                conn = mysql.connector.connect(
                    user='root', password='', host='127.0.0.1', database='clinic_managment_system')
                insert_stmt = (
                    "INSERT INTO dr_mahesh_patil(Day)"
                    "VALUES (%s )"
                )
                data = (date)
                cursor = conn.cursor()
                cursor.execute(insert_stmt, data)
                conn.commit()
                conn.close()
            elif self.docter_var.get() == "Dr.GANESH KARAD":
                conn = mysql.connector.connect(
                    user='root', password='', host='127.0.0.1', database='clinic_managment_system')
                insert_stmt = (
                    "INSERT INTO dr_ganesh_karad(Day)"
                    "VALUES (%s )"
                )
                data = (date)
                cursor = conn.cursor()
                cursor.execute(insert_stmt, data)
                conn.commit()
                conn.close()
            elif self.docter_var.get() == "Dr.ANJALI MULE":
                conn = mysql.connector.connect(
                    user='root', password='', host='127.0.0.1', database='clinic_managment_system')
                insert_stmt = (
                    "INSERT INTO dr_anjali_mule(Day)"
                    "VALUES (%s )"
                )
                data = (date)
                cursor = conn.cursor()
                cursor.execute(insert_stmt, data)
                conn.commit()
                conn.close()
            else:
                print("wrong choice")

        top = tk.Toplevel(app)

        cal = Calendar(top, font="Arial 14", selectmode='day', cursor="hand1", year=2018, month=2, day=5)
        cal.pack(fill="both", expand=True)
        ttk.Button(top, text="ok", command=print_sel).pack()
        return "pk"

    def dataBook(self, controller):
        global usersurnameget, usernameget, usergenderget, userdobget, useremailget, usermobget
        TokenNumber = random.randint(1000, 9999)

        DoctorName = self.docter_var.get()
        AppDate = self.day.get()
        AppMonth = self.month.get()
        AppYear = self.year.get()
        Slot = self.Slot_v.get()
        statusis = "pending"

        try:
            connection = mysql.connector.connect(user='root', password='', host='127.0.0.1',
                                                 database='clinic_managment_system')

            sql_select_Query = "select * from current_user_data"
            cursor = connection.cursor()
            cursor.execute(sql_select_Query)
            records = cursor.fetchall()
            for row in records:
                useridget = row[0]
                usernameget = row[1]
                usersurnameget = row[2]
                usergenderget = row[3]
                useremailget = row[4]
                userdobget = row[5]
                usermobget = row[6]

            connection.close()
            cursor.close()
        except mysql.connector.Error as e:
            messagebox.showwarning("warning", "SORRY FOR INCONVINEINT SERVICE")
        if DoctorName == "Dr.SHUBHAMAK SAWANT":
            conn = mysql.connector.connect(
                user='root', password='', host='127.0.0.1', database='clinic_managment_system')
            insert_stmt = (
                "INSERT INTO dr_shubhamak_sawant(TokenNo,First_Name,Last_Name,Gender,DOB,Email,Mob_No,Month,Year,Slot,Status)"
                "VALUES (%s, %s, %s, %s, %s, %s ,%s ,%s,%s ,%s ,%s )"
            )
            data = (
            TokenNumber, usernameget, usersurnameget, usergenderget, userdobget, useremailget, usermobget, AppDate,
            AppMonth, AppYear, Slot, statusis)
            cursor = conn.cursor()
            cursor.execute(insert_stmt, data)
            conn.commit()
            conn.close()
            controller.show_frame(Pateintdetail)

        elif self.docter_var.get() == "Dr.MAHESH PATIL":
            conn = mysql.connector.connect(
                user='root', password='', host='127.0.0.1', database='clinic_managment_system')
            insert_stmt = (
                "INSERT INTO dr_mahesh_patil(TokenNo,First_Name,Last_Name,Gender,DOB,Email,Mob_No,Month,Year,Slot,Status)"
                "VALUES (%s,%s, %s, %s, %s, %s ,%s ,%s ,%s ,%s ,%s )"
            )
            data = (
            TokenNumber, usernameget, usersurnameget, usergenderget, userdobget, useremailget, usermobget, AppDate,
            AppMonth, AppYear, Slot, statusis)
            cursor = conn.cursor()
            cursor.execute(insert_stmt, data)
            conn.commit()
            conn.close()
            controller.show_frame(Pateintdetail)

        elif self.docter_var.get() == "Dr.GANESH KARAD":
            conn = mysql.connector.connect(
                user='root', password='', host='127.0.0.1', database='clinic_managment_system')
            insert_stmt = (
                "INSERT INTO dr_ganesh_karad(TokenNo,First_Name,Last_Name,Gender,DOB,Email,Mob_No,Month,Year,Slot,Status)"
                "VALUES (%s,%s, %s, %s, %s, %s ,%s ,%s,%s ,%s ,%s)"
            )
            data = (
            TokenNumber, usernameget, usersurnameget, usergenderget, userdobget, useremailget, usermobget, AppDate,
            AppMonth, AppYear, Slot, statusis)
            cursor = conn.cursor()
            cursor.execute(insert_stmt, data)
            conn.commit()
            conn.close()
            controller.show_frame(Pateintdetail)


        elif self.docter_var.get() == "Dr.ANJALI MULE":
            conn = mysql.connector.connect(
                user='root', password='', host='127.0.0.1', database='clinic_managment_system')
            insert_stmt = (
                "INSERT INTO dr_anjali_mule(TokenNo,First_Name,Last_Name,Gender,DOB,Email,Mob_No,Month,Year,Slot,Status)"
                "VALUES (%s,%s, %s, %s, %s, %s ,%s ,%s,%s ,%s  ,%s )"
            )
            data = (
            TokenNumber, usernameget, usersurnameget, usergenderget, userdobget, useremailget, usermobget, AppDate,
            AppMonth, AppYear, Slot, statusis)
            cursor = conn.cursor()
            cursor.execute(insert_stmt, data)
            conn.commit()
            conn.close()
            controller.show_frame(Pateintdetail)
        else:
            print("ERROR")


        pdf = FPDF()
        # create or add a page in pdf
        pdf.add_page()
        # set font style and size for text
        pdf.set_font('arial', size=12)
        # create cells and insert text in pdf
        # left aligned text
        fnamepd=usernameget
        lnamepd=usersurnameget
        genderpd=usergenderget
        dobpd=userdobget
        emailpd=useremailget
        phonepd=usermobget
        doctorpd=DoctorName
        tokenpd=TokenNumber
        datepd=AppDate
        timepd="2 PM"

        nameid = "YOUR APPOINTMENT DETAILS :"
        pdf.image('head.png', x=0, y=0, w=220, h=57)
        pdf.ln(57)
        pdf.set_text_color(0, 0, 255)
        pdf.cell(200, 10, 'PATEINT DETAILS :', 1, 1, 'L')
        # pdf.cell(200, 10,txt= str(nameid),ln=60,align='L')
        # center aligned text

        pdf.set_text_color(0, 0, 0)
        pdf.cell(200, 10, txt='FIRST NAME :', ln=60, align='L')
        pdf.cell(200, 10, txt=str(fnamepd), ln=60, align='C')
        pdf.cell(200, 10, txt='LAST NAME :', ln=70, align='L')
        pdf.cell(200, 10, txt=str(lnamepd), ln=70, align='C')
        pdf.cell(200, 10, txt='DATE OF BIRTH :', ln=80, align='L')
        pdf.cell(200, 10, txt=str(dobpd), ln=80, align='C')
        pdf.cell(200, 10, txt='EMAIL :', ln=90, align='L')
        pdf.cell(200, 10, txt=str(emailpd), ln=90, align='C')
        pdf.cell(200, 10, txt='PHONE NO :', ln=100, align='L')
        pdf.cell(200, 10, txt=str(phonepd), ln=100, align='C')
        pdf.cell(200, 10, txt='GENDER :', ln=110, align='L')
        pdf.cell(200, 10, txt=str(genderpd), ln=110, align='C')

        pdf.set_text_color(0, 0, 255)
        pdf.cell(200, 10, 'APPOINTMENT DETAILS :', 1, 1, 'L')
        pdf.ln(10)
        pdf.set_text_color(0, 0, 0)
        pdf.cell(200, 10, txt='DOCTOR :', ln=190, align='L')
        pdf.cell(200, 10, txt=str(doctorpd), ln=190, align='C')
        pdf.cell(200, 10, txt='TOKEN NO :', ln=200, align='L')
        pdf.cell(200, 10, txt=str(tokenpd), ln=200, align='C')
        pdf.cell(200, 10, txt='DATE :', ln=210, align='L')
        pdf.cell(200, 10, txt=str(datepd), ln=210, align='C')
        pdf.cell(200, 10, txt='TIME :', ln=220, align='L')
        pdf.cell(200, 10, txt=str(timepd), ln=220, align='C')

        pdf.image('tail.png', x=0, y=240, w=220, h=57)

        # save the pdf with any_name.pdf
        pdf.output('ClinicManagementSystem.pdf')
        print(f"text_pdf is created..and it is saved in:\n {os.getcwd()}")






        me = "vishnukantmule@gmail.com"
        you = useremailget
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "Link"
        msg['From'] = me
        msg['To'] = you

        text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
        html = f"""\
        <html>
          <head></head>
          <body bgcolor="#00FFFF">
            <h1 style="color: orange;">CLINIC MANAGMENT SYSTEM</h1>
            <hr color="red">
            <hr color="green">
            <img src="https://picsum.photos/1250/400?women" alt="error for load">
            <hr>
            <h2> Dear {usernameget}</h2>
            <p><h3>your appointment has been booked :</h3>
            <br>
            <br>

               <h3>NAME : {usernameget}&nbsp;{usersurnameget}</h3>
               <h3>MOBILE NO:{usermobget}</h3>
               <h3>DOCTOR :{DoctorName}</h3>
               <h3>TOKEN NO :{TokenNumber}</h3>
               <h3>SLOT :{Slot}</h3>
               <h3>DAY :{AppDate}</h3>
               <h3>MONTH :{AppMonth}</h3>
               <h3>YEAR :{AppYear}</h3>
            </p>
            <br>
            <br>
            <br>
            <hr>
            <p>
              <div>
                   <h3> PLEASE REMEMBER TO BRING :</h3>
                   <ul>
                    <li>Current List of All Medications You Are Taking.</li>
                    <li>Medical History.</li>
                    <li>A Family Member or Friend.</li>
                    </ul>
              </div>   
              <br>
                <img src="https://www.canva.com/design/DAE8b04WRBo/tKB1Olde3wtx7hYtV_VMJQ/watch?utm_content=DAE8b04WRBo&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink" alt="error for load">

            </p>

          </body>
        </html>
        """

        part1 = MIMEText(text, 'plain')
        part2 = MIMEText(html, 'html')

        msg.attach(part1)
        msg.attach(part2)

        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login('vishnukantmule@gmail.com', 'cgezqyarhsxghdfy')
        mail.sendmail(me, you, msg.as_string())
        mail.quit()
        n.sendmailforpdf()


class sawantINFO(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="skyblue")

        self.label = tk.Label(self, text="Dr.Shubhamak Sawant", font=40, bg="red", fg="white", borderwidth=5,
                              padx=530)
        self.label.place(x=0, y=5)
        tk.Button(self, text="⌂", bg='white', command=lambda: controller.show_frame(StartPage)).place(x=10, y=12)

        img = Image.open('shubhamak.jpg')
        self.tkimage = ImageTk.PhotoImage(img)
        tk.Label(self, image=self.tkimage, bg='red').place(x=60, y=50)
        self.label = tk.Label(self, text="Dr.Shubhamak Sawant", bg='skyblue', font=LARGEFONT).place(x=60, y=290)
        self.label = tk.Label(self, text="Specializations :", fg='red', bg='skyblue', font=LARGEFONT).place(x=370, y=60)
        self.label = tk.Label(self, text="⏺   Scoliosis surgery, minimally invasive and endoscopic spine surgery",
                              fg='black', bg='skyblue', font=20).place(x=390, y=100)
        self.label = tk.Label(self, text="⏺   Consultant - Spine Surgeon ", fg='black', bg='skyblue', font=20).place(
            x=390, y=130)

        self.label = tk.Label(self, text="Qualification :", fg='red', bg='skyblue', font=LARGEFONT).place(x=370, y=200)
        self.label = tk.Label(self, text="⏺   MBBS - NSCB Medical college, Jabalpur (2006) ", fg='black', bg='skyblue',
                              font=20).place(x=390,
                                             y=240)
        self.label = tk.Label(self, text="⏺   MS (ortho) - MGM Medical college, Indore (2009) ", fg='black',
                              bg='skyblue', font=20).place(x=390, y=270)

        self.label = tk.Label(self, text="Experience :", fg='red', bg='skyblue', font=LARGEFONT).place(x=370, y=320)
        self.label = tk.Label(self,
                              text="⏺   Experience of 10 years in spine surgery with special expertise in scoliosis surgery ",
                              fg='black',
                              bg='skyblue', font=20).place(x=390, y=360)
        self.label = tk.Label(self,
                              text="⏺   Dr.Sawant was Professor in Orthopedics and head of spine unit at (SAIMS), Indores ",
                              fg='black', bg='skyblue',
                              font=20).place(x=390, y=390)
        self.label = tk.Label(self, text="⏺   Role of posterior approach in multisegmental cervical myelopathy  ",
                              fg='black', bg='skyblue', font=20).place(x=390, y=420)
        self.label = tk.Label(self,
                              text="⏺   Predictive factors for progression of spondylolisthesis  ",
                              fg='black', bg='skyblue', font=20).place(x=390, y=450)

        self.label = tk.Label(self, text="Awards :", fg='red', bg='skyblue', font=LARGEFONT).place(x=370, y=500)
        self.label = tk.Label(self, text="⏺   Prof. K.T. Dholakia Gold Medal- best paper (IOACON 2008) ", fg='black',
                              bg='skyblue', font=20).place(
            x=390, y=540)
        self.label = tk.Label(self, text="⏺   Prof. Sudhir Kapoor gold medal for best case report of the year 2014 ",
                              fg='black',
                              bg='skyblue', font=20).place(x=390, y=570)

        self.label = tk.Label(self, text="OPD :", fg='red', bg='skyblue', font=LARGEFONT).place(x=40, y=350)

        self.label = tk.Label(self, text="OPD :", fg='red', bg='skyblue', font=LARGEFONT).place(x=40, y=350)
        self.label = tk.Label(self, text="● Morning-(10AM-2PM)", fg='black', bg='skyblue', font=10).place(x=30, y=390)
        self.label = tk.Label(self, text="● Evening-(4PM-7PM)", fg='black', bg='skyblue', font=10).place(x=30,
                                                                                                         y=420)

        self.label = tk.Label(self, text="COTACT :", fg='red', bg='skyblue', font=LARGEFONT).place(x=40, y=610)
        self.label = tk.Label(self, text="● +91-9326513775 ", fg='black', bg='skyblue', font=10).place(x=30, y=650)

        self.label = tk.Label(self, text="", font=40, bg="green", fg="white", borderwidth=0.2,
                              pady=330).place(x=330, y=50)

        button2 = ttk.Button(self, text="REQUEST AN APPOINTMENT",
                             command=lambda: controller.show_frame(Pateint), style="C.TButton")
        button2.place(x=810, y=620, width=220, height=50)


class patilINFO(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="skyblue")

        self.label = tk.Label(self, text="Dr.Mahesh Patil", font=40, bg="red", fg="white", borderwidth=5,
                              padx=530)
        self.label.place(x=0, y=5)
        tk.Button(self, text="⌂", bg='white', command=lambda: controller.show_frame(StartPage)).place(x=10, y=12)

        img = Image.open('mahesh.jpg')
        self.tkimage = ImageTk.PhotoImage(img)
        tk.Label(self, image=self.tkimage, bg='red').place(x=60, y=50)
        self.label = tk.Label(self, text="Dr.Mahesh Patil", bg='skyblue', font=LARGEFONT).place(x=80, y=290)
        self.label = tk.Label(self, text="Specializations :", fg='red', bg='skyblue', font=LARGEFONT).place(x=370, y=60)
        self.label = tk.Label(self, text="⏺   General Surgery ", fg='black', bg='skyblue', font=20).place(x=390, y=100)
        self.label = tk.Label(self, text="⏺   Consultant - Laparoscopic Surgery & General Surgery ", fg='black',
                              bg='skyblue', font=20).place(
            x=390, y=130)

        self.label = tk.Label(self, text="Qualification :", fg='red', bg='skyblue', font=LARGEFONT).place(x=370, y=200)
        self.label = tk.Label(self, text="⏺  MBBS", fg='black', bg='skyblue', font=20).place(x=390,
                                                                                             y=240)
        self.label = tk.Label(self, text="⏺   MS ", fg='black', bg='skyblue', font=20).place(x=390, y=270)

        self.label = tk.Label(self, text="Experience :", fg='red', bg='skyblue', font=LARGEFONT).place(x=370, y=320)
        self.label = tk.Label(self, text="⏺   2 Years Experience in General surgery ", fg='black',
                              bg='skyblue', font=20).place(x=390, y=360)

        self.label = tk.Label(self, text="Awards :", fg='red', bg='skyblue', font=LARGEFONT).place(x=370, y=500)
        self.label = tk.Label(self, text="⏺  Vice President Centra zone IAGES 2014-2018 ", fg='black', bg='skyblue',
                              font=20).place(
            x=390, y=540)
        self.label = tk.Label(self, text="⏺   Secretary Atysi From 2016 to Till  date. ", fg='black',
                              bg='skyblue', font=20).place(x=390, y=570)

        self.label = tk.Label(self, text="OPD :", fg='red', bg='skyblue', font=LARGEFONT).place(x=40, y=350)
        self.label = tk.Label(self, text="● Morning-(10AM-2PM)", fg='black', bg='skyblue', font=10).place(x=30, y=390)
        self.label = tk.Label(self, text="● Evening-(4PM-7PM)", fg='black', bg='skyblue', font=10).place(x=30,
                                                                                                         y=420)

        self.label = tk.Label(self, text="", font=40, bg="green", fg="white", borderwidth=0.2,
                              pady=330).place(x=330, y=50)
        self.label = tk.Label(self, text="COTACT :", fg='red', bg='skyblue', font=LARGEFONT).place(x=40, y=610)
        self.label = tk.Label(self, text="● +91-8754236978 ", fg='black', bg='skyblue', font=10).place(x=30, y=650)

        button2 = ttk.Button(self, text="REQUEST AN APPOINTMENT",
                             command=lambda: controller.show_frame(Pateint), style="C.TButton")
        button2.place(x=810, y=620, width=220, height=50)


class karadINFO(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="skyblue")

        self.label = tk.Label(self, text="Dr.Ganesh Karad", font=40, bg="red", fg="white", borderwidth=5,
                              padx=530)
        self.label.place(x=0, y=5)
        tk.Button(self, text="⌂", bg='white', command=lambda: controller.show_frame(StartPage)).place(x=10, y=12)

        img = Image.open('ganesh.jpg')
        self.tkimage = ImageTk.PhotoImage(img)
        tk.Label(self, image=self.tkimage, bg='red').place(x=60, y=50)
        self.label = tk.Label(self, text="Dr.Ganesh Karad", bg='skyblue', font=LARGEFONT).place(x=80, y=290)
        self.label = tk.Label(self, text="Specializations :", fg='red', bg='skyblue', font=LARGEFONT).place(x=370, y=60)
        self.label = tk.Label(self, text="⏺   Internal Medicine ", fg='black', bg='skyblue', font=20).place(x=390,
                                                                                                            y=100)
        self.label = tk.Label(self, text="⏺   Consultant - Internal Medicine ", fg='black', bg='skyblue',
                              font=20).place(
            x=390, y=130)

        self.label = tk.Label(self, text="Qualification :", fg='red', bg='skyblue', font=LARGEFONT).place(x=370, y=200)
        self.label = tk.Label(self, text="⏺   M.B.B.S. MGM Medical College, Indore ", fg='black', bg='skyblue',
                              font=20).place(x=390,
                                             y=240)
        self.label = tk.Label(self, text="⏺   M.D. Medicine MGM Medical College, Indore ", fg='black', bg='skyblue',
                              font=20).place(x=390, y=270)

        self.label = tk.Label(self, text="Experience :", fg='red', bg='skyblue', font=LARGEFONT).place(x=370, y=320)
        self.label = tk.Label(self, text="⏺   9 Years Clinical Experience ", fg='black',
                              bg='skyblue', font=20).place(x=390, y=360)

        self.label = tk.Label(self, text="Awards :", fg='red', bg='skyblue', font=LARGEFONT).place(x=370, y=500)
        self.label = tk.Label(self, text="⏺   Attended many conferences ", fg='black', bg='skyblue', font=20).place(
            x=390, y=540)

        self.label = tk.Label(self, text="OPD :", fg='red', bg='skyblue', font=LARGEFONT).place(x=40, y=350)

        self.label = tk.Label(self, text="OPD :", fg='red', bg='skyblue', font=LARGEFONT).place(x=40, y=350)
        self.label = tk.Label(self, text="● Morning-(10AM-2PM)", fg='black', bg='skyblue', font=10).place(x=30, y=390)
        self.label = tk.Label(self, text="● Evening-(4PM-7PM)", fg='black', bg='skyblue', font=10).place(x=30,
                                                                                                         y=420)

        self.label = tk.Label(self, text="COTACT :", fg='red', bg='skyblue', font=LARGEFONT).place(x=40, y=610)
        self.label = tk.Label(self, text="● +91-9821400548 ", fg='black', bg='skyblue', font=10).place(x=30, y=650)

        button2 = ttk.Button(self, text="REQUEST AN APPOINTMENT",
                             command=lambda: controller.show_frame(Pateint), style="C.TButton")
        button2.place(x=810, y=620, width=220, height=50)


class muleIINFO(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="skyblue")

        self.label = tk.Label(self, text="Dr.Anjali Mule", font=40, bg="red", fg="white", borderwidth=5,
                              padx=530)
        self.label.place(x=0, y=5)
        tk.Button(self, text="⌂", bg='white', command=lambda: controller.show_frame(StartPage)).place(x=10, y=12)

        img = Image.open('vijita.jpg')
        self.tkimage = ImageTk.PhotoImage(img)
        tk.Label(self, image=self.tkimage, bg='red').place(x=60, y=50)
        self.label = tk.Label(self, text="Dr.Anjali S Mule", bg='skyblue', font=LARGEFONT).place(x=80, y=290)
        self.label = tk.Label(self, text="Specializations :", fg='red', bg='skyblue', font=LARGEFONT).place(x=370, y=60)
        self.label = tk.Label(self, text="⏺   Chest Medicine ", fg='black', bg='skyblue', font=20).place(x=390, y=100)
        self.label = tk.Label(self, text="⏺   Consultant - Chest Physician ", fg='black', bg='skyblue', font=20).place(
            x=390, y=130)

        self.label = tk.Label(self, text="Qualification :", fg='red', bg='skyblue', font=LARGEFONT).place(x=370, y=200)
        self.label = tk.Label(self, text="⏺   M.D ( Chest & TB) ", fg='black', bg='skyblue', font=20).place(x=390,
                                                                                                            y=240)
        self.label = tk.Label(self, text="⏺   DNBE ", fg='black', bg='skyblue', font=20).place(x=390, y=270)

        self.label = tk.Label(self, text="Experience :", fg='red', bg='skyblue', font=LARGEFONT).place(x=370, y=320)
        self.label = tk.Label(self, text="⏺   Consultant Chest Physician at Jupiter Hospital ", fg='black',
                              bg='skyblue', font=20).place(x=390, y=360)
        self.label = tk.Label(self, text="⏺   Practising Chest Physician since 17years ", fg='black', bg='skyblue',
                              font=20).place(x=390, y=390)
        self.label = tk.Label(self, text="⏺   Ex-Honorary TB specialist and Unit head at GTB Hospital, Seweri ",
                              fg='black', bg='skyblue', font=20).place(x=390, y=420)
        self.label = tk.Label(self, text="⏺   Teaching experience of 9 years in Rajiv Gandhi Medical College ",
                              fg='black', bg='skyblue', font=20).place(x=390, y=450)

        self.label = tk.Label(self, text="Awards :", fg='red', bg='skyblue', font=LARGEFONT).place(x=370, y=500)
        self.label = tk.Label(self, text="⏺   Presented papers at SRSC ", fg='black', bg='skyblue', font=20).place(
            x=390, y=540)
        self.label = tk.Label(self, text="⏺   Management of MDR TB in resource limited setting in India. ", fg='black',
                              bg='skyblue', font=20).place(x=390, y=570)

        self.label = tk.Label(self, text="OPD :", fg='red', bg='skyblue', font=LARGEFONT).place(x=40, y=350)

        self.label = tk.Label(self, text="OPD :", fg='red', bg='skyblue', font=LARGEFONT).place(x=40, y=350)
        self.label = tk.Label(self, text="● Morning-(10AM-2PM)", fg='black', bg='skyblue', font=10).place(x=30, y=390)
        self.label = tk.Label(self, text="● Evening-(4PM-7PM)", fg='black', bg='skyblue', font=10).place(x=30,
                                                                                                         y=420)

        self.label = tk.Label(self, text="COTACT :", fg='red', bg='skyblue', font=LARGEFONT).place(x=40, y=610)
        self.label = tk.Label(self, text="● +91-7842513674 ", fg='black', bg='skyblue', font=10).place(x=30, y=650)

        self.label = tk.Label(self, text="", font=40, bg="green", fg="white", borderwidth=0.2,
                              pady=330).place(x=330, y=50)

        button2 = ttk.Button(self, text="REQUEST AN APPOINTMENT",
                             command=lambda: controller.show_frame(Pateint), style="C.TButton")
        button2.place(x=810, y=620, width=220, height=50)


if __name__ == "__main__":
    app = tkinterApp()
    app.geometry("1150x750")
    # app.maxsize(1150,750)
    app.minsize(1150, 750)
    app.title("CLINI MANAGMENT SYSTEM")
    app.iconbitmap(r'clinic.ico')
    app.mainloop()
