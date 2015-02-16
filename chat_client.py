from multiprocessing import Process
from firebase import  firebase
from sseclient import SSEClient
import time
import json

roomId = "Room000001"
roomPath = "/Rooms/" + roomId 
tweetsPath = roomPath + "/Tweets"

def poll_target():
	sse = SSEClient("https://dazzling-fire-5952.firebaseio.com/PythonChatDemo/Track.json")
	print("Watching Firebase node - %s" % ("https://dazzling-fire-5952.firebaseio.com/PythonChatDemo/Track.json"))
	for t in sse:
		t_data = json.loads(t.data)	
		if t_data is None: # Keep alive
			continue

		if t_data["data"] is None:
			continue
		
		for (k, v) in t_data["data"].items():
			print("%s says: %s" % (k, v))

#Main
if __name__ == '__main__':

	username = input("Input your name: ")
	fb = firebase.FirebaseApplication("https://dazzling-fire-5952.firebaseio.com/", None)

	fb.post('/PythonChatDemo/Track', {username: "%s joined the chat" % (username)})
	t = Process(target=poll_target)
	t.start()

	while(True):
		message = input("")
		fb.post('/PythonChatDemo/Track', {username: message})
