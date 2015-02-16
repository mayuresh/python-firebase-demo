from twitter import *
from firebase import  firebase
from sseclient import SSEClient
import time
import json

roomId = "Room000001"
roomPath = "/Rooms/" + roomId 
tweetsPath = roomPath + "/Tweets"

def poll_target():
	sse = SSEClient("https://dazzling-fire-5952.firebaseio.com/PythonDemo/Track.json")
	print("Watchin Firebase node - %s" % ("https://dazzling-fire-5952.firebaseio.com/PythonDemo/Track.json"))
	for t in sse:
		print("Data changed !")
		t_data = json.loads(t.data)	
		if t_data is None: # Keep alive
			continue
		
		for (k,v) in t_data["data"].items():
			print("Key = %s, Value = %s" % (k, v))

#Main
if __name__ == '__main__':
	poll_target()
