from os import system
#import pyttsx3

#engine = pyttsx3.init()
#engine.say("I will speak this text")  You can use the audio mechanisms with this python library
#engine.runAndWait()
#engine.stop()

def voice(string):

    system("say {}".format(string))
    






