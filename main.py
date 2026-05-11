import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests
from openai import OpenAI
import pygame
from gtts import gTTS
import os





recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "yourapi"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3') 

    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("temp.mp3") 

def aiProcess(command):
    client = OpenAI(api_key="yourapi",
    )

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named assistance skilled in general tasks like Alexa and Google Cloud. Give short responses please"},
        {"role": "user", "content": command}
    ]
    )
    return completion.choices[0].message.content

def process_command(command):
    if "open youtube" in command.lower():
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube.")
    elif "open google" in command.lower()   :
        webbrowser.open("https://www.google.com")
        speak("Opening Google.")
    elif "open linkedin" in command.lower():
        webbrowser.open("https://linkedin.com")
        speak("Opening LinkedIn.")
    elif "open facebook" in command.lower():
        webbrowser.open("https://facebook.com")
        speak("Opening Facebook.")
    elif command.lower() in musiclibrary.music:
        song = command.lower().split(" ", 1)[1] if "play " in command.lower() else command.lower()
        link = musiclibrary.music[song]
        webbrowser.open(link)
        speak(f"Playing {song}.")

    elif "news" in command.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=np&apiKey={newsapi}")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            
            # Extract the articles
            articles = data.get('articles', [])
            
            # Print the headlines
            for article in articles:
                speak(article['title'])
    else:
        # Let OpenAI handle the request
        output = aiProcess(command)
        speak(output) 


if __name__ == "__main__":
    speak("Initializing Assistance....")

    while True:
        # obtain audio from the microphone
        r = sr.Recognizer()

        print("Processing audio...")

        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "assistance"):
                speak("Ya")
                # Listen for command
                with sr.Microphone() as source:
                    print("Assistance Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    process_command(command)

            if (word.lower() == "stop" or word.lower() == "exit" or word.lower() == "quit" or word.lower() == "end"):
                speak("Shutting down. Goodbye!")
                break

        except Exception as e:
            print("Error:{0}".format(e))
