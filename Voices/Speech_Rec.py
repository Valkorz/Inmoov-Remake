import speech_recognition as sr

def recognition():
   r = sr.Recognizer()
   with sr.Microphone() as source:
      print("Say something")
      audio = r.listen(source)
   text = r.recognize_ibm(audio)
   return text

   
