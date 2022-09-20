import random
# Wir importieren random
# wir schreiben eine Funktion um uns den text zu formatieren, sodass er gut zu verarbeiten ist


def reformat(keywordss_t_e, text):  # wir erhalten eine liste mit keywords die wir excluden und einen text
    text = text.split(keywordss_t_e[1])  # Was macht split? "Das ist ein" -> ["Das", "ist", "ein"]-
    # wir übergeben ein keyword nach dem wir immer splitten- statt space also keyword[1]
    for i in range(len(text)):  # Wir gucken den ganzen text an
        text[i] = text[i].replace(keywordss_t_e[0], "")  # wir ersetzen unsere keywords; replace nimmt keine listen
        text[i] = text[i].replace(keywordss_t_e[1], "")  # -||-
        text[i] = text[i].replace("\n", "")  # wir ersetzen auch Leerzeilen
    return text  # Rückgabe des Textes

# wir wollen auch etwas schreiben können
def randomText():  # exakte beschreibung davon was wir tun
    size = random.randint(1, 20)  # wir generieren eine zahl zwischen 1 und 20
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"
                , "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    text = "\n<start>\n"
    for i in range(size):
        text += alphabet[random.randint(0, len(alphabet)-1)]
    text += "\n</start>"
    return text  # wir haben einen text mit unseren keywords generiert und einen beliebigen string an buchstaben
