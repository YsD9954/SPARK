import pickle
from pathlib import Path
import bcrypt
import streamlit_authenticator as stauth

names = ["Peter Parker", "Rebecca Miller"]
usernames = ["pparker", "rmiller"]
passwords = ["XXX", "XXX"]

hashed_passwords = [bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()) for password in passwords]

file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)