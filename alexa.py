import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
# Creating a Recognizer to recognize my voice

listener = sr.Recognizer()
engine = pyttsx3.init() # engine that speaks to me
# Convert the voice of Alexa into a femele voice
# Gets all the voices different voices that the text speech can provide
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    # engine.say('What can I do for you')
    engine.runAndWait()

def take_command(): # From myself
    try:
        with sr.Microphone() as source: # source3 of my audio
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            # Detecting whether Alexa is called
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa ', '')
                print(command)
    except:
        pass
    return command

# What do you want to do with Alexa
def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play',  '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('Sorry, I have a headache')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again')

while True:
    run_alexa()