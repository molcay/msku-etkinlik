# -*- coding: utf-8 -*-

from twython import Twython

APP_KEY = '0AwQb39K8mcVG79XIM8LRCV5f'
APP_SECRET = 'JxGnVU9bc9rhYHqKWX0vUugBfP4BoWvXrTtCc2lz9tRHvTbYiw'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()
print ACCESS_TOKEN

twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)
result = twitter.search(q='Garanti', count='100', lang='tr')

print result['search_metadata']

usernames = []
for i,tweet in enumerate(result['statuses']):
  print "[%d] Text : %s" % (i+1,tweet['text'].encode("utf-8"))
  """print "Tags : %s" % tweet['entities']['hashtags']
  print "URLS : %s" % tweet['entities']['urls']
  print "User : %s" % tweet['user']['name']
  print "link : https://twitter.com/%s/status/%s\n\n" % (tweet['user']['screen_name'], tweet['id_str'])"""
  usernames.append(tweet['user']['id_str'])
print ",".join(usernames)  
result_users = twitter.lookup_user(user_id=",".join(usernames))   
# print result_users

for i,user in enumerate(result_users):
   pass
   # print "%d. %s: %s" % (i+1, user['name'], user['description'])
