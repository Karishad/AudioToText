# imports the speech_recognition module
# if not contained, run 
# pip install SpeechRecognition
import speech_recognition as sr

r = sr.Recognizer()
audio_file = sr.AudioFile('Speech.ogg')
with audio_file as source:
    r.adjust_for_ambient_noise(source)
    audio = r.record(source)
    
result = r.recognize_google(audio)

with open('Speech.txt', mode = 'w') as file:
    file.write("Recognize text: " )
    file.write("\n")
    file.write(result) 
    print("done")