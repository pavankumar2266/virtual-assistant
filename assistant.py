import wx
import wikipedia
import wolframalpha
import speech_recognition as sr
import win32com.client as wincl

def speak(text):
    #print(text)
    s= wincl.Dispatch("SAPI.SpVoice")
    s.Speak(text)
   
def recordAudio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("How may i help you?")
        audio = r.listen(source)
    
    data=r.recognize_google(audio)
    
    try:
        print("You said: " +data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return data
  
def groot():
    speak("I am assistant")
    print("Say something")
    input=recordAudio()
    OnEnter(input)

def OnEnter(input):
     try:
        app_id = "Y677G2-KL5A7V43EX"
        client = wolframalpha.Client(app_id)
        res = client.query(input)
        answer = next(res.results).text
        print answer
        speak(answer)
     except:
        print "wiki"
        answer=wikipedia.summary(input)
        print answer
        speak(answer)

groot()
