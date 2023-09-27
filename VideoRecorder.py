import cv2
import numpy as np
import pyautogui
import pygetwindow as gw

# numărul de cadre pe secundă la care se va înregistra videoclipul
frame_rate = 10.0

# definim funcția de înregistrare a desktopului având ca parametrii numele fișierului video așa cum va fi salvat, nr de secunde ale video-ului și un parametru barieră
def record_video(video_filename, record_seconds, barrier):
    try:
        # așteaptă ca toate thread-urile să se sincronizeze pentru ca înregistrarea video să pornească simultan
        barrier.wait()

        # Găsește fereastra browser-ului (poate necesita nume personalizat pentru fereastra browser-ului)
        browser_window = gw.getWindowsWithTitle("YouTube")[0]

        # Obține coordonatele și dimensiunile ferestrei browser-ului
        left, top, width, height = browser_window.left, browser_window.top, browser_window.width, browser_window.height

        # definim un cod cu patru caractere pentru codec-ul de compresie a videoclipului
        fourcc = cv2.VideoWriter_fourcc(*"XVID")
        # inițializăm obiectul video_out
        video_out = cv2.VideoWriter(video_filename, fourcc, frame_rate, (width, height))

        print("Înregistrează ecranul browser-ului...")

        num_frames = int(frame_rate * record_seconds)

        for _ in range(num_frames):
            # Capturăm ecranul doar pentru fereastra browser-ului
            screenshot = pyautogui.screenshot(region=(left, top, width, height))
            frame = np.array(screenshot)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            video_out.write(frame)

        print("Înregistrare ecran browser finalizată.")
        # eliberăm resursele
        video_out.release()
    except Exception as e:
        print(f"A intervenit o eroare: {str(e)}")
