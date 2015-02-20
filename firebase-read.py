#!/usr/local/bin/python2.7

from firebase import firebase

FIREBASE_URL = "https://dazzling-fire-5952.firebaseio.com/"

# Main
if __name__ == '__main__':
    fb = firebase.FirebaseApplication(FIREBASE_URL, None) # Create a reference to the Firebase Application

    result = fb.get('/PythonDemo', "Node1") # Get  data from firebase

    print("FB Data = %s" % result)
