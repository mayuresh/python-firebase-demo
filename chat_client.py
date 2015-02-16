from multiprocessing import Process
from firebase import firebase
from sseclient import SSEClient

FIREBASE_URL = "https://dazzling-fire-5952.firebaseio.com/"


def poll_chat():
    sse = SSEClient(FIREBASE_URL + "PythonChatDemo/Track.json")
    print("Watching Firebase node - %s" % (FIREBASE_URL + "PythonChatDemo/Track.json"))
    for t in sse:
        t_data = json.loads(t.data)
        if t_data is None:  # Keep alive
            continue

        if t_data["data"] is None:
            continue

        for (k, v) in t_data["data"].items():
            print("%s says: %s" % (k, v))

# Main
if __name__ == '__main__':

    # Start a thread to monitor changes to firebase
    t = Process(target=poll_chat)
    t.start()

    username = input("Input your name: ")
    fb = firebase.FirebaseApplication(FIREBASE_URL, None)

    # Post initial message to Firebase
    fb.post('/PythonChatDemo/Track', {username: "%s joined the chat" % (username)})


    # Post new messages to Firebase
    while (True):
        message = input("")
        fb.post('/PythonChatDemo/Track', {username: message})