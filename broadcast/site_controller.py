from sites import secret
from sites import gmail


def broadcastMessage(message):
   key=secret.key
   broadcaststatus=gmail.mail(message,key)
   return broadcaststatus
   broadcaststatus=gmail.twit(message,key)
   
   
   
