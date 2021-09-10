import os

from gtts import gTTS

myname=("My name is Chinta Pranav.")
fathername=("My father's name is Chinta Venkataa Subrahmanya Sastry.")
mothername=("My mother's name is Chinta  Satya Sri Sailaja.")
maternalgrndmom=("My materanl grandmother's name is Bhaskara Lakshmi Perepa.")
maternalgrndad=("My maternal grandfather's name is Satyamurthy Perepa.")
paternalgrndmom=("My paternal grandmother's name is Chinta Padmavati.")
paternalgrndad=("My paternal grandfather's name is Chinta Lakshmi Narayana Sastry.")
cousin=("My cousin's name is Krithik Perepa.")
maternaluncle=("My maternal Uncle's name is Umakanth Perepa.")
maternalaunt=("My maternal aunt's name is Vaidehi Perepa")

text_to_read=myname+fathername+mothername+maternalgrndmom+maternalgrndad+paternalgrndmom+paternalgrndad+cousin+maternaluncle+maternalaunt
#text_to_read="నా పేరు పద్మావతి, నా మారుపేరు బుల్లితల్లి. నాకు 71 సంవత్సరాలు. నేను బెంగళూరులో నివసిస్తున్నాను. నాకు గారెలు అంటే చాలా ఇష్టం "
language="te"
slow_audio_speed=False
filename="my_file.mp3"


audio_created = gTTS(text=text_to_read,lang=language, slow=slow_audio_speed)
audio_created.save(filename)

os.system(f'start {filename}') 


