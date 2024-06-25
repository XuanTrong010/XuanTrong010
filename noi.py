import speech_recognition as sr

# Tạo đối tượng Recognizer
robot_ear = sr.Recognizer()

# Sử dụng Microphone để lấy âm thanh
with sr.Microphone() as mic:
    print("Robot : I'm Listening")
    audio = robot_ear.listen(mic)

# Thử nhận dạng giọng nói sử dụng Google Web Speech API
try:
    you = robot_ear.recognize_google(audio)
    print("You said: " + you)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print(f"Could not request results from Google Speech Recognition service; {e}")
