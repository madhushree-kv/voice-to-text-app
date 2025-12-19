import tkinter as tk
import speech_recognition as sr

def voice_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        status_label.config(text="Listening...")
        window.update()
        try:
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio)
            text_area.insert(tk.END, text + "\n")
            status_label.config(text="Done")
        except:
            status_label.config(text="Error")

window = tk.Tk()
window.title("Voice to Text App")
window.geometry("400x300")

record_button = tk.Button(window, text="Start Recording", command=voice_to_text)
record_button.pack(pady=10)

text_area = tk.Text(window, height=10, width=40)
text_area.pack()

status_label = tk.Label(window, text="")
status_label.pack(pady=5)

window.mainloop()
