import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP_SSL("smtp.gmail.com") #my server i'm using to send the email
server.ehlo()
server.ehlo()

#loop that allows you to send multiple emails if you wish
true = True
while true:
    emailIN = input("Enter your email address you want to use to send the message: ")
    password = input("Enter the app password for the email: ")

    server.login(emailIN, password) #logs into the email

    Head = input("Enter who you sending this message from: ")
    emailOut = input("Enter your email address you want to send the message to: ")
    subject = input("Enter the message you want to send in the email: ")

    #the message formating
    msg = MIMEMultipart()
    msg['From'] = Head     
    msg['To'] = emailOut
    msg['Subject'] = subject

    # with open('message.txt', 'r') as f:
    message = input("Enter the message you wish to send to the person: ")
    msg.attach(MIMEText(message, 'plain'))

    #if you wish to send a picture as well
    pic = input("Do you wish to send a picture with the email? y/n ")
    if pic == 'y':
        print("To send a picture you need to place the picture into this folder")
        picName = input("Please enter the name of the picture including what type it is: ")
        filename = picName
        attachment = open(filename, 'rb')
        #attaches the picture
        p = MIMEBase('application', 'octet-stream')
        p.set_payload(attachment.read())

        encoders.encode_base64(p)
        p.add_header('Content-Disposition', f'attachment; filename={filename}')
        msg.attach(p)
    
    text = msg.as_string()
    server.sendmail('speedkingc18@gmail.com', 'mcc18040@byui.edu', text) #sends the email
    print("message sent:)")
    again = input("if you wish to send another message enter y if you want to exit out hit q ")
    if again == 'q': #allows you to exit the program when done if you wish
        true = False
    