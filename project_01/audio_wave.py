# Audio file formants
# .mp3
# .flac
# .wav
# importing important libraries

import wave

obj = wave.open("output.wav", "rb") 

print("Number of channels: ", obj.getnchannels())
print("Sample width: ", obj.getsampwidth())
print("Frame rate: ", obj.getframerate())
print("Number of frames: ", obj.getnframes())
print("Parameters: ", obj.getparams())

t_audio = obj.getnframes() / obj.getframerate()
print("Duration in seconds: ", t_audio)

frames = obj.readframes(-1)
print(type(frames),type(frames[0]))
print("Length of frames: ", len(frames) / 2)
# print("Frames: ", frames)
obj.close()

obj_new = wave.open("output_new.wav", "wb")

obj_new.setnchannels(1)
obj_new.setsampwidth(2)
obj_new.setframerate(16000.0)
obj_new.writeframes(frames)
obj_new.close()