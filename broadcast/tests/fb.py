import facebook

def main():
  # Fill in the values noted in previous steps here
  cfg = {
    "page_id"      : "712018825585122",  # Step 1
    "access_token" : "EAACEdEose0cBAOyi8d16kPmwXIzQZBSgLroKkYyeijFPczUgernZANZCglcBpub8grWZCo6PL6md8kzKNsAnBZBYhl4H2tj93ozZCYPhSFVW1coTd2xhrTAcBQ21SVjEOdWx90c281ZCFwLRk13qx1r5oilrCxUc8K6ZBP0Wg7ww2m3eZAZB7t3Vyof0dcclpP7FMZD"  
    }

  api = get_api(cfg)
  msg = "Hello, world!"
  status = api.put_wall_post(msg)

def get_api(cfg):
  graph = facebook.GraphAPI(cfg['access_token'])
  # Get page token to post as the page. You can skip 
  # the following if you want to post as yourself. 
  resp = graph.get_object('me/accounts')
  page_access_token = None
  for page in resp['data']:
    if page['id'] == cfg['page_id']:
      page_access_token = page['access_token']
  graph = facebook.GraphAPI(page_access_token)
  return graph
if __name__ == "__main__":
  main()
