from sites import secret
from sites import gmail


def broadcastMessage(message):
   key=secret.key
   try:
      broadcaststatus=gmail.mail(message,key)
      return broadcaststatus
   except:
       return {}  
