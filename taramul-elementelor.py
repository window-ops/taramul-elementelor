import random

# Definirea variabilelor
LATIME_LABIRINT = 12
LUNGIME_LABIRINT = 10
PUNCT_START = (0, 0)
DESTINATIE = (11, 9)
EROI = ['Aqua', 'Sylvanus', 'Ignis', 'Aurum', 'Terra']
INAMICI = 24
CAPCANE = 26
PUNCTE_VIATA_MAXIME_PE_EROU = 100
PUNCTE_VIATA = {erou: PUNCTE_VIATA_MAXIME_PE_EROU for erou in EROI}

# Generarea aleatorie a pozițiilor inamicilor și a capcanelor
pozitii_inamici = [(random.randint(0, LATIME_LABIRINT - 1), random.randint(0, LUNGIME_LABIRINT - 1)) for _ in range(INAMICI)]
pozitii_capcane = [(random.randint(0, LATIME_LABIRINT - 1), random.randint(0, LUNGIME_LABIRINT - 1)) for _ in range(CAPCANE)]


# Funcție pentru verificarea dacă o poziție este validă în labirint
def este_pozitie_valida(pozitie):
    x, y = pozitie
    return 0 <= x < LATIME_LABIRINT and 0 <= y < LUNGIME_LABIRINT


# Funcție pentru a verifica dacă o poziție conține un inamic
def este_pozitie_inamic(pozitie):
    return pozitie in pozitii_inamici


# Funcție pentru a verifica dacă o poziție conține o capcană
def este_pozitie_capcana(pozitie):
    return pozitie in pozitii_capcane


# Funcție pentru a afișa starea curentă a labirintului și a poziției eroilor
def afiseaza_labirint(pozitie_curenta):
    for y in range(LUNGIME_LABIRINT):
        for x in range(LATIME_LABIRINT):
            if (x, y) == pozitie_curenta:
                print('X', end=' ')
            elif (x, y) == PUNCT_START:
                print('S', end=' ')
            elif (x, y) == DESTINATIE:
                print('D', end=' ')
            elif este_pozitie_inamic((x, y)):
                print('E', end=' ')
            elif este_pozitie_capcana((x, y)):
                print('T', end=' ')
            else:
                print('.', end=' ')
        print()


# Funcție pentru a începe jocul
def start_joc():
    print("Bine ați venit în Tărâmul Elementelor! Eroii noștri -", ', '.join(EROI),
          "- au pornit în căutarea Misticii Umbrei.")
    print("(S = start; X = poziția curentă; T = capcană; E = inamic; D = destinație)")
    pozitie_curenta = PUNCT_START
    afiseaza_labirint(pozitie_curenta)
    while pozitie_curenta != DESTINATIE:
        miscare = input("Introduceți direcția de deplasare (sus, jos, stanga, dreapta): ")
        pozitie_noua = pozitie_curenta
        if miscare == "sus":
            pozitie_noua = (pozitie_curenta[0], pozitie_curenta[1] - 1)
        elif miscare == "jos":
            pozitie_noua = (pozitie_curenta[0], pozitie_curenta[1] + 1)
        elif miscare == "stanga":
            pozitie_noua = (pozitie_curenta[0] - 1, pozitie_curenta[1])
        elif miscare == "dreapta":
            pozitie_noua = (pozitie_curenta[0] + 1, pozitie_curenta[1])
        if este_pozitie_valida(pozitie_noua):
            pozitie_curenta = pozitie_noua
            afiseaza_labirint(pozitie_curenta)
            if este_pozitie_inamic(pozitie_curenta):
                print("Un erou întâlnește un inamic și pierde 20 de puncte de viață.")
                erou = EROI[random.randint(0, len(EROI) - 1)]
                PUNCTE_VIATA[erou] -= 20
                if PUNCTE_VIATA[erou] <= 0:
                    print(f"{erou} a fost învins. Jocul s-a încheiat.")
                    return
            elif este_pozitie_capcana(pozitie_curenta):
                print("Un erou a căzut într-o capcană și pierde 15 puncte de viață.")
                erou = EROI[random.randint(0, len(EROI) - 1)]
                PUNCTE_VIATA[erou] -= 15
                if PUNCTE_VIATA[erou] <= 0:
                    print(f"{erou} și toți ceilalți eroi au fost învinși. Jocul s-a încheiat.")
                    return
            else:
                print("Eroii avansează în siguranță.")
        else:
            print("Deplasare invalidă. Încercați din nou.")
    print("Eroul a ajuns la destinație și a învins Mistica Umbrei! Lumină și echilibru au fost restabilite în Tărâmul "
          "Elementelor.")


# Pornirea jocului
start_joc()
