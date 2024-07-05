import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Function to convert text to speech
def speak_text(text):
    engine.say(text)
    engine.runAndWait()

# Main function
if __name__ == "__main__":
    print("Welcome to the Text-to-Speech program!")
    while True:
        text = input("Enter the text you want to convert to speech (or type 'q' to quit): ")
        if text.lower() == 'q':
            break
        speak_text(text)
