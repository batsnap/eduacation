a=list(map(int,input().split()))
a.pop()
a.append()



import smtplib

server = 'smtp.gmail.com'
user = 'batkur@gmail.com'
password = '112001batyrovich'

recipients = ['batyrovich@mail.ru']
sender = 'batkur@gmail.com'
message = 'Hello World'

session = smtplib.SMTP_SSL(server,465)
# if your SMTP server doesn't need authentications,
# you don't need the following line:
session.login(user, password)
session.sendmail(sender, recipients, message)
session.close()
