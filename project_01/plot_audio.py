import wave
import numpy as np
import matplotlib.pyplot as plt

obj = wave.open("output.wav", "rb")

sample_freq = obj.getframerate()
n_sample = obj.getnframes()
signal_wave = obj.readframes(-1)

obj.close()

t_audio = n_sample / sample_freq
print(t_audio)

signal_array = np.frombuffer(signal_wave, dtype=np.int16)

times = np.linspace(0, t_audio, num=n_sample)

plt.figure(figsize=(20, 4))
plt.plot(times, signal_array, color='blue')
plt.title("Signal Wave")
plt.ylabel("signal wave")
plt.xlabel("Time in seconds")
plt.xlim(0, t_audio)
plt.show()