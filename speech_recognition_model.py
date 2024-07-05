# pip install SpeechRecognition

# pip install pyaudio


import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

# Capture audio data from microphone
with sr.Microphone() as source:
    print("say something:")
    audio_data = recognizer.listen(source)

# Recognize speech using Google Web Speech API
try:
    print("You said: " + recognizer.recognize_google(audio_data))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print(f"Could not request results from Google Speech Recognition service; {e}")