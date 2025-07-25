import streamlit as st
import sqlite3
import hashlib

# Function to hash password
def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

# Function to check hashed password
def check_hashes(password, hashed_text):
    if make_hashes(password) == hashed_text:
        return hashed_text
    return False

# Database management
conn = sqlite3.connect('data.db')
c = conn.cursor()

# Function to create user table
def create_usertable():
    c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')

# Function to add user data
def add_userdata(username, password):
    c.execute('INSERT INTO userstable(username,password) VALUES (?,?)', (username, password))
    conn.commit()

# Function to login user
def login_user(username, password):
    c.execute('SELECT * FROM userstable WHERE username =? AND password = ?', (username, password))
    data = c.fetchall()
    return data

def login_page():
    st.subheader("Login Section")
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    if st.button("Login"):
        create_usertable()
        hashed_pswd = make_hashes(password)
        result = login_user(username, check_hashes(password, hashed_pswd))
        if result:
            st.session_state[f'{username}_{hashed_pswd}'] = {'logged_in': True}
            st.success("Logged In as {}".format(username))
        else:
            st.warning("Incorrect Username/Password")

def home_page():
    st.set_page_config(
        page_title='Home',
        page_icon='🏥',
    )
    st.title("Homepage")
    st.header('About Us')
    st.write('Welcome to M.E.D.I.C. We are committed to providing high-quality healthcare services to our users.')

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
    st.write("You are logged in.")  # Displayed only after successful login

def main():
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False
    
    if not st.session_state['logged_in']:
        login_page()
    else:
        home_page()

if __name__ == '__main__':
    main()
