import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def wish():
    engine.say('Hello, I"m Natasha. How can I help you?')
    engine.runAndWait()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            commands = listener.recognize_google(voice)
            engine.say(commands)
            engine.runAndWait()
            # print(command)
    except:
        pass
    return commands

def run():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('Playing '+ song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print('time: '+time)
        talk('current time is ' +time)
    elif 'who is' in command:
        info = wikipedia.summary(command, 1)
        print(info)
        talk(info)
    elif 'what is' or 'what are' in command:
        info = wikipedia.summary(command, 1)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('I didnot get that, Can you please repeat it?')
wish()
while True:
    run()