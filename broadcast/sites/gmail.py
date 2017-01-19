import smtplib
class gmail:
    def __init__(self,username,pswd):
       self.username=username
       self.pswd=pswd
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

