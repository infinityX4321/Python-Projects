# Python code to illustrate Sending mail from
# your Gmail account
import smtplib

# creates SMTP session
s = smtplib.SMTP('smtp.outlook.com', 587)

# start TLS for security
s.starttls()

# Authentication
#s.login("rsveanand@outlook.com", "password")
# message to be sent
message = "hello kunal"

# sending the mail
s.sendmail("kunalsingh754prime@outlook.com", "rsveanand@outlook.com", message)
#s.sendmail("rsveanand@gmail.com", "rsveanand@gmail.com", message)
# terminating the session
s.quit()
