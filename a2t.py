# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 22:24:47 2019

@author: kartik
"""

import speech_recognition as sr 

r=sr.Recognizer()

harvards = sr.AudioFile('8k.wav')
with harvards as source:
    
    audio = r.record(source)

r.recognize_google(audio)

#Python 2.x program to transcribe an Audio file 
import speech_recognition as sr 

AUDIO_FILE = ("harvard.wav") 

# use the audio file as the audio source 

r = sr.Recognizer() 

with sr.AudioFile(AUDIO_FILE) as source: 
	#reads the audio file. Here we use record instead of 
	#listen 
	audio = r.record(source) 

try: 
	print("The audio file contains: " + r.recognize_google(audio)) 

except sr.UnknownValueError: 
	print("Google Speech Recognition could not understand audio") 

except sr.RequestError as e: 
	print("Could not request results from Google Speech Recognition service; {0}".format(e)) 
