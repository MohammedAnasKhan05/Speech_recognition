from pydub import AudioSegment

# Load the audio file
audio = AudioSegment.from_wav("output.wav")

# Increase volume by 6 dB
audio = audio + 6

# Double the audio length by repeating it once
audio = audio * 2

# Apply a 2-second fade-in effect
audio = audio.fade_in(2000)

# Apply a 2-second fade-out effect
audio = audio.fade_out(2000)

# Export the modified audio to MP3
audio.export("output_new1.mp3", format="mp3")

# Load the exported MP3 (perhaps for further processing or validation)
audio2 = AudioSegment.from_mp3("output_new1.mp3")
print("Done")
