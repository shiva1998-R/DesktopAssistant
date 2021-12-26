import speech_recognition as sr

r=sr.Recognizer()
print(sr.Microphone.list_microphone_names())
while True:
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=2)
        print("Set minimum energy threshold to {}".format(r.energy_threshold))
        print("say anything : ")
        audio= r.listen(source,phrase_time_limit=5)
        try:
            print("Got it! Now to recognize it...")
            text = r.recognize_google(audio)
            print(text)
            if 'exit' in text:
                break
        except:
            print("sorry, could not recognise")


