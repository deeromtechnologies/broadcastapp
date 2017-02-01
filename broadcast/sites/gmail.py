import smtplib

class Broadcast(object):
   def authentication(self,server):
      raise errors() 
   def sendmsg(self,message,server):
      raise errors()
class gmail(Broadcast):
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

    def sendmsg(self,server,username,toaddress,msg):
       server.sendmail(username,toaddress,msg)
       server.quit()

def mail(msg,key):
   username=key['from']
   pswd=key['pswd']
   toaddress=key['toaddr']
   mail_obj=gmail(username,pswd)
   server_obj=mail_obj.authentication()
   if server_obj:
      mail_obj.sendmsg(server_obj,username,toaddress,msg)
      return 'success'
   else:
      return 'fail'
   
