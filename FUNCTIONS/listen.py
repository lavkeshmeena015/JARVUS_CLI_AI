# pip install PyAudio
# pip install SpeechRecognition

import speech_recognition as sr 

def Listen():
    r = sr.Recognizer()
    
    with sr.Microphone() as source :
        print("listening..!!")

        r.pause_threshold = 1
        # audio = r.listen(source)
        audio = r.listen(source,0,6)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio,language='en-in')
        
        print(f" your Command : {query}\n")
    except :
        return ""
    
    query = str(query).lower()

    return query

Listen()