from multiprocessing import Process
from firebase import firebase
from sseclient import SSEClient
import json

FIREBASE_URL = "https://dazzling-fire-5952.firebaseio.com/"


def poll_chat():
    sse = SSEClient(FIREBASE_URL + "PythonChatDemo/Track.json")
    print("Watching Firebase node - %s" % (FIREBASE_URL + "PythonChatDemo/Track.json"))

    for new_message in sse:
        message_data = json.loads(new_message.data)

        if message_data is None:  # Keep alive
            continue

        if message_data["data"] is None:
            continue

        if message_data["path"] == "/": # Initial Read for old messages
            print("Previous messages")
            for (nodeid, message_dict) in message_data["data"].items():
                #print("nodeid: %s, message_dict: %s" % (nodeid, message_dict))
                for (name, message) in message_dict.items():
                    print("%s says: %s" % (name, message))

        else: # New Message
            for (name, message) in message_data["data"].items():
                print("%s says: %s" % (name, message))

# Main
if __name__ == '__main__':

    # Start a thread to monitor changes to firebase
    t = Process(target=poll_chat)
    t.start()

    username = input("Input your name: ")
    fb = firebase.FirebaseApplication(FIREBASE_URL, None)

    # Post initial message to Firebase
    fb.post('/PythonChatDemo/Track', {username: "Joined the chat"})

    # Post new messages to Firebase
    while (True):
        message = input("")
        fb.post('/PythonChatDemo/Track', {username: message})