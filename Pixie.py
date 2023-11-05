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
        speak("Welcome, I am your personal voice assistant, Pixel")

    def VoiceCommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")  # Print the "Listening..." message
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")  # Print the user's voice input
        except Exception as e:
            print(e)
            print("Unable to Recognize your voice.")
            return "None"
        return query

    if __name__ == '__main__':
        greet()
        while True:
            work = VoiceCommand()
            if "Wikipedia" in work:
                speak("Searching Wikipedia...")
                speak("Please specify the topic you want to search for.")
                topic = VoiceCommand()
                if topic != "None":
                    speak(f"Searching Wikipedia for {topic}...")
                    wiki_wiki = wikipediaapi.Wikipedia("en")
                    page = wiki_wiki.page(topic)
                    if page.exists():
                        speak("According to Wikipedia")
                        speak(page.summary[:500])  # Speak the first 500 characters of the summary
                    else:
                        speak(f"Sorry, I couldn't find information about {topic} on Wikipedia.")
            if 'hello' in work:
                speak('Hi, how can I help you')

            # Open links using Microsoft Edge
            webbrowser.register('msedge', None, webbrowser.BackgroundBrowser(msedge_path), preferred=True)
            web_browser = webbrowser.get('msedge')  # Register and get Microsoft Edge

            if 'open YouTube' in work:
                speak("Here you go to YouTube")
                web_browser.open_new_tab("https://www.youtube.com/")

            if 'open Google' in work:
                speak("Here you go to Google")
                web_browser.open_new_tab("https://www.google.com/")

            if 'play music' in work:
                speak('Opening music player....')
                web_browser.open_new_tab("https://music.youtube.com/")

            if 'open Gmail' in work:
                speak("Here you go to Gmail")
                web_browser.open_new_tab("https://mail.google.com")

            if 'open WhatsApp' in work:
                speak("Opening WhatsApp for you")
                web_browser.open_new_tab("https://web.whatsapp.com/")

            if 'exit' in work or 'bye' in work:
                speak("Thanks for giving me your time... have a nice day!")
                exit()

except BaseException as ex:
    print(f"Error occurred = {ex}")

finally:
    print("Thank you... Bye, have a nice day")


# In[ ]:





# In[ ]:




