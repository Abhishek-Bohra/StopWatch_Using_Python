import time
import pyttsx3  # Text-to-speech library

def speak(message):
    """Speaks the given message using the pyttsx3 library."""
    engine = pyttsx3.init()
    engine.say(message)
    engine.runAndWait()

def countdown(my_time):
    """Counts down from the specified time in seconds and speaks 'Time's Up' at the end."""
    for x in range(my_time, 0, -1):
        seconds = x % 60
        minutes = int(x / 60) % 60
        hours = int(x / 3600)
        print(f"{hours:02}:{minutes:02}:{seconds:02}")
        time.sleep(1)
    speak("Times up")  # Speak the message after the countdown finishes

if __name__ == "__main__":
    my_time = int(input("Enter the time in seconds: "))
    countdown(my_time)