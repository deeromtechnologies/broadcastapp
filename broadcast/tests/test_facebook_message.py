import Facebook
#def test_message_to_facebook():
 #   fb=Facebook()
  #  assert fb.message_sent==True
 
def test_facebook_post():
    A = Facebook.FaceBook()
    message = 'hello world'
    acknowledgement = A.facebook_post(message)
    assert acknowledgement is True
