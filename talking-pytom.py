import pyttsx3
friend = pyttsx3.init()
speech = input("Say Something: ")
friend.say(speech)
friend.runAndWait() 
