from spillebrett import Spillebrett
from time import sleep


def main():
    rader = int(input("Velg rader: "))
    kolonner = int(input("Velg kolonner: "))

    game = Spillebrett(rader, kolonner)

    same = 0
    while same <= 10:
        game.tegnBrett()
        print(f"Levende celler: {game.antallLevende()}")
        print(f"Generasjon:     {game.generasjonsTall()}")
        print()
        sleep(0.2)

        levendeFoer = game.antallLevende()
        game.oppdatering()
        levendeEtter = game.antallLevende()

        if levendeFoer == levendeEtter:
            same += 1
        else:
            same = 0

    print("inf loop")


main()
