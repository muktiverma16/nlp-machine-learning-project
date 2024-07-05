import win32com.client as wincom
speak = wincom.Dispatch("SAPI.SpVoice")
print('Welcome to Myspeechassistant created by Mukti.')
while True:
    x=input('Enter what you want me to speak:')
    if x=="q":
        break
    speak.Speak(x) 