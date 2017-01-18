import smtplib
class gmail:
    def __init__(self,username,pswd,msg):
       self.username=username
       self.pswd=pswd
       self.msg=msg
    def authentication(self,server):
      # server=smtplib.SMTP('smtp.gmail.com',587)
       server.starttls()
       server.login(self.username,self.pswd)
    def messagebro(self,server):
       server.sendmail(self.msg)
       server.quit()

       
