# serai_trailer_voiceover_merge.py
# Generate SERAI trailer narration with Lola and merge into one audio file

from lola_voice import speak   # adjust if Lola uses a different module
from pydub import AudioSegment

# Full cinematic script lines
script_lines = [
    "In a world where intelligence is no longer bound by reality...",
    "A new architecture emerges — uniting mind, matter, and motion.",
    "SERAI thinks. It moves. It connects. It creates.",
    "At its heart, a living workbook… orchestrating realities.",
    "SERAI is not just software. It is the blueprint of tomorrow.",
    "SERAI — Building realities beyond imagination."
]

# Step 1: Generate individual audio clips
filenames = []
for i, line in enumerate(script_lines, start=1):
    filename = f"scene_{i}.mp3"
    print(f"Generating narration for Scene {i}: {line}")
    speak(line, filename=filename)   # Lola's TTS saves each line
    filenames.append(filename)

# Step 2: Merge all clips into one continuous track
combined = AudioSegment.empty()
for file in filenames:
    clip = AudioSegment.from_file(file, format="mp3")
    combined += clip + AudioSegment.silent(duration=500)  # 0.5s pause between lines

# Export final merged narration
combined.export("serai_trailer_full.mp3", format="mp3")
print("Final narration saved as serai_trailer_full.mp3")
