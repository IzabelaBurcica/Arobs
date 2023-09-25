# audio_recorder.py
from datetime import datetime

import pyaudio
import wave
import numpy as np

# Setări pentru înregistrarea audio
chunk = 1024
FORMAT = pyaudio.paInt32
channels = 2
sample_rate = 44100

def record_audio(audio_filename, record_seconds):


    print("A INCEPUT THREAD UL AUDIO" ,  datetime.now())
    p = pyaudio.PyAudio()

    # Identifică dispozitivul audio pentru sunetul ecranului
    device_index = None
    for i in range(p.get_device_count()):
        device_info = p.get_device_info_by_index(i)
        if "Stereo Mix" in device_info["name"]:
            device_index = i
            break

    if device_index is None:
        print("Nu s-a putut găsi dispozitivul pentru sunetul ecranului. Verifică dacă acesta este activat și redenumit corect.")
        return

    audio_stream = p.open(format=FORMAT,
                          channels=channels,
                          rate=sample_rate,
                          input=True,
                          input_device_index=device_index,
                          frames_per_buffer=chunk)
    audio_frames = []

    # Calculează numărul de frame-uri necesare pentru înregistrarea dorită
    frames_to_record = int(sample_rate * record_seconds)

    print("Înregistrează sunetul...")
    for _ in range(0, frames_to_record // chunk):
        audio_data = audio_stream.read(chunk)
        audio_frames.append(audio_data)

    # Adaugă frame-uri suplimentare pentru a acoperi secundele rămase pt ca raman frame uri care nu sunt inregistrate(de dimensiune mai mica de un chunk)
    extra_frames = frames_to_record % chunk
    if extra_frames > 0:
        audio_data = audio_stream.read(extra_frames)
        audio_frames.append(audio_data)

    print("Înregistrare sunet finalizată.")

    audio_stream.stop_stream()
    audio_stream.close()
    p.terminate()

    wf = wave.open(audio_filename, "wb")
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(sample_rate)
    wf.writeframes(b"".join(audio_frames))
    wf.close()

if __name__ == "__main__":
    record_audio("test.wav",13)