import time
def test(x):
	q = 0
	n = 0
	for i in range(x):
		q += i
		n = n+q
	return q


if __name__ == "__main__":
	start = time.time()
	for _ in range(100000):
		test(1000)
	end = time.time()
	print(end-start)
#Dynamisch Interpretiert heißt:
#Die Datentypen werden während der Laufzeit bestimmt was viel zeit in anspruch nimmt: kleines beispiel:
#wir haben eine variable x und wir weisen ihr =3 zu was sie zu einem integer macht, d.h. &x hat einen umfang von 32-64 bit
#wollen wir nun in kompilierten sprachen + .1 machen bekommen wir einen fehler; warum?
#wir versuchen auf einen integer einen double zu rechnen- theoretisch möglich; heißt aber dass wir dann einfach binär alle zahlen rüberschieben
#ergo: wir haben bei 3 + 0.1 nicht 3 + 0.1 sondern 3 + 1E-1-> wir haben 11 + 0,0001,1000000000000000000000001- was die rechnung ad absurdum führt
#in interpretierten sprachen erkennt der interpreter: oh datentyp wechseln
#also kopieren wir den inhalt aus &x an ein &x1; wandeln es in einen double um und führen dann die operation durch
#wir haben somit viel mehr speicheroperationen und- speicheroperationen sind die langsamste operation (lesen ausgenommen)