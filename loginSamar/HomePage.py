import streamlit as st

st.set_page_config(
    page_title = 'Home',
    page_icon = '🏥',
    )
l,m,r = st.columns(3)

st.title("Homepage")
st.header('About Us')
st.write('Welcome to M.E.D.I.C  We are committed to providing high-quality healthcare services to our users.')

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
st.link_button("Login",'http://localhost:8501')
st.link_button("Sign up",'')


