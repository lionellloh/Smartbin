import pyrebase
# Get the below information from Authentication > Web Set Up
config = {
  "apiKey": "AIzaSyCjAuz7jFaiGjpn1045aPGrqPqllWuOZto",
  "authDomain": "dw-iot-965fa.firebaseapp.com",
  "databaseURL": "https://dw-iot-965fa.firebaseio.com/",
  "storageBucket": "dw-iot-965fa.appspot.com",
  "serviceAccount": "./dw-iot-965fa-firebase-adminsdk-nqcyu-cb26baf829.json"
}
firebase = pyrebase.initialize_app(config)

# The default permissions of a Firebase database requires authentication to perform read or write actions.
# The simplest way to authenticate is by signing
# in with an email and password. A new user can be created in the Auth tab of the Firebase console.
# Once a user is created, the following Pyrebase code can be used to created an authentication connection:

# Three types of services - 1. Authentication, 2. Database and 3. Storage
auth = firebase.auth()
user = auth.sign_in_with_email_and_password("lionellloh@gmail.com", "lionell")

token = (user['idToken'])

# Main functionalities of a database interface are the abilities
# to Create, Read, Update, and Delete data.

db = firebase.database()
archer = {"name": "John Archer", "agency": "Figgis Agency"}
db.child("agents").push(archer, user['idToken'])
db.child("agents").set(archer, user['idToken'])

all_agents = db.child().get(user['idToken']).val()
print(all_agents)
