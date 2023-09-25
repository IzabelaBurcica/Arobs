import time

from numpy import random
from selenium import webdriver
from selenium.webdriver.common.by import By

from AudioRecorder import record_audio
from VideoRecorder import record_video

# Configuram Selenium și deschidem un browser Chrome
driver = webdriver.Chrome()
driver.get("https://www.youtube.com")


# Așteptam să se încarce pagina principală a YouTube ului
time.sleep(3)

#pornim cele 2 inregistrari

record_audio("test_audio.wav",13)
record_video("test_video.avi",13)

# Alegerea unui videoclip aleatoriu de pe pagina principală
video_elements = driver.find_elements(By.CSS_SELECTOR, "a#video-title")
if video_elements:
    random_video = video_elements[random.randint(0, len(video_elements) - 1)]
    random_video.click()
    time.sleep(3)

    # Redam videoclipul
    player = driver.find_element(By.CSS_SELECTOR, ".ytp-play-button")
    player.click()
else:
    print("Nu s-a gasit videoclip")
# Așteptam o anumită perioadă, apoi închidem browser-ul
time.sleep(20)  # timpul in care browser ul sta deschis
driver.quit()

