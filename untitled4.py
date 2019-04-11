# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 19:35:55 2019

@author: kartik
"""
import time
import speech_recognition as sr
def callback(recognizer, audio):                          # this is called from the background thread
    try:
        print("You said " + recognizer.recognize_google(audio))  # received audio data, now need to recognize it
        #time.sleep(3)
    except LookupError:
        print("Oops! Didn't catch that")
        
try:
    r = sr.Recognizer()
    print("start listening")
    r.listen_in_background(sr.Microphone(device_index = 1), callback)
    
   
    #while True: time.sleep(1)
except:
    print("some error")