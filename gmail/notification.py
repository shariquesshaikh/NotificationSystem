import smtplib

server = smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()
server.ehlo()

#search less secure apps on chrome browser and on less secure apps permission page enable permission for sender_email_address
server.login('sender_email_address','sender_email_password')  

subject = "subject"
body= "body"
msg=f"Subject: {subject}\n\n{body} "

server.sendmail(
    'sender_email_address',
    'receiver_email_address',
    msg
    )

server.quit()
