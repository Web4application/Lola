import whisper
import sounddevice as sd
import scipy.io.wavfile as wav
import os
from elevenlabs import generate, play, set_api_key

set_api_key("YOUR_ELEVENLABS_API_KEY")  # Replace with your key

def record_audio(filename="input.wav", duration=5):
    print("Recording...")
    fs = 44100
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    wav.write(filename, fs, audio)
    print("Recording done.")

def transcribe_audio(filename="input.wav"):
    model = whisper.load_model("base")
    result = model.transcribe(filename)
    return result["text"]

def speak_text(text):
    audio = generate(text=text, voice="Lola")  # Use your ElevenLabs voice name
    play(audio)
