import os

from gtts import gTTS

text_to_read="Puttina roju Subhaakaanshalu, thatha"
language="te"
slow_audio_speed=False
filename="my_file.mp3"


audio_created = gTTS(text=text_to_read,lang=language, slow=slow_audio_speed)
audio_created.save(filename)

os.system(f'start {filename}') 