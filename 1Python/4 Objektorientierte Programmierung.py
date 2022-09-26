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

    def move(self, dx: float, dy: float):
        new_x = self.x + dx
        new_y = self.y + dy
        return Punkt(x=new_x, y=new_y)


punktA = Punkt(3, 3)
print("punktA ist bei:", punktA.x, punktA.y)
punktB = punktA.move(1, 4)
print("punktB ist bei:", punktB.x, punktB.y)


class Dreieck:
    def __init__(self, punkte: list[Punkt]) -> None:
        if len(punkte) != 3:
            raise ValueError("Es werden genau 3 Punkte erwartet")  # Wenn wir nicht 3 Punkte haben, werfen wir einen -
                                                                   # Fehler
        self.punkte = punkte

    def intersects(self, punkt: Punkt):
        return False

    def get_flaecheninhalt(self) -> float:
        flaecheninhalt = 0.0
        # hier rechnen -> a*b / 2, wobei flaecheninhalt = ((max_x -min_x) * (max_y - min_y)) / 2
        x_min = self.punkte[0].x
        x_max = self.punkte[0].x
        y_min = self.punkte[0].y
        y_max = self.punkte[0].y
        for punkt in self.punkte:
            if punkt.x < x_min:
                x_min = punkt.x

            if punkt.x > x_min:
                x_max = punkt.x

            if punkt.y < y_min:
                y_min = punkt.y

                y_max = punkt.y

        flaecheninhalt = (x_max - x_min) * (y_max - y_min) * 0.5
        return flaecheninhalt

    def move_dreieck(self, dx: float, dy: float):  # warum object? wir können hier kein Dreieck angeben, weil Python
                                                # den Datentyp "Dreieck" noch nicht kennt, da jedes mal alles neu-
                                                # interpretiert werden muss
        # hier drei Punkte ausrechnen
        punkte = []  # hier sollen die generierten Punkte gesammelt werden (WICHTIG: die bestehenden Punkte
                                                # dürfen _nicht geändert werden, sondern du brauchst neue Punkte
                                                # vielleicht erst eine move_punkt methode in der Punkt-Klasse schreiben?
        for punkt in self.punkte:
            punkte.append(punkt.move(dx, dy))

        return Dreieck(punkte)  # hier soll am ende ein Dreieck zurückgegeben werden


A = Punkt(0, 0)
B = Punkt(-1, 0)
C = Punkt(0, -1)
DreieckA = Dreieck([A, B, C])
DreieckB = DreieckA.move_dreieck(1, 1)

print(DreieckA.get_flaecheninhalt())
print(DreieckB.get_flaecheninhalt())

















# dann kannst du dir DatOps und CommandLine ansehen
# dann ab zu 2 NumPy
