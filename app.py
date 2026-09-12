import streamlit as st
import pickle

model = pickle.load(open("spam_model.pkl", "rb"))

st.title("📩 Spam Message Classifier")

message = st.text_area("Enter your message")

if st.button("Predict"):
    if message.strip() == "":
        st.warning("Please enter a message.")
    else:
        prediction = model.predict([message])[0]

        if prediction == 1:
            st.error("🚨 This is SPAM")
        else:
            st.success("✅ This is HAM")