import smtplib
import ssl

port = 465

password = "paassword"

context = ssl.create_default_context()

server = smtplib.SMTP_SSL("smtp.gmail.com", port, context=context)
server.login("address@gmail.com", password)

sender_email = "address@gmail.com"
receiver_email = "address1@gmail.com"
message = "hello world!"

server.sendmail(sender_email, receiver_email, message)
print("done")
