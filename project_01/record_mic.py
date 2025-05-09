import pyaudio
import wave

FRAMES_PER_BUFFER = 3200   # 2 seconds of audio
FORMAT = pyaudio.paInt16  # 16-bit PCM
CHANNELS = 1  # Mono audio
RATE = 16000  # Sample rate in Hz

p = pyaudio.PyAudio()
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=FRAMES_PER_BUFFER)
print("Start recording...")

seconds = 5  # Duration of recording in seconds
frames = []

for i in range(0, int(RATE / FRAMES_PER_BUFFER * seconds)):
    data = stream.read(FRAMES_PER_BUFFER)
    frames.append(data)
print("Recording finished.")

stream.stop_stream()
stream.close()
p.terminate()

obj = wave.open("output.wav", "wb")
obj.setnchannels(CHANNELS)
obj.setsampwidth(p.get_sample_size(FORMAT))
obj.setframerate(RATE)
obj.writeframes(b"".join(frames))
obj.close()