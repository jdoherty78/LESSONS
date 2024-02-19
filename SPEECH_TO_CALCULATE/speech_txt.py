def SpeakText(command = "This is so cool"):
    import pyttsx3
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
