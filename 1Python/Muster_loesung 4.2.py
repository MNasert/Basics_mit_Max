# Python bietet nur sehr umständliche Gestaltung abstrakter Klassen, daher schreiben wir direkt eine funktionale
# "Basis" Klasse für einen Menschen und dann folgeattribute, sorgen aber dafür, dass ein Fehler geworfen wird, wenn
# keine der Folgeklassen verwendet wurde

class Mensch:
    def __init__(self, name: str, age: int) -> None:
        """
        Here could be a proper description of this class
        :param name: here could be put a proper description of this parameter
        :param age: here could be put a proper description of this parameter
        """

        self.name = name
        self.age = age
        self.gender = None

    # Hier kommen Methoden, die jede Unterklasse haben muss
    def say_something(self, something) -> None:
        """
        Here could be a proper description of this method
        :param something: here could be put a proper description of this parameter
        :return:
        """

        if not self.gender:
            raise AttributeError(f"Used invalid class type {type(self)}")
        print(f"{self.name}, {self.gender}{self.age}: {something}")


# Wichtig:
# wir müssen nicht in jeder der folgenden Klassen nochmal eine "say_something" Methode schreiben, da sie bereits
# existiert und an die "Kinder" weitergegeben wird - vererbt wird
# genauso existieren auch die Klassenattribute "name", "age" und "gender", diese wurden erzeugt mittels
# super(...).__init(...)
# super ruft den parent (Die Klasse die vererbt/ von der geerbt wird) auf und ermöglicht Zugriffe auf darüberliegende
# Methoden. So auch die Initialisierung der der Klassenattribute.

class Mann(Mensch):
    def __init__(self, name: str, age: int) -> None:
        """
        Here could be a proper description of this class

        Note that we do not have to describe every parameter, if its described in the parent-class
        """

        super(Mann, self).__init__(name, age)
        self.gender = "M"

    def say_something(self, something) -> None:
        super(Mann, self).say_something(something)  # Könnten wir optional auch machen, da wir aber nix an der
        # Methode ändern, brauchen wir das nicht


class Frau(Mensch):
    def __init__(self, name: str, age: int) -> None:
        """
        Here could be a proper description of this class

        Note that we do not have to describe every parameter, if its described in the parent-class
        """

        super(Frau, self).__init__(name, age)
        self.gender = "F"


Person_Fehler = Mensch("Niemand", -1)
try:
    Person_Fehler.say_something("Dieser Aufruf wird einen Fehler verursachen")
except AttributeError as e:  # e für "exception"
    print("Hier wird gleich der von uns in der Klasse festgelegte Error geprintet:")
    print(e, "\n")


PersonA = Mann("Hans", 63)
PersonA.say_something("Hallo")

PersonB = Frau("Gisela", 75)
PersonB.say_something("Hallo")
