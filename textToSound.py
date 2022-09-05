import pyttsx3


engine = pyttsx3.init()
engine.setProperty('rate', 120)
try:
    file = open('Golden.txt', 'r')
    for word in file.readlines():
        engine.say(word)
        engine.runAndWait()
except:
    print('failed')