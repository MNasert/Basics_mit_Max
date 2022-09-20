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
# Und auch hier kann man noch andere Methoden definieren
# Wir überschreiben wieder

class Mensch:
    def __init__(self, alter: int):
        self.alter = alter
        print(self)

    def aelter_werden(self):
        self.alter += 1


alter = int(input("Wie alt bist du?\n"))  # Wir lesen eine Variable ein
du = Mensch(alter)
print(du.alter)

# Aufgaben:
# 1 füge in die Klasse Mensch einen Namen und mache, dass man ihn
# zum Anfang angeben kann
# 2 belese dich über Vererbung und mache eine Mann & Frau Klasse,
# die von Mensch erbt
# dann ab zu 2 NumPy
