### Mediul de dezvoltare si functionalitate

Aplicatia a fost realizata utilizand ca mediu de dezvoltare PyCharm 2023.2.1 si are ca scop inregistrarea audio si video a unei ferestre de pe YouTube.
Aceasta implica realizarea a 4 fisiere de tip .py si anume un program principal unde vor fi testate functiile implementate.
### Implementare

Fisierul AudioRecorder.py contine functia record_audio, care inregistreaza sunetul browser-ului. Pentru a inregistra doar sunetul furnizat de browser am modificat OutPut-ul dispozitivului audio 
pentru browser-ul Google Chrome(asa cum se poate observa in imaginea de mai jos), astfel inregistram doar sunetul furnizat de pagina de YouTube indiferent daca in paralel se aud si alte sunete pe desktop.
Fisierul calculate_sound_level.py contine functia extract_sound_level, care determina nivelul sunetului in db, din inregistarea audio, si il salveaza intr-un fisier .txt.

### Testare
Pentru a vedea functionalitatea aplicatiei este nevoie sa se descarce cele 4 fisiere de tip .py, sa se instaleze bibliotecile necesare si sa se ruleze fisierul main.py.
Fisierul VideoRecorder.py contine functia record_video, care inregistreaza doar browser-ul deschis cu ajutorul bibliotecii Selenium.

![image](https://github.com/IzabelaBurcica/Arobs/assets/106831283/c96c3c88-7380-49f0-b9ac-13b662e9cb27)
