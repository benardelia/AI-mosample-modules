# pre request pyAudio package should be installed, otherwise speech recognition 
# will throw an attribute error 
import speech_recognition as sr

listener = sr.Recognizer()

try:
    with sr.Microphone() as source:
        print('Listening...')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        print(command)
except:
    print('failed')   