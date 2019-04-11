# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 21:58:54 2019

@author: kartik
"""

import speech_recognition as sr 


r = sr.Recognizer() 
mic_list = sr.Microphone.list_microphone_names() 

with sr.Microphone(device_index = 1) as source: 
    r.adjust_for_ambient_noise(source) 
    print ("Say Something")
    i=1
    
    audio = r.listen(source,phrase_time_limit=2) 
          
    try: 
        text = r.recognize_google(audio) 
        print( "you said: " + text )
      
    except sr.UnknownValueError: 
        print("Google Speech Recognition could not understand audio") 
      
    except sr.RequestError as e: 
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        
print("copmpleted")
    
        
        
        
        
        
        
        
        