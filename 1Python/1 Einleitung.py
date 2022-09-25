# Wir starten mit den Grundlagen:
# Datentypen

#Wir sehen uns hier mal genauer die Datentypen an
variableA = 1  # Integer aka Ganzzahl
variableB = 1.1  # double bzw float64- float32 gibts hier NICHT zumindest nicht builtin
variableC = "c"  # Was das jetzt wieder?- String- wir benutzen keine chars/ gibts auch nicht als solches in Python
variableD = "Das ist Variable D"  # Eindeutig String

# Wie finden wir heraus was wir an datentypen haben?
print(type(variableA))
print(type(variableB))
print(type(variableC))
print(type(variableD))

# und wenn wir A + 0,1 rechnen?
print(type(variableA + .1))  # tadaaa! dynamisch interpretiert

# ineffizient ohne ende! Beweis folgt später / selber belesen

# Was können wir jetzt noch machen?
eine_Liste = [variableA, variableB]  # Wir speichern mehrere Variablen in einer Liste; wie ein Array aber ineffizient
# bzw nicht sooo schlimm weil: wir halten hier pointer drin

print(eine_Liste[0])  # das item an stelle 0 >[0]< ist das 1. item
# was können wir noch machen?

eine_Liste.append(variableC)
print(eine_Liste)  # wir haben variableC ans ende angehangen!
# und wenn wir das item an stelle 0 nicht mögen?

eine_Liste.pop(0)
print(eine_Liste)  # moment? wir müssen nicht eine_Liste = eine_Liste.pop(0) machen?- nein das ist
# eine inplace-operation
# Veranschaulichung: Eine Liste zeigt immer auf das nächste Objekt in der Liste, A zeigt auf B zeigt auf C...,
# wenn wir jetzt ein Objekt entfernen, dann ersetzen wir aus A->B->C einfach B mit C und haben A->C
# listen sind objekte und pop ist eine Methode die auf der liste aufgerufen wird und sich selbst manipuliert

eine_Liste.extend(range(10))
print(eine_Liste)  # wir können einen generator übergeben und generieren damit objekte

# wir können auch herausfinden, wieviele Elemente in einer Liste sind?


# der boolean
yes = True
no = False
print(yes or no)
print(yes and no)
# kein kommentar

# und nun das dictionary aka Map/ Hashmap:
dictionary = {"key1": "value1", "key2": "value2"} # ein dictionary besteht aus key: value paaren

# indizieren lässt sich das wiefolgt:
print(dictionary["key1"]) # ähnlich wie listen/ arrays

# Aufgaben:
# 1 Lege eine Liste in ein Dictionary & manipuliere diese Liste, während sie im Dictionary ist
# 2 Bringe das Programm zum Absturz
