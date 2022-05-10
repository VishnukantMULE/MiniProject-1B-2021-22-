import smtplib
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
import mysql

import main
import imghdr
from email.message import EmailMessage

def sendmailforpdf():
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
    Sender_Email = "vishnukantmule@gmail.com"
    Reciever_Email = useremailget
    Password = "cgezqyarhsxghdfy"

    newMessage = EmailMessage()
    newMessage['Subject'] = "PATEINT APPOINTMENT PDF"
    newMessage['From'] = Sender_Email
    newMessage['To'] = Reciever_Email
    newMessage.set_content('Caring for the whole patient, not just your symptoms')

    files = ['ClinicManagementSystem.pdf']

    for file in files:
        with open(file, 'rb') as f:
            file_data = f.read()
            file_name = f.name
        newMessage.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(Sender_Email, Password)
        smtp.send_message(newMessage)
