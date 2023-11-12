#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import wikipediaapi
import os

# Specify the path to the Microsoft Edge executable (msedge.exe)
msedge_path = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

# Create a Wikipedia object with a custom user agent
wiki_wiki = wikipediaapi.Wikipedia(
    language="en",
    user_agent="YourUserAgent/1.0"
)

try:
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    def speak(audio):
        engine.say(audio)
        engine.runAndWait()

    def greet():
        hour = int(datetime.datetime.now().hour)
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        print("Time:", current_time)

        if hour >= 0 and hour < 12:
            speak("Good Morning !")
        elif hour >= 12 and hour < 18:
            speak("Good Afternoon !")
        else:
            speak("Good Evening !")
        speak("Welcome, I am your personal voice assistant, Pixie")

    def VoiceCommand():
        r = sr.Recognizer()

        while True:
            with sr.Microphone() as source:
                print("Listening...")  # Print the "Listening..." message
                r.pause_threshold = 1
                audio = r.listen(source)

            try:
                print("Recognizing...")
                query = r.recognize_google(audio, language='en-in')
                print(f"User said: {query}\n")  # Print the user's voice input
                return query.lower()  # Return the recognized command in lowercase
            except sr.UnknownValueError:
                print("Could not understand audio. Please try again.")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
                return "None"  # Return "None" to handle the error in the main loop

    if __name__ == '__main__':
        greet()
        while True:
            work = VoiceCommand()
            if work == "none":
                continue  # Continue listening if the command is not recognized

            if "wikipedia" in work:
                speak("Searching Wikipedia...")
                speak("Please specify the topic you want to search for.")
                topic = VoiceCommand()
                if topic != "none":
                    speak(f"Searching Wikipedia for {topic}...")
                    wiki_wiki = wikipediaapi.Wikipedia("en")
                    page = wiki_wiki.page(topic)
                    if page.exists():
                        speak("According to Wikipedia")
                        speak(page.summary[:500])  # Speak the first 500 characters of the summary
                    else:
                        speak(f"Sorry, I couldn't find information about {topic} on Wikipedia.")
                else:
                    continue  # Continue listening for more commands if no specific topic is provided

            # Add more conditions for other commands
            elif 'hello' in work:
                speak('Hi, how can I help you')
            elif 'open youtube' in work:
                speak("Here you go to YouTube")
                print("Here you go to YouTube")
                webbrowser.open_new_tab("https://www.youtube.com/")
            elif 'open google' in work:
                speak("Here you go to Google")
                print("Here you go to Google")
                webbrowser.open_new_tab("https://www.google.com/")
            elif 'play music' in work:
                speak('Opening music player....')
                print('Opening music player....')
                webbrowser.open_new_tab("https://music.youtube.com/")
            elif 'open gmail' in work:
                speak("Here you go to Gmail")
                print("Here you go to Gmail")
                webbrowser.open_new_tab("https://mail.google.com")
            elif 'open whatsapp' in work:
                speak("Opening WhatsApp for you")
                print("Opening WhatsApp for you")
                webbrowser.open_new_tab("https://web.whatsapp.com/")
            elif 'exit' in work or 'bye' in work:
                speak("Thanks for giving me your time... have a nice day!")
                speak("Thanks for giving me your time 😊")
                exit()

            # Continue listening for more commands
except BaseException as ex:
    print(f"Error occurred = {ex}")

finally:
    print("Thank you... Bye, have a nice day")


# In[ ]:




