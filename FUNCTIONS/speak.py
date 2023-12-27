import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voices' , voices[1].id)
engine.setProperty('rate',150)

def Speak(audio) :
    print("    ")
    print(f": {audio}")
    print("   ")
    engine.say(audio)
    engine.runAndWait()

# Speak("hey ! how are you")