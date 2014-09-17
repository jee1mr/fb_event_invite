import urllib2
import sys
import json
access = str(sys.argv[1])

req = urllib2.Request('https://graph.facebook.com/me/friends?&access_token='+access)

response = urllib2.urlopen(req)

friends = response.read()

f = open('fb_friends.json','w') 

f.write(friends)

f.close()
json_data=open('fb_friends.json')

data = json.load(json_data)

num_of_friends= int(len(data["data"]))


f= open('fb_invite','w')

event_id = str(sys.argv[2])

invite_url = "https://graph.facebook.com/v1.0/"+event_id+"/invited?users="
arr=""

for i in range(0,num_of_friends):
	arr=str(data["data"][i]["id"])+","+str(arr)	


fullurl= invite_url+arr+"&&access_token="+str(access)	

req = urllib2.Request(fullurl)


