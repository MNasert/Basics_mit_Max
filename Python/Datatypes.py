#Wir sehen uns hier mal genauer die Datentypen an
variableA = 1 #was ist das?
variableB = 1.1#das wissen wir: double bzw float64- float32 gibts hier NICHT zumindest nicht builtin
variableC = "c"#Was das jetzt wieder?- String- wir benutzen keine chars/ gibts auch nicht
variableD = "Das ist Variable D"#Eindeutig String
#Wie finden wir heraus was wir wollen?
#print- schleifen gucken wir uns bald an
print(type(variableA))
print(type(variableB))
print(type(variableC))
print(type(variableD))
#und wenn wir A + 0,1 rechnen?
print(type(variableA +.1))#tadaaa! dynamisch interpretiert ****magic*****
#ineffizient ohne ende! Beweis folgt später / selber belesen
#Was können wir jetzt noch machen?
eine_Liste = [variableA, variableB]#Wir speichern mehrere Variablen in einer Liste; wie ein Array aber ineffizient
#bzw nicht sooo schlimm weil: wir halten hier pointer drin
print(eine_Liste[0])#das 0. item ist das 1. item
#was können wir noch machen?
eine_Liste.append(variableC)
print(eine_Liste)#wir haben variableC ans ende angehangen!
#und wenn wir das item an stelle 0 nicht mögen?
eine_Liste.pop(0)
print(eine_Liste)#moment? wir müssen nicht eine_Liste = eine_Liste.pop(0) machen?- nein ****magic****
#listen sind objekte und pop ist eine Methode die auf der liste aufgerufen wird und sich selbst manipuliert
eine_Liste.extend(range(10))
print(eine_Liste)#noch mehr ****magic****- wir können einen generator übergeben und generieren damit objekte
#und zum schluss
#der boolean
yes = True
no = False
print(yes or no)
print(yes and no)
#kein kommentar nötig ####trivial####