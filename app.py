import streamlit as st
from langchain_core.messages import AIMessage,HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.document_loaders import WebBaseLoader
import getpass
import os
import pickle
from pathlib import Path
import streamlit_authenticator as stauth
import pandas as pd;



os.environ["GOOGLE_API_KEY"] = "AIzaSyD8rf2XNEHQGrWb4U2V9MzTUSZmvXrFJ38"





# app config
st.set_page_config(page_title="M.E.D.I.C", page_icon="logo.png")
st.title("M.E.D.I.C")

#-----------------USER AUTHENTICATION--------------------


#
# file_path = Path(__file__).parent / "hashed_pw.pkl"
# with file_path.open("rb") as file:
#     hashed_passwords = pickle.load(file)
#
# # Define user authentication parameters
# names = ["Peter Parker", "Rebecca Miller"]
# usernames = ["pparker", "rmiller"]
#
# # Initialize authentication
# authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
#                                     "M.E.D.I.C", "abcdef")
#
# # Attempt login
# names, authentication_status, usernames = authenticator.login("Login", "main")
#
# # Handle authentication status
# if authentication_status == False:
#     st.error("Username/password is incorrect")
# elif authentication_status == None:
#     st.warning("Please enter your username and password")
# else:





    # not working!!!!!111


# ---------------------------------------------------------------------
#
# import streamlit as st
# import firebase_admin
# from firebase_admin import firestore
# from firebase_admin import credentials
# from firebase_admin import auth
# import json
# import requests
#
# cred = credentials.Certificate("softies-1d56d-77a0938371d4.json")
# firebase_admin.initialize_app(cred)
#
#
# def app():
#     # Usernm = []
#     st.title('Welcome to M.E.D.I.C')
#
#     if 'username' not in st.session_state:
#         st.session_state.username = ''
#     if 'useremail' not in st.session_state:
#         st.session_state.useremail = ''
#
#     def sign_up_with_email_and_password(email, password, username=None, return_secure_token=True):
#         try:
#             rest_api_url = "https://identitytoolkit.googleapis.com/v1/accounts:signUp"
#             payload = {
#                 "email": email,
#                 "password": password,
#                 "returnSecureToken": return_secure_token
#             }
#             if username:
#                 payload["displayName"] = username
#             payload = json.dumps(payload)
#             r = requests.post(rest_api_url, params={"key": "AIzaSyApr-etDzcGcsVcmaw7R7rPxx3A09as7uw"}, data=payload)
#             try:
#                 return r.json()['email']
#             except:
#                 st.warning(r.json())
#         except Exception as e:
#             st.warning(f'Signup failed: {e}')
#
#     def sign_in_with_email_and_password(email=None, password=None, return_secure_token=True):
#         rest_api_url = "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword"
#
#         try:
#             payload = {
#                 "returnSecureToken": return_secure_token
#             }
#             if email:
#                 payload["email"] = email
#             if password:
#                 payload["password"] = password
#             payload = json.dumps(payload)
#             print('payload sigin', payload)
#             r = requests.post(rest_api_url, params={"key": "AIzaSyApr-etDzcGcsVcmaw7R7rPxx3A09as7uw"}, data=payload)
#             try:
#                 data = r.json()
#                 user_info = {
#                     'email': data['email'],
#                     'username': data.get('displayName')  # Retrieve username if available
#                 }
#                 return user_info
#             except:
#                 st.warning(data)
#         except Exception as e:
#             st.warning(f'Signin failed: {e}')
#
#     def reset_password(email):
#         try:
#             rest_api_url = "https://identitytoolkit.googleapis.com/v1/accounts:sendOobCode"
#             payload = {
#                 "email": email,
#                 "requestType": "PASSWORD_RESET"
#             }
#             payload = json.dumps(payload)
#             r = requests.post(rest_api_url, params={"key": "AIzaSyApr-etDzcGcsVcmaw7R7rPxx3A09as7uw"}, data=payload)
#             if r.status_code == 200:
#                 return True, "Reset email Sent"
#             else:
#                 # Handle error response
#                 error_message = r.json().get('error', {}).get('message')
#                 return False, error_message
#         except Exception as e:
#             return False, str(e)
#
#     # Example usage
#     # email = "example@example.com"
#
#     def f():
#         try:
#             # user = auth.get_user_by_email(email)
#             # print(user.uid)
#             # st.session_state.username = user.uid
#             # st.session_state.useremail = user.email
#
#             userinfo = sign_in_with_email_and_password(st.session_state.email_input, st.session_state.password_input)
#             st.session_state.username = userinfo['username']
#             st.session_state.useremail = userinfo['email']
#
#             global Usernm
#             Usernm = (userinfo['username'])
#
#             st.session_state.signedout = True
#             st.session_state.signout = True
#
#
#         except:
#             st.warning('Login Failed')
#
#     def t():
#         st.session_state.signout = False
#         st.session_state.signedout = False
#         st.session_state.username = ''
#
#     def forget():
#         email = st.text_input('Email')
#         if st.button('Send Reset Link'):
#             print(email)
#             success, message = reset_password(email)
#             if success:
#                 st.success("Password reset email sent successfully.")
#             else:
#                 st.warning(f"Password reset failed: {message}")
#
#     if "signedout" not in st.session_state:
#         st.session_state["signedout"] = False
#     if 'signout' not in st.session_state:
#         st.session_state['signout'] = False
#
#     if not st.session_state["signedout"]:  # only show if the state is False, hence the button has never been clicked
#         choice = st.selectbox('Login/Signup', ['Login', 'Sign up'])
#         email = st.text_input('Email Address')
#         password = st.text_input('Password', type='password')
#         st.session_state.email_input = email
#         st.session_state.password_input = password
#
#         if choice == 'Sign up':
#             username = st.text_input("Enter  your unique username")
#
#             if st.button('Create my account'):
#                 # user = auth.create_user(email = email, password = password,uid=username)
#                 user = sign_up_with_email_and_password(email=email, password=password, username=username)
#
#                 st.success('Account created successfully!')
#                 st.markdown('Please Login using your email and password')
#                 st.balloons()
#         else:
#             # st.button('Login', on_click=f)
#             st.button('Login', on_click=f)
#             # if st.button('Forget'):
#             forget()
#             # st.button('Forget',on_click=forget)
#
#     if st.session_state.signout:
#         st.text('Name ' + st.session_state.username)
#         st.text('Email id: ' + st.session_state.useremail)
#         st.button('Sign out', on_click=t)
#
#     def ap():
#         st.write('Posts')
#
#
#
#
#
#
#
#
#
#






# --------------------------------------------------------------------

# USING SQL...............

# -------------------------------------------------------------------

import streamlit as st
import pandas as pd


# Security
#passlib,hashlib,bcrypt,scrypt
import hashlib
def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False
# DB Management


import sqlite3
conn = sqlite3.connect('data.db')
c = conn.cursor()
# DB  Functions
def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')


def add_userdata(username,password):
	c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
	conn.commit()

def login_user(username,password):
	c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
	data = c.fetchall()
	return data


def view_all_users():
	c.execute('SELECT * FROM userstable')
	data = c.fetchall()
	return data



def main():
	"""Simple Login App"""


	menu = ["Home","Login","SignUp"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Home":
		st.subheader("Home")

	elif choice == "Login":
		st.subheader("Login Section")

		username = st.sidebar.text_input("User Name")
		password = st.sidebar.text_input("Password",type='password')
		if st.sidebar.checkbox("Login"):
			# if password == '12345':
			create_usertable()
			hashed_pswd = make_hashes(password)

			result = login_user(username,check_hashes(password,hashed_pswd))
			if result:

				st.success("Logged In as {}".format(username))


# #m MWKO SABKO NHI DIKHANA DATA!!!!!!!!!!!!!!!!
#
# 				# task = st.selectbox("Task",["Add Post","Analytics","Profiles"])
# 				# if task == "Add Post":
# 				# 	st.subheader("Add Your Post")
# 				#
# 				# elif task == "Analytics":
# 				# 	st.subheader("Analytics")
# 				# elif task == "Profiles":
# 				# 	st.subheader("User Profiles")
# 				# 	user_result = view_all_users()
# 				# 	clean_db = pd.DataFrame(user_result,columns=["Username","Password"])
# 				# 	st.dataframe(clean_db)
#


			else:
				st.warning("Incorrect Username/Password")





	elif choice == "SignUp":
		st.subheader("Create New Account")
		new_user = st.text_input("Username")
		new_password = st.text_input("Password",type='password')

		if st.button("Signup"):
			create_usertable()
			add_userdata(new_user,make_hashes(new_password))
			st.success("You have successfully created a valid Account")
			st.info("Go to Login Menu to login")





# # ---------------------------------------------------------
# # FOR DB MANAGEMENT tp !!!!!!!!!!!!!!!
#
# #
# #
# # import sqlite3
# # import pandas as pd
# #
# # # Connect to SQLite database
# # conn = sqlite3.connect('D:\APNA ANDROID\MEDIC\data.db')  # Replace 'path_to_website_database.db' with the actual path to the .db file
# #
# # # Write SQL query to extract data
# # query = "SELECT * FROM your_table"  # Replace 'your_table' with the name of the table containing the data you want to export
# #
# # # Convert query result to DataFrame
# # df = pd.read_sql_query(query, conn)
# #
# # # Close database connection
# # conn.close()
# #
# # # Export DataFrame to Excel
# # df.to_excel('output.xlsx', index=False)  # Replace 'output.xlsx' with the desired name for the Excel file
#
# # ---------------------------------------------------------
# #-------------------------------------------
#
#
#
#
#

if __name__ == '__main__':
    main()

# # ---------------------------------------------------












#
#
#
# from flask import Flask, render_template, request, redirect, session
# import sqlite3
#
# app = Flask(__name__)
# app.secret_key = 'ysd9954'  # Change this to a random secret key
#
# # Database setup
# conn = sqlite3.connect('users.db')
# cursor = conn.cursor()
# cursor.execute('''CREATE TABLE IF NOT EXISTS users (
#                     id INTEGER PRIMARY KEY,
#                     username TEXT UNIQUE,
#                     password TEXT,
#                     first_login INTEGER DEFAULT 1
#                 )''')
# conn.commit()
# conn.close()
#
# # Registration
# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         conn = sqlite3.connect('users.db')
#         cursor = conn.cursor()
#         cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
#         conn.commit()
#         conn.close()
#         return redirect('/login')
#     return render_template('register.html')
#
# # Login
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         conn = sqlite3.connect('users.db')
#         cursor = conn.cursor()
#         cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
#         user = cursor.fetchone()
#         conn.close()
#         if user:
#             session['username'] = username
#             if user[3] == 1:  # Check if first login is required
#                 return redirect('/first_login')
#             else:
#                 return redirect('/dashboard')
#         else:
#             return "Invalid username or password"
#     return render_template('login.html')
#
# # First Login Process
# @app.route('/first_login', methods=['GET', 'POST'])
# def first_login():
#     if 'username' not in session:
#         return redirect('/login')
#     if request.method == 'POST':
#         # Perform actions for first login process
#         username = session['username']
#         # Update user's first login status in the database
#         conn = sqlite3.connect('users.db')
#         cursor = conn.cursor()
#         cursor.execute("UPDATE users SET first_login=0 WHERE username=?", (username,))
#         conn.commit()
#         conn.close()
#         return redirect('/dashboard')
#     return render_template('first_login.html')
#
# # Dashboard
# @app.route('/dashboard')
# def dashboard():
#     if 'username' not in session:
#         return redirect('/login')
#     return f"Welcome to the dashboard, {session['username']}!"





















# ------------------------------------------------------------------





















def get_response(user_input):
    loader = WebBaseLoader("https://www.ndtv.com/")
    docs = loader.load()
    llm = ChatGoogleGenerativeAI(model="gemini-1.0-pro")
    result = llm.invoke(user_input)
    return result





#sidebar




with st.sidebar:



    st.header("Enter Your Details")
    user_age = st.text_input("Age")
    user_gender = st.radio("Gender",["Male","Female","Other"])

if user_age is None or user_age == "":
    st.info("Please enter your age")
else:
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = [
            AIMessage(content="Hello I am M.E.D.I.C. Your personal healthcare assistant")
        ]
    #user-input
    user_query = st.chat_input("What ails you my love...")

    if user_query is not None and user_query!="":
        response = get_response(user_query)
        st.session_state.chat_history.append(HumanMessage(content=user_query))
        st.session_state.chat_history.append(AIMessage(content=response.content))

    #conversation
    for message in st.session_state.chat_history:
        if isinstance(message, AIMessage):
            with st.chat_message("🩺"):
                st.write(message.content)
        elif isinstance(message, HumanMessage):
            with st.chat_message("HUMAN"):
                st.write(message.content)



#
# def set_background():
#
#     st.markdown(
#         """
#         <style>
#         .reportview-container {
#             background: url("background.jpg") no-repeat center center fixed;
#             background-size: cover;
#         }
#         </style>
#         """,
#         unsafe_allow_html=True,
#     )


# not working above backgroubnd!!!!!!!!!


def set_background_image(image_url):
    page_bg_img = '''
    <style>
    body {
    background-image: url("''' + image_url + '''");
    background-size: cover;
    }
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)


def main():
    set_background_image('background.jpg')


    st.header('About Us')
    st.write(
        'Welcome to M.E.D.I.C  We are committed to providing high-quality healthcare services to our users.')

    st.header('Our Services')
    st.write("""
    - Primary Care
    - Specialized Treatments
    - Preventive Care
    - Emergency Services
    """)

    st.header('Contact Us')
    st.write("""
    If you have any questions or would like to schedule an appointment, please contact us at:

    Email: info@medicalhealth.com
    
    Phone: 123-456-7890
    
    Address: Mumbai, India
    """)


if __name__ == '__main__':
    main()
