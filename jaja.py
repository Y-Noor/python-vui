import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
import subprocess
import webbrowser

def speak(txt):
    tts = gTTS(text=txt, lang="en")
    filename = "prmpt.mp3"
    tts.save(filename)
    playsound.playsound(filename)

def getAudio():
    r = sr.Recognizer()
    with sr.Microphone() as src:
        audio = r.listen(src)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))

        return said.lower()

def openProg(prog):
    dct = {
        "spotify" : r"C:\Users\Noor Y\AppData\Roaming\Spotify\Spotify.exe",
        "chrome" : r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    }

    subprocess.Popen(dct[prog])


if __name__ == '__main__':
    WAKE = "hey alexa"
    while True:
        print("I am listening")
        returnVal = getAudio()

        if returnVal == WAKE:
            print()
            print(">>>>>>>>>>> sup ni**a")
            returnVal = getAudio()
            if "open" in returnVal:
                kw = returnVal.split()[-1]
                print(">>>>>>>>", kw)
                openProg(kw)

            elif "google scholar" in returnVal:
                kw = returnVal.split()
                s = ' '.join(kw[2:])
                print(s)
                if s.find(".") != -1:
                    webbrowser.open(s)
                else:
                    webbrowser.open('https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=' + s)

            elif "google" in returnVal:
                kw = returnVal.split()
                s = ' '.join(kw[1:])
                if s.find(".") != -1:
                    webbrowser.open(s)
                else:
                    webbrowser.open('http://www.google.com/search?q=' + s)



        # subprocess.Popen(chrome)
