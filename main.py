import time
import threading
import logging  # Importă modulul pentru logging

import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
from moviepy.editor import VideoFileClip, AudioFileClip
from AudioRecorder import record_audio
from VideoRecorder import record_video
from calculate_sound_level import extract_sound_level

# Configurarea logger-ului
logging.basicConfig(filename="execution_log.txt", level=logging.INFO, format="%(asctime)s - %(levelname)s: %(message)s")

audio_filename = "audio.wav"
video_filename = "screen_capture.avi"
final_video_filename = "final_video.mp4"
record_seconds = 20

def record_audio_and_video():
    try:

        barrier = threading.Barrier(2)

        # Cream două fire de execuție pentru înregistrare audio și video
        video_thread = threading.Thread(target=record_video, args=(video_filename, record_seconds, barrier))
        audio_thread = threading.Thread(target=record_audio, args=(audio_filename, record_seconds, barrier))

        # Deschidem Selenium și navighează pe YouTube
        driver = webdriver.Chrome()
        driver.get("https://www.youtube.com")
        time.sleep(3)

        logging.info("Deschidere browser si navigare pe YouTube")

        # Alegem un videoclip aleatoriu de pe pagina principală
        video_elements = driver.find_elements(By.CSS_SELECTOR, "a#video-title")
        if video_elements:
            random_video = video_elements[np.random.randint(0, len(video_elements))]
            random_video.click()
            time.sleep(3)

            logging.info("Alegere videoclip aleatoriu")

            # Redare videoclip
            player = driver.find_element(By.CSS_SELECTOR, ".ytp-play-button")
            player.click()

            logging.info("Redare videoclip")

        # Pornim cele două fire de execuție
        audio_thread.start()
        video_thread.start()

        logging.info("Incep înregistrarea audio si video")

        # Așteaptăm ca cele două fire de execuție să se încheie
        audio_thread.join()
        video_thread.join()

        logging.info("Inregistrarea audio si video s-a incheiat")

        # Încarcăm fișierele video și audio
        video_clip = VideoFileClip(video_filename)
        audio_clip = AudioFileClip(audio_filename)

        # Suprapunem audio-ul pe videoclip
        final_clip = (video_clip.set_audio(audio_clip))

        # Salvam videoclipul final
        final_clip.write_videofile(final_video_filename, codec="libx264")

        logging.info("Generare si salvare videoclip final")

        # Eliberam resursele
        final_clip.close()
        video_clip.close()
        audio_clip.close()

        # Închidem browser-ul
        driver.quit()

    except Exception as e:
        logging.error(f"A intervenit o eroare: {str(e)}")

if __name__ == "__main__":
    record_audio_and_video()
    output_file_path = 'sound_level.txt'  # Numele fișierului de ieșire pentru nivelul sunetului

    try:
        extract_sound_level(audio_filename, output_file_path)
        logging.info("Calcul nivel de sunet efectuat cu succes")
    except Exception as e:
        logging.error(f"A intervenit o eroare în calcularea nivelului de sunet: {str(e)}")
