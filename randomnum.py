import os

from gtts import gTTS

import random 

name=str(input("Please enter the user's name :"))
x1=("You Dont wait for the opportunity, you create it.")
x2=("Yesterday was past, Tomorrow is a mystery, Today is a Gift. That's why it is called present.")
x3=("Either you run the day, or the day runs you.")
x4=("It's not about being the best, it is about being better than you were the previous day.")
x5=("If you change your mindset, there is a probability to change your whole world.")
x6=("Tough situations build strong people.")
x7=("Fear does not exist anywhere, it only exists in your mind")
x8=("The Best way to predict the future is to create it")
x9=("You have to fight through some bad days to earn the best day of your life.")
x10=("If safety is a joke, then Death is a punchline")
x11=("అరటి దూట  పశువుల ఆహారం ; Banana stem is cattle's food.")
samplelist=[x11]
text = samplelist[random.randrange(0,len(samplelist))]

print(name,"!", text)

text_to_read = name + "!" + text
language="en"
slow_audio_speed=False
filename="my_file.mp3"


audio_created = gTTS(text=text_to_read,lang=language, slow=slow_audio_speed)
audio_created.save(filename)

os.system(f'start {filename}') 


