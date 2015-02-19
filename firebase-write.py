from firebase import firebase

FIREBASE_URL = "https://dazzling-fire-5952.firebaseio.com/"

# Main
if __name__ == '__main__':

    fb = firebase.FirebaseApplication(FIREBASE_URL, None) # Create a reference to the Firebase Application

    data = raw_input("Input Data: ") # Get data from terminal

    fb.post('/PythonDemo', {"Data": data}) # Post data to firebase
