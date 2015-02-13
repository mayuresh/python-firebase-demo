from firebase import firebase
firebase = firebase.FirebaseApplication("https://dazzling-fire-5952.firebaseio.com/", None)

while(True):
	key = input("Input a key: ")
	value = input("Input a value: ")

	firebase.post('/PythonDemo/Track', {key: value})
	print("%s added to Firebase at %s\n" % ({key: value}, "https://dazzling-fire-5952.firebaseio.com/" + "/PythonDemo/Track"))
