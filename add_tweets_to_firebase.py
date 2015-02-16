from twitter import *
from firebase import  firebase
from chat import ClosableSSEClient
from multiprocessing import Process, Lock
from multiprocessing.sharedctypes import Value, Array
import time
import json
import twitter_config

roomId = "Room000001"
roomPath = "/Rooms/" + roomId 
tweetsPath = roomPath + "/Tweets"

def poll_tweets(s, ts, fb, track, tweetsPath):
	
	while(1) :
		track = s.value.decode(encoding='UTF-8')
		print("Get poll with track = %s" % (track))
		iterator = ts.statuses.filter(track = track)

		print("In poll_tweets starting iterator")
		for i in iterator:
			print(i)
			fb.post(tweetsPath, i)
			print("Posted to firebase \n")
			if (s.value.decode(encoding='UTF-8') != track):
				print("Tracking changed. Restart poll")
				break
	
def poll_target(s, url, label):
	print("In poll_target")
	sse = ClosableSSEClient("https://dazzling-fire-5952.firebaseio.com/Rooms/Room000001/Track.json")
	for t in sse:
		print("t is : " + t.data)
		t_data = json.loads(t.data)	
		print("t_data is : %s" % t_data)
		if t_data is None: # Keep alive
			continue
		s.value = t_data["data"].encode(encoding='UTF-8')
		print("Tracking set to - %s" % (s.value))
	
#Main
if __name__ == '__main__':
	lock = Lock()

	fb = firebase.FirebaseApplication("https://dazzling-fire-5952.firebaseio.com", None)
	ts = TwitterStream(auth = twitter_config.auth)

	track = fb.get(roomPath, "Track")
	s = Array('c', b'1234567890 1234567890 1234567890 1234567890 1234567890 1234567890 1234567890 1234567890 1234567890 1234567890 1234567890 1234567890 ', lock=lock)
	print("Setting s.value to %s" % (track))
	s.value = track.encode(encoding='UTF-8')
	
	t = Process(target=poll_target, args = (s, "https://dazzling-fire-5952.firebaseio.com/Rooms/Room000001/", "Track"))
	t.start()

	p = Process(target=poll_tweets, args = (s, ts, fb, track, tweetsPath))
	p.start()

