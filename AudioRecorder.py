# audio_recorder.py
import pyaudio
import wave


# Setari pentru inregistrarea audio
chunk = 1024  # dimensiunea unui "chunk" de date audio care va fi înregistrat la fiecare iterație
FORMAT = pyaudio.paInt32  # dormatul pentru datele audio
channels = 2
sample_rate = 44100 #frecventa de esantionare

#definim functia de inregistrare aufio avand ca parametrii numele fisierului audio asa cum va fi salvat, nr de secunde ale sunetului si un parametru bariera

def record_audio(audio_filename, record_seconds, barrier):
    #asteapta ca toate thread-urile sa se sincronizeze pentru ca inregistrarea video si audio sa porneasca simultan
    barrier.wait()
    #print("A INCEPUT THREAD UL AUDIO" ,  datetime.now())
    p = pyaudio.PyAudio()  # inițializeaza obiectul PyAudio pentru a lucra cu inregistrarea audio


    #identifica dispozitivul audio pentru sunetul ecranului
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
    audio_frames = []  #inițializează o lista pentru a stoca cadrele audio capturate

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

    audio_stream.stop_stream() #opreste fluxul audio
    audio_stream.close() #inchide fluxul audio
    p.terminate()

    wf = wave.open(audio_filename, "wb")
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(sample_rate)
    wf.writeframes(b"".join(audio_frames))
    wf.close()
