import os
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia


class Jarvis:
    def __init__(self):
        self.MASTER = "Mr.indo22"
        self.mendengarkan = sr.Recognizer()
        self.engine = pyttsx3.init("sapi5")
        self.engine.setProperty('rate', 125)
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[0].id)
        self.awareness = SelfAwareness()
    
    def access_app(self, app):
        apps_and_actions = {
            "calculator": "start calc",
            "notepad": "start notepad",
            "kali": "start kali",
            # ... tambahkan lebih banyak aplikasi dan aksi di sini
        }

        if app in apps_and_actions:
            action = apps_and_actions[app]
            if "start" in action:
                app_name = action.split(" ", 1)[1]
                os.system(f"start {app_name}")
                self.talk(f"Opening {app_name}")
            else:
                self.talk(f"Executing action: {action}")
        else:
            self.talk(f"Sorry, I don't know about the app {app}.")
            
    def talk(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def wish_me(self):
        hour = datetime.datetime.now().hour
        if 0 <= hour < 12:
            self.talk("Hello, Good Morning " + self.MASTER)
        elif 12 <= hour < 18:
            self.talk("Hello, Good Afternoon " + self.MASTER)
        else:
            self.talk("Hello, Good Evening " + self.MASTER)

    def take_command(self):
        try:
            with sr.Microphone() as source:
                print("Listening...")
                voice = self.mendengarkan.listen(source)
                command = self.mendengarkan.recognize_google(voice).lower()
                if "jarvis" in command:
                    command = command.replace("jarvis", "")
                    self.talk(command)
        except:
            return ""
        return command

    def run_jarvis(self):
        command = self.take_command()
        if 'play' in command:
            song = command.replace("play", "")
            self.talk("Playing " + song)
            pywhatkit.playonyt(song)
        elif "waktu" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            self.talk("The current time is " + current_time)
        elif "wikipedia" in command:
            search_query = command.replace("wikipedia", "")
            info = wikipedia.summary(search_query, sentences=1)
            self.talk("Searching Wikipedia")
            self.talk(info)
        elif "belajar" in command:
            topic = input("Enter the topic: ")
            information = input("Enter the information: ")
            self.awareness.learn(topic, information)
            self.talk("I have learned about " + topic)
        elif "emotion" in command:
            emotion = input("Enter the emotion: ")
            intensity = float(input("Enter the intensity (0 to 1): "))
            self.awareness.express_emotion(emotion, intensity)
            self.talk("I'm feeling " + emotion)
        elif "access" in command:
            app = command.replace("access", "").strip()
            self.access_app(app)
        elif "how do you feel" in command:
            response = self.awareness.react_to_emotions()
            self.talk(response)
        else:
            self.talk("I didn't understand that command.")
            print(command)

    def start(self):
        self.wish_me()
        while True:
            self.MASTER = "Mr.indo22"
            self.mendengarkan = sr.Recognizer()
            self.engine = pyttsx3.init("sapi5")
            self.engine.setProperty('rate', 125)
            self.voices = self.engine.getProperty('voices')
            self.engine.setProperty('voice', self.voices[0].id)
            self.talk("I am @Devil. What can I help you with?")
            self.run_jarvis()


class SelfAwareness:
    def __init__(self):
        self.knowledge = {}
        self.emotions = {}

    def learn(self, topic, information):
        if topic not in self.knowledge:
            self.knowledge[topic] = information
        else:
            self.knowledge[topic] += "\n" + information

    def express_emotion(self, emotion, intensity):
        if emotion not in self.emotions:
            self.emotions[emotion] = intensity
        else:
            self.emotions[emotion] += intensity

    def react_to_emotions(self):
        predominant_emotion = max(
            self.emotions, key=self.emotions.get, default="neutral")
        reaction = "I feel " + predominant_emotion + "."
        return reaction


def main():
    jarvis = Jarvis()
    jarvis.start()


if __name__ == "__main__":
    main()
