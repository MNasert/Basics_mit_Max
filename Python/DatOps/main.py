import Python.DatOps.tools as tools
#wir importieren alles

if __name__ == "__main__":#main methode....

    try:#wir versuchen die datei zu öffnen
        file = open("data.dat")
        lines = file.read()#wir lesen alles ein
        file.close()#wir schließen das file erstmal wieder
        text = tools.reformat(["<start>", "</start>"], lines)# wir benutzen unsere selbstgeschriebene Methode/Funktion
        print(text)#und geben uns mal alles aus
    except FileNotFoundError:#haben wir das file nicht gefunden dann sag uns das:
        print("No such file in directory")

    file = open("data.dat", "a")#wir öffnen die datei nochmal im "a" mode- append- anfügen
    file.write(tools.randomText())#wir schreiben unseren randomtext rein
    file.close()#und schließen alles

