# Wir können auch größere Objekte als Methoden erstellen:

class Mensch:
    alter = 0

# Das ist ein Mensch und er hat ein Attribut : Alter


du = Mensch()
print(du)  # gibt uns nur den Pointer auf die Stelle im RAM
print(du.alter)  # gibt uns die Variable
ich = Mensch()  # man kann mehrere hiervon haben
du.alter += 1
print(ich.alter)
print(du.alter)
# und ihre eigenschaften sind unterschiedlich
# wir überschreiben jetz mal die Klasse Mensch, sodass man ein Alter mitgeben kann:
# Dafür schreiben wir die "init" Methode - den Konstruktor, eine Methode, die ein Klassenobjekt "erstellt"/ "füllt"


class Mensch:
    def __init__(self, alter: int) -> None:
        self.alter = alter


alter = int(input("Wie alt bist du?\n"))  # Wir lesen eine Variable ein
du = Mensch(alter)
print(du.alter)
# wichtig: self gibt die "Referenz auf sich selbst" d.h. wenn wir self benutzen, dann meinen wir _dieses_ Objekt
# Und auch hier kann man noch andere Methoden definieren
# Wir überschreiben wieder


class Mensch:
    def __init__(self, alter: int) -> None:
        self.alter = alter
        print(self)

    def aelter_werden(self) -> None:
        self.alter += 1


alter = int(input("Wie alt bist du?\n"))  # Wir lesen eine Variable ein
du = Mensch(alter)
print(du.alter)

# Eine Klasse kann auch andere Klassen als Objekte bzw. Attribute in sich haben:


class Menschengruppe:
    def __init__(self, menschen: list[Mensch]) -> None:  # wir können so auch datentypen angeben (list[Mensch])
        self.menschen = menschen

    def durchschnittsalter(self) -> float:
        _alter = 0
        for mensch in self.menschen:  # wir gehen über jeden Mensch in unserer Menschengruppe
            _alter += mensch.alter
        return _alter/len(self.menschen)


# Aufgaben:
# 1 füge in die Klasse Mensch einen Namen und mache, dass man ihn
# zum Anfang angeben kann
# 2 belese dich über Vererbung und mache eine Mann & eine Frau Klasse. beide sollen von Mensch erben
# 3 schreibe eine Punktklasse, und eine Dreieckklasse, die Dreieckklasse soll 3 Punkte entgegennehmen und:
#   - den flächeninhalt ausgeben können
#   - gucken können ob ein Punkt-Objekt _im_ aufgespannten Dreieck ist
#   - Bewegbar sein um ein dx und ein dy und dann eine Dreieck-Objekt zurückgeben
#   Startcode zum weitermachen:
class Punkt:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    # ggf move methode?


class Dreieck:
    def __init__(self, punkte: list[Punkt]) -> None:
        if len(punkte) != 3:
            raise ValueError("Es werden genau 3 Punkte erwartet")  # Wenn wir nicht 3 Punkte haben, werfen wir einen -
                                                                   # Fehler
        self.punkte = punkte

    def get_flaecheninhalt(self) -> float:
        flaecheninhalt = 0.0
        # hier rechnen -> a*b / 2, wobei flaecheninhalt = ((max_x -min_x) * (max_y - min_y)) / 2
        return flaecheninhalt

    def move_dreieck(self, dx, dy) -> object:  # warum object? wir können hier kein Dreieck angeben, weil Python
                                                # den Datentyp "Dreieck" noch nicht kennt, da jedes mal alles neu-
                                                # interpretiert werden muss
        # hier drei Punkte ausrechnen
        punkte = []  # hier sollen die generierten Punkte gesammelt werden (WICHTIG: die bestehenden Punkte
                                                # dürfen _nicht geändert werden, sondern du brauchst neue Punkte
                                                # vielleicht erst eine move_punkt methode in der Punkt-Klasse schreiben?
        return Dreieck(punkte)  # hier soll am ende ein Dreieck zurückgegeben werden

# dann kannst du dir DatOps und CommandLine ansehen
# dann ab zu 2 NumPy
