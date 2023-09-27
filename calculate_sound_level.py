import numpy as np
import wave

def rms_flat(a):
    return np.sqrt(np.mean(np.absolute(a)**2))

def extract_sound_level(audio_file_path, output_file_path):
    try:
        # Deschide fișierul audio pentru citire
        audio_file = wave.open(audio_file_path, 'rb')

        # Obține informații despre fișierul audio
        n_frames = audio_file.getnframes()

        # Citeste toate cadrele audio
        audio_data = audio_file.readframes(n_frames)

        # Converteste datele audio in format numpy array
        audio_array = np.frombuffer(audio_data, dtype=np.int16)

        # Calculează nivelul sunetului utilizând funcția rms_flat
        sound_level = 20 * np.log10(rms_flat(audio_array)) - 20 * np.log10(18613)

        # Închide fișierul audio
        audio_file.close()

        # Salvează nivelul sunetului în fișierul text
        with open(output_file_path, 'w') as output_file:
            output_file.write(f'Nivelul sunetului: {sound_level:.2f} dB')

    except Exception as e:
        print(f'Eroare: {str(e)}')
