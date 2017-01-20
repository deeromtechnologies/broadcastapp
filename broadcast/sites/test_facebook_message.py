import Facebook

def test_facebook_post():
    A = Facebook.FaceBook()
    message = 'hello world'
    respose = A.facebook_post(message)
    assert response is True
