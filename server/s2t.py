### This script sends a .wav file to google cloud speech to text api, and returns text
import os
import io



# Find audio file
file_name = os.path.join(
    os.path.dirname(__file__),
    'myRecording.wav')

# Loads the audio file into memory
with io.open(file_name, 'rb') as audio_file:
    content = audio_file.read()

