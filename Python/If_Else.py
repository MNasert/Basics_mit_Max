variable1 = True
variable2 = False
eine_Liste = [True, True, False, True]
#bool, bool & liste von bools
if False in eine_Liste:#if BEDINGUNG: ANWEISUNGEN
    if not variable1:
        print("Passiert offensichtlich nicht")
    else:#else: ANWEISUNGEN
        if variable2:
            print("Das passiert auch nicht!")
        elif True in eine_Liste:#elif BEDINGUNG: ANWEISUNGEN
            print("In der Liste ist wohl mindestens ein True drin!")
        else:
            print("das hätte nicht passieren dürfen")
x = 10
y = 20
#kleiner exkurs auf string.format(*args)
print("{} ist größer als {}".format(x if x > y else y,
                                    y if x > y else x))
#wir formatieren erst die erste {} dann die zweite {}
