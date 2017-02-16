import facebook
import requests


class FaceBook():

    def __init__(self,access_token):
        self.access_token = access_token
        

    def authentication(self):
        graph = facebook.GraphAPI(self.access_token)
        return graph
    
    def sendmsg(self, message,server):
        if (server.put_wall_post(message)):
            success = True
            return success 
def fbmessage(message):
    access_token = "EAACEdEose0cBAOcTOPrs5sTxvuVS8LS6m8v8KPnhTtXNAW9e7oCCMenZC8sS5UT4paJYyrVucFZCHcNWvDGmUMr9SWqqLqlaB6DF8cb4wpaVRFNdXptiRZCqVHylzjFBeFZCq7hVZCZBA13W6Deg2pqwLBfuLUe9Fn3zWWllSObvx2ZCvbydgpIIdFWApumkIoZD"
    fb=FaceBook(access_token)
    server=fb.authentication()
    status=fb.sendmsg(message,server)
    return status
    

    
