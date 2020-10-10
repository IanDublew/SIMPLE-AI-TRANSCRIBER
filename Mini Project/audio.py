import speech_recognition as sr
from os import path
# just change the name of the audio file here if you want to sample another audio file.
AUDIO_FILE = path.join(path.dirname(
    path.realpath(__file__)), "B.wav")
# use the audio file as the audio source
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)
# recognize speech using Google Speech Recognition
    try:
        print("Audio Output::" +
              r.recognize_google(audio))
    except sr.UnknownValueError:
        print("Could Not Understand Audio")
    except sr.RequestError as e:
        print(
            "Could not request results from Speech Recognition service; {0}".format(e))
