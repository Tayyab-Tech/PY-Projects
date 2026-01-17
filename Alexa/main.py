# alexa  - VOICE-ACTIVATED VIRTUAL ASSISTANT  
# alexa is a voice-activated virtual assistant designed to perform tasks such as web browsing, playing music, fetching news, and responding to user queries using OpenAI's GPT-3.5-turbo model.

import speech_recognition as sr
import pyttsx3
import time
import webbrowser

recognizer = sr.Recognizer()

def speak(text):
    time.sleep(0.3)
    engine = pyttsx3.init('sapi5')
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def processCommand(c):
    if "open google" in c.lower():
        speak("Yes! I can open Google for you")
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        speak("Yes! I can open Facebook for you")
        webbrowser.open("https://facebook.com")
    elif "open insta" in c.lower():
        speak("Yes! I can open instagram for you")
        webbrowser.open("https://instagram.com")
    elif "open linkedin" in c.lower():
        speak("Yes! I can open linkedin for you")
        webbrowser.open("https://linkedin.com")
    elif "open github" in c.lower():
        speak("Yes! I can open github for you")
        webbrowser.open("https://github.com")


if __name__ == "__main__":
    speak("Initializing alexa")

    while True:
        try:
            # Wake word
            with sr.Microphone() as source:
                print("Listening!")
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = recognizer.listen(source, timeout=4, phrase_time_limit=3)
                print("Recognizing...")
            word = recognizer.recognize_google(audio).strip().lower()

            if word.lower() == "alexa":
                speak("Alexa here")
                # Command
                with sr.Microphone() as source:
                    print("Alexa Active...")
                    recognizer.adjust_for_ambient_noise(source, duration=0.5)
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

                command = recognizer.recognize_google(audio)
                processCommand(command)

        except sr.UnknownValueError:
            print("Could not understand audio")

        except sr.WaitTimeoutError:
            print("Listening timed out")

        except Exception as e:
            print("Error:", e)
