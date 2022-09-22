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
# 2 belese dich über Vererbung und mache eine Mann & Frau Klasse,
# die von Mensch erbt
# dann ab zu 2 NumPy
