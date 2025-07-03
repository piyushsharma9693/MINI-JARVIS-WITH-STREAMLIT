import streamlit as st
from gtts import gTTS
import datetime
import os

# Text-to-speech function
def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save("output.mp3")
    audio_file = open("output.mp3", "rb")
    st.audio(audio_file.read(), format="audio/mp3")
    audio_file.close()
    os.remove("output.mp3")

# Greeting function
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        greeting = "Good morning!"
    elif 12 <= hour < 18:
        greeting = "Good afternoon!"
    else:
        greeting = "Good evening!"
    speak(greeting)
    return f"{greeting} I am your assistant. How can I help you?"

# Streamlit App
st.title("🧠 Mini Jarvis - Deployment Version")
st.write("Type your command below:")

if st.button("🤖 Greet Me"):
    wish_text = wishMe()
    st.success(wish_text)

query1 = st.text_input("💬 Enter your command:")

if query1:
    st.write(f"🗣 You typed: {query1}")

    if 'time' in query1.lower():
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        response = f"The current time is {current_time}"
        speak(response)
        st.success(response)

    elif 'exit' in query1.lower() or 'stop' in query1.lower():
        speak("Goodbye!")
        st.warning("Assistant stopped.")

    else:
        response = "I didn't understand that. Please try again."
        speak(response)
        st.error(response)
