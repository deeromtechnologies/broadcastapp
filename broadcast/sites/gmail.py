import smtplib
class gmail:
    def __init__(self,username,pswd):
       self.username=username
       self.pswd=pswd
    def authentication(self):
       server=smtplib.SMTP('smtp.gmail.com',587)
       server.starttls()
       try:
          server.login(self.username,self.pswd)
          return server
       except smtplib.SMTPAuthenticationError:
          return None

    def messagebro(self,server,username,toaddress,msg):
       server.sendmail(username,toaddress,msg)
       server.quit()

def mail(msg,toaddress):
   username="testmailcalicut@gmail.com"
   pswd="asdasdqwe"
   mail_obj=gmail(username,pswd)
   server_obj=mail_obj.authentication()
   if server_obj:
      mail_obj.messagebro(server_obj,username,toaddress,msg)
      return 'success'
   else:
      return 'fail'
   
