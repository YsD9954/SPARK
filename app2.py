

import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
import os

# Initialize the ChatGoogleGenerativeAI instance
os.environ["GOOGLE_API_KEY"] = ""
llm = ChatGoogleGenerativeAI(model="gemini-1.0-pro")

from PIL import Image

# Load your image
image = Image.open(r"MedicLogo.png")  # Replace "your_image_path.jpg" with the path to your image file

# Display the image






st.image(image,  width=200)


def generate_diagnosis(age, gender, chief_complaint, past_medical_history, allergies, smoking_history, stress, exercise,
                       sleep_routine):
    """
    Generate the diagnosis based on the provided information.
    """
    query = f"A person's age is {age}. Their gender is {gender}. Their chief medical complaint is {chief_complaint}. Past medical history is {past_medical_history}. Allergies includes {allergies}. Smoking history is {smoking_history}. Stress due to occupation is {stress}. Exercise routine is {exercise}. Sleep routine is {sleep_routine}. Now guess the disease the person is suffering from and answer in the format-Disease,Details about the disease,Treatment and in the end give a disclaimer saying always consult professional medical help"
    result = llm.invoke(query)
    return result.content


# Streamlit app
def main():
    st.markdown("<h1 style='color:#095152;text-align:center;'>M.E.D.I.C.</h1>", unsafe_allow_html=True)

    # Collect user input
    age = st.number_input("Enter the person's age", min_value=0, max_value=150, step=1)
    gender = st.selectbox("Select the person's gender", ["Male", "Female", "Other"])
    chief_complaint = st.text_input("Enter the person's chief medical complaint")
    past_medical_history = st.text_input("Enter the person's past medical history")
    allergies = st.text_input("Enter the person's allergies")
    smoking_history = st.text_input("Enter the person's smoking history")
    stress = st.radio("Does the person experience stress due to occupation?", ("Yes", "No"))
    exercise = st.radio("Does the person exercise?", ("Yes", "No"))
    sleep_routine = st.slider("Enter the person's sleep routine (hours)", min_value=0, max_value=24, value=8, step=1)

    # Generate diagnosis
    if st.button("Generate Diagnosis"):
        diagnosis = generate_diagnosis(age, gender, chief_complaint, past_medical_history, allergies, smoking_history,
                                       stress, exercise, sleep_routine)
        st.write(diagnosis)

page_bg="""
<style>
[data-testid="stAppViewContainer"]
{
background-color: #7dd6d6;
}
</style>

<style>
[data-testid="stHeader"]
{
background-color: #7dd6d6;
}
</style>

<style>
[data-testid="stImage"]
        .center {
            display: block;
            margin-left: auto;
            margin-right: auto;
        }
    </style>
"""

st.markdown(page_bg,unsafe_allow_html=True)

if __name__ == "__main__":
    main()
