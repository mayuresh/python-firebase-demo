from firebase import firebase

FIREBASE_URL = "https://dazzling-fire-5952.firebaseio.com/"

# Main
if __name__ == '__main__':

    fb = firebase.FirebaseApplication(FIREBASE_URL, None) # Create a reference to the Firebase Application

    data = raw_input("Input Data: ") # Get data from terminal

    fb.put('/PythonDemo/Node1', "Data", data) # Add data to Node Node1
