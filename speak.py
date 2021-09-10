import os

from gtts import gTTS

text_to_read="Good morning and Happy New Year"
language="en"
slow_audio_speed=False
filename="my_file.mp3"


audio_created = gTTS(text=text_to_read,lang=language, slow=slow_audio_speed)
audio_created.save(filename)

os.system(f'start {filename}')  
