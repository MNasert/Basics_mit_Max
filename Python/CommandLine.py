import argparse# wir brauchen das!

parser = argparse.ArgumentParser(description="Wir haben einen Argparser!")#wir instanzieeren einen argparser
parser.add_argument("zahlen", metavar="n", type=float, nargs="+")#wir geben ihm ein neues argument zum verwalten

#beliebige Methode- dummy
def plus(liste):
    q = 0
    for i in liste:
        q += i
    return q


#wir parsen alle argumente
args = parser.parse_args()
print(plus(args.zahlen))#und geben uns das ergebnis aus!



