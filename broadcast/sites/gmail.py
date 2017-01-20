import smtplib
class gmail:
    def __init__(self,username,pswd):
       self.username=username
       self.pswd=pswd
<<<<<<< HEAD
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
   
=======
    def authentication(self,server):
       server.starttls()
       server.login(self.username,self.pswd)
       return "success"
    def messagebro(self):
       server.sendmail(self,msg)
       server.quit()

def mail(message):
   username="studio4g4@gmail.com"
   pswd="9633206869"
   txt=message
   m=gmail(username,pswd)
   server=smtplib.SMTP('smtp.gmail.com',587)       
   try:
      login=m.authentication(server)
      if login=="success":
         send= m.messagebro(txt)
      else: 
         send="fail"
      return send
   except:
      return "authentication failed"

>>>>>>> b1df9d4b3a846b0c3bf3154e31880bafaba3a613
