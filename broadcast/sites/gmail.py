import smtplib
import tweepy
class BroadcastError(Exception):
     pass
class AuthenticationError(Exception):
     pass
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
       except AuthenticationError as exceptn:
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
   
class Twitter(Broadcast):
     def __init__(self,consumer_key,consumer_secret,access_token,access_token_secret):
            self.consumer_key=consumer_key
            self.consumer_secret=consumer_secret
            self.access_token=access_token
            self.access_token_secret=access_token_secret
     def authentication(self):
            auth=tweepy.Authentication(self.consumer_key,self.consumer_secret)
            auth.set_access_token(self.access_token,self.access_token_secret)
            api=tweepy.API(auth)
            return api
     def sendmsg(self,message,server):
           try:
               server.update_status(status=message)
           except tweepy.TweepError as e:
               raise BroadcastError()
def twit(message,key):
    consumer_key=key['consumer_key']
    consumer_secret=key['consumer_secret']
    access_token=key['access_token']
    access_token_secret=key['access_token_secret']
    twitter=Twitter(consumer_key,consumer_secret,access_token,access_token_secret)
    server=twitter.authentication()
    status=twitter.sendmsg(message,server)
    return status

