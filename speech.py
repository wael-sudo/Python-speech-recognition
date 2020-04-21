
#####problems that may accure 
### you have to install pyaudio but first the whl file from https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio 
# download  PyAudio-0.2.11-cp37-cp37m-win32.whl
# pip install 'Path'\PyAudio-0.2.11-cp37-cp37m-win32.whl
import speech_recognition as sr
r=sr.Recognizer()
with sr.Microphone() as source:
    print("say somthing !!")
    audio=r.listen(source)
    
    try:
        text=r.recognize_google(audio)
        print('you said: {}'.format(text))
         
    except:
        print('Sorry could not recognize your voice')
             
