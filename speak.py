import pyttsx3

# Initialize the engine
engine = pyttsx3.init()

# Set properties (optional)
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 1.0)  # Volume (0.0 to 1.0)

# Speak text
engine.say("Hello! This is a text-to-speech test.")
engine.runAndWait()
