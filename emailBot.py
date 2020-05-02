import smtplib
import ssl

## Constant Port
port = 465
sender_email = "example@tcd.ie"
password = "password"
context = ssl.create_default_context()
server = smtplib.SMTP_SSL("smtp.gmail.com", port, context=context)

## logging into your own email
server.login(sender_email, password)

receiver_email = input("Enter the email address of the person you want send this to: ")
times_sent = input("Enter an amount of times you want to send it: ")
message = input("Enter a message you want to send to them: ")
print("Sending " + message + " to " + receiver_email + " " + times_sent + " times")
for i in range(0, int(times_sent)):
    message_sending = message + "\n \n \n \n \n \n " + "This is automated message " + (str(i) + 1) + " of " + times_sent
    server.sendmail(sender_email, receiver_email, message_sending)

print("done")
