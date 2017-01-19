import facebook
import requests

access_token="EAACEdEose0cBACfeZANohoqX8NsZCOCiE3d2wMKVscIcJvllrZASx5bZAhn5naZCeDUf3p7Fige1FsYoYYxx9nPIK5rrxNIqKIy4NlXzFaMxShPCD08Bc02WG9rlkCTu2iZBciWqriiPu7eBwzJVdZBTl9OGS03zTyzXTqALvOJfJnZBJJrums9YWNQnGV8aejgZD"
user_id="712018825585122"
class FaceBook:
    #def __init__(self, username, password):
     #   self.username = username
      #  self.password = password
        
    #def authenticate(self, username, password):
        
     #   return access_token

    def facebook_post(self, message):
        graph = facebook.GraphAPI(access_token)
        resp = graph.get_object(user_id)
        if (graph.put_wall_post(message)):
            acknw = True
            return acknw

    

    
