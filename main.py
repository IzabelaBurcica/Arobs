# main.py
import time
import threading

import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
from moviepy.editor import VideoFileClip, AudioFileClip
from AudioRecorder import record_audio
from VideoRecorder import record_video


# Numele fișierului de ieșire pentru sunet
audio_filename = "audio.wav"
# Numele fișierului de ieșire pentru video
video_filename = "screen_capture.avi"
# Numele fișierului final
final_video_filename = "final_video.mp4"
record_seconds = 20

# Funcție pentru înregistrarea sunetului și video
def record_audio_and_video():

    barrier = threading.Barrier(2)

    # Creează două fire de execuție pentru înregistrare audio și video
    video_thread = threading.Thread(target=record_video, args=(video_filename, record_seconds, barrier))
    audio_thread = threading.Thread(target=record_audio, args=(audio_filename, record_seconds, barrier))

    # Deschide Selenium și navighează pe YouTube
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com")
    time.sleep(3)

    # Alegere videoclip aleatoriu de pe pagina principală
    video_elements = driver.find_elements(By.CSS_SELECTOR, "a#video-title")
    if video_elements:
        random_video = video_elements[np.random.randint(0, len(video_elements))]
        random_video.click()
        time.sleep(3)

        # Redare videoclip
        player = driver.find_element(By.CSS_SELECTOR, ".ytp-play-button")
        player.click()


    # Porniți cele două fire de execuție
    audio_thread.start()
    video_thread.start()


    # Așteaptă ca cele două fire de execuție să se încheie
    audio_thread.join()
    video_thread.join()

    # Încarcă fișierele video și audio
    video_clip = VideoFileClip(video_filename)
    audio_clip = AudioFileClip(audio_filename)

    # Suprapune audio-ul pe videoclip
    final_clip = (video_clip.set_audio(audio_clip))

    # Salvează videoclipul final
    final_clip.write_videofile(final_video_filename, codec="libx264")

    # Eliberează resursele
    final_clip.close()
    video_clip.close()
    audio_clip.close()

    # Închide browser-ul Selenium
  #  time.sleep(10)
    driver.quit()

if __name__ == "__main__":
    record_audio_and_video()
