import speech_recognition as sr
import io


path = input("enter path of the audio file")
audio_file = io.open("path.flac", 'rb')

r = sr.Recognizer()

with sr.AudioFile(audio_file) as source:
    audio = r.record(source)

try:
    print("the audio file contains: "+r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")

except sr.RequestError as e:
    print("could not request results from Google Speech Recognition service; {0}".format(e))
