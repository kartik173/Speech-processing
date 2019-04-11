# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 19:07:18 2019

@author: kartik
"""

import time
import speech_recognition as sr

# this is called from the background thread
def callback(recognizer, audio):
    # received audio data, now we'll recognize it using Google Speech Recognition
    try:
        print("you said" + recognizer.recognize_google(audio))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

r = sr.Recognizer()
m = sr.Microphone(device_index=1)

stop_listening = r.listen_in_background(m, callback,phrase_time_limit=3)

# stop listening, wait for 5 seconds, then restart listening
stop_listening()
time.sleep(0.1)
stop_listening = r.listen_in_background(m, callback,phrase_time_limit=3)

# do other things on the main thread

print("1")
while True: time.sleep(0.1)