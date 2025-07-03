import streamlit as st
import speech_recognition as sr
from gtts import gTTS
import datetime
import os

# Text-to-speech function using gTTS and Streamlit audio
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

# Speech recognition function
def takeCommand():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Listening...")
        audio = recognizer.listen(source)

    try:
        st.info("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        return query
    except Exception:
        return "Sorry, I didn't catch that. Please try again."

# Streamlit App
st.title("🧠 Mini Jarvis - Voice Assistant")
st.write("Click the button and speak your command.")

if st.button("🎙 Start Listening"):
    wish_text = wishMe()
    st.success(wish_text)
    query1 = takeCommand()
    st.write(f"🗣 You said: {query1}")

    if 'time' in query1:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        response = f"The current time is {current_time}"
        speak(response)
        st.success(response)

    elif 'exit' in query1 or 'stop' in query1:
        speak("Goodbye!")
        st.warning("Assistant stopped.")

    else:
        response = "I didn't understand that. Please try again."
        speak(response)
        st.error(response)
