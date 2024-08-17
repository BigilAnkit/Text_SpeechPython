# import os

# if __name__ =='__main__':
#     print("Welcome to RoboSpeaker 1.1 Created by Ankit")
#     while True:
#         x = input("Enter what you want me to speack: ")
#         if x == "q":
#             os.system(".Speak('Bye Bye Friend')")
#             break
#         command = f".Speak('{x}')"
#         os.system(command)

# # import os

# # if __name__ == '__main__':
# #     print("Welcome to RoboSpeaker 1.1 Created by Ankit")
# #     while True:
# #         x = input("Enter what you want me to speak (or 'q' to quit): ")
# #         if x == "q":
# #             os.system("PowerShell -Command \"Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('Bye Bye Friend')\"")
# #             break
# #         command = f"PowerShell -Command \"Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{x}')\""
# #         os.system(command)

from gtts import gTTS
import os

def text_to_speech(text):
    tts = gTTS(text)
    tts.save("output.mp3")
    os.system("start output.mp3")

if __name__ == "__main__":
    user_input = input("Enter the text you want to convert to speech: ")
    text_to_speech(user_input)



# # Install pyttsx3 using pip install pyttsx3.
# # import the module
# import pyttsx3 

# # initialise the pyttsx3 engine 
# engine = pyttsx3.init() 

# # convert text to speech 
# engine.say("I love Python for text to speech, and you?") 
# engine.runAndWait() 