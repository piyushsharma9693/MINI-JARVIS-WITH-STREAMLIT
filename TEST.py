import speech_recognition as sr
from gtts import gTTS
import datetime
import playsound
import os

# Function to convert text to speech
def speak(text):
    tts = gTTS(text=text, lang='en')
    filename = "output.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

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

# Function to take microphone input and return as text
def takeCommand():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"You said: {query}")
        return query
    except Exception as e:
        print("Sorry, I didn't catch that. Please try again.")
        return "None"

# Main program
if __name__ == "__main__":
    wish_text = wishMe()
    print(wish_text)

    while True:
        query1 =
