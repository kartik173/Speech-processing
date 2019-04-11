# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 19:32:50 2019

@author: kartik
"""

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
        print("Google Speech Recognition thinks you said " + recognizer.recognize_google(audio))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

r = sr.Recognizer()
mic_list = sr.Microphone.list_microphone_names()
m = sr.Microphone(device_index = 1)
with m as source:
    r.adjust_for_ambient_noise(m)
    stop_listening = r.listen_in_background(m, callback)
    
    # stop listening, wait for 1 seconds, then restart listening
    stop_listening()
    time.sleep(1)
    stop_listening = r.listen_in_background(m, callback)
    
    # do other things on the main thread
    while True:
        time.sleep(0.1)