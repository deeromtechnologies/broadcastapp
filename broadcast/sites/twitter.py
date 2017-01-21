import tweepy

consumer_key="1VJ1GSRUdhrFmDzix04adrBrB"
access_token="819759837898801152-ZcIJgHCJImmBUnrM9iRFM7J3RSNV4yn"
consumer_secret="Xreq2PQDpMgrSc6VONBdYeiwFXT9fBYZOPFaMhfHoOQSHniqyp"       
access_token_secret="DSPTCri6L51AecjsJCG1ThazxOts2imxkbzBFticZHhWN"

def get_api(cfg):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return tweepy.API(auth)
