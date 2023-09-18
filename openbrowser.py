import time

from numpy import random
from selenium import webdriver
from selenium.webdriver.common.by import By

# Configuram Selenium și deschidem un browser Chrome
driver = webdriver.Chrome()
driver.get("https://www.youtube.com")

# Așteptam să se încarce pagina principală a YouTube
time.sleep(3)

# Alegerea unui videoclip aleatoriu de pe pagina principală
video_elements = driver.find_elements(By.CSS_SELECTOR, "a#video-title")
if video_elements:
    random_video = video_elements[random.randint(0, len(video_elements) - 1)]
    random_video.click()
    time.sleep(3)  # încărcarea paginii videoclipului

