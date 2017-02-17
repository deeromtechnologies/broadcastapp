from sites import secret
from sites import broadcast


def broadcastMessage(message):
   key=secret.key
   
   broadcaststatus=broadcast.mail(message,key)
   return broadcaststatus
#   broadcaststatus=gmail.twit(message,key)
   
   
   
