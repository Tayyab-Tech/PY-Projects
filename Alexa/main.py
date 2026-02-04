# alexa - VOICE-ACTIVATED VIRTUAL ASSISTANT USING GOOGLE GEMINI

import speech_recognition as sr
import pyttsx3
import pygame
import time
import webbrowser
import requests
import os
from gtts import gTTS
import musicLibrary  # Make sure this exists with your music dictionary

# --- API KEYS ---
api_gemini = "AIzaSyCyh7btdorr6RSClSql8Fx39g0PH3vquMg"
newsapi = "04701901eebd4e94a3d40a5b681cf0aa"

# --- SPEECH ENGINE ---
def speak(text):
    time.sleep(0.3)
    engine = pyttsx3.init('sapi5')
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')

    pygame.mixer.init()
    pygame.mixer.music.load("temp.mp3")
    pygame.mixer.music.play()

    # Keep the program running while music plays
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("temp.mp3")

# --- GEMINI AI PROCESSING ---
def aiprocess(command):
    import requests

    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"
    headers = {
        "Content-Type": "application/json",
        "x-goog-api-key": api_gemini
    }
    payload = {
        "systemInstruction": {
            "parts": [
                {"text": "You are Alexa, a concise virtual assistant. Give short responses."}
            ]
        },
        "contents": [
            {
                "parts": [
                    {"text": command}
                ]
            }
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()

        # The text output is nested under candidates -> content -> parts -> text
        ai_text = data["candidates"][0]["content"]["parts"][0]["text"]
        print("Alexa AI:", ai_text)
        return ai_text

    except requests.exceptions.HTTPError as e:
        print("API HTTP Error:", e)
        return "Sorry, I couldn't get a response from the AI."

    except Exception as e:
        print("Request Error:", e)
        return "Sorry, an error occurred while processing that."

# --- COMMAND PROCESSOR ---
def processCommand(c):
    c_lower = c.lower()

    if "open google" in c_lower:
        speak("Opening Google for you")
        webbrowser.open("https://google.com")

    elif "open facebook" in c_lower:
        speak("Opening Facebook for you")
        webbrowser.open("https://facebook.com")

    elif "open insta" in c_lower:
        speak("Opening Instagram for you")
        webbrowser.open("https://instagram.com")

    elif "open linkedin" in c_lower:
        speak("Opening LinkedIn for you")
        webbrowser.open("https://linkedin.com")

    elif "open github" in c_lower:
        speak("Opening GitHub for you")
        webbrowser.open("https://github.com")

    elif c_lower.startswith("play "):
        song = c_lower.split(" ", 1)[1]
        if song in musicLibrary.music:
            speak(f"Playing {song} for you")
            webbrowser.open(musicLibrary.music[song])
        else:
            speak("Sorry, I couldn't find that song")

    elif "news" in c_lower:
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])
            if not articles:
                speak("No news found right now.")
            for i, article in enumerate(articles, start=1):
                speak(f"{i}. {article['title']}")
        else:
            speak(f"Failed to fetch news. Status code: {r.status_code}")
            print(f"Failed to fetch news. Status code: {r.status_code}")

    else:
        # AI handles everything else
        output = aiprocess(c)
        speak(output)

# --- MAIN LOOP ---
if __name__ == "__main__":
    speak("Initializing Alexa")

    recognizer = sr.Recognizer()

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word 'Alexa'...")
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = recognizer.listen(source, timeout=4, phrase_time_limit=3)
            word = recognizer.recognize_google(audio).strip().lower()

            if word == "alexa":
                speak("Hello, how can I help you?")
                with sr.Microphone() as source:
                    print("Listening for command...")
                    recognizer.adjust_for_ambient_noise(source, duration=0.5)
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

                command = recognizer.recognize_google(audio)
                print("Command received:", command)
                processCommand(command)

        except sr.UnknownValueError:
            print("Could not understand audio")

        except sr.WaitTimeoutError:
            print("Listening timed out")

        except Exception as e:
            print("Error:", e)