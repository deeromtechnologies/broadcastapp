def test_message_to_facebook():
    fb=Facebook()
    assert fb.message_sent==True
