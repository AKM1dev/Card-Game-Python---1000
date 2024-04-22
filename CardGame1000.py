import random
import os
trefl = 0
karo = 0
kier = 0
pik = 0
PunktyG1 = 0
PunktyG2 = 0
ZnakKartyG1 = ()
ZnakKartyG2 = ()
KolorKartyG1 = ()
KolorKartyG2 = ()
TaliaKartG1 = []
TaliaKartG2 = []
ZbiórKartG1 = []
ZbiórKartG2 = []
Musek1 = []
Musek2 = []
PoprawnaKarta = True
x = True
BidGracza = "gracza 1"
BidG1 = 100
TerazBid = 100
NastępnyBid = TerazBid + 10
WartościKart = {"dziewiątka": 0, "dziesiątka": 10, "walet": 2, "dama": 3, "król": 4, "as": 11}
def DobierzKartę():
    TypKarta = random.randint(1, 6)
    if TypKarta == 1:
        TypKarta = "dziewiątka"
    elif TypKarta == 2:
        TypKarta = "dziesiątka"
    elif TypKarta == 3:
        TypKarta = "walet"
    elif TypKarta == 4:
        TypKarta = "dama"
    elif TypKarta == 5:
        TypKarta = "król"
    elif TypKarta == 6:
        TypKarta = "as"
    Kolor = random.randint(1, 4)
    if Kolor == 1:
        Kolor = "trefl"
    elif Kolor == 2:
        Kolor = "karo"
    elif Kolor == 3:
        Kolor = "kier"
    elif Kolor == 4:
        Kolor = "pik"
    Karta = f"{TypKarta} {Kolor}"
    return Karta
while x == True:
    if len(Musek1) == 2:
        break
    KMusek1 = DobierzKartę()
    if KMusek1 not in Musek1:
        Musek1.append(KMusek1)
while x == True:
    if len(Musek2) == 2:
        break
    KMusek2 = DobierzKartę()
    if KMusek2 not in Musek1 and KMusek2 not in Musek2:
        Musek2.append(KMusek2)
while x == True:
    if len(TaliaKartG1) == 10:
        break
    Karta = DobierzKartę()
    if Karta not in Musek1 and Karta not in Musek2 and Karta not in TaliaKartG1:
        TaliaKartG1.append(Karta)
while x == True:
    if len(TaliaKartG2) == 10:
        break
    Karta = DobierzKartę()
    if Karta not in Musek1 and Karta not in Musek2 and Karta not in TaliaKartG1 and Karta not in TaliaKartG2:
        TaliaKartG2.append(Karta)
Bid = input(f"{TerazBid} {BidGracza}, podbijesz do {NastępnyBid}? [Y/N] ")
if Bid == "Y":
    BidGracza = "gracza 2"
    TerazBid = NastępnyBid
    NastępnyBid = NastępnyBid + 10
    while x == True:
        Bid = input(f"{TerazBid} {BidGracza}, podbijesz do {NastępnyBid}? [Y/N] ")
        if Bid != "Y":
            break
        if Bid == "Y":
            TerazBid = NastępnyBid
            NastępnyBid = NastępnyBid + 10
            if BidGracza == "gracza 1":
                BidGracza = "gracza 2"
            else:
                BidGracza = "gracza 1"
            if Bid != "Y":
                if BidGracza == "gracza 1":
                    Bidder = "gracza 1"
                if BidGracza == "gracza 2":
                    Bidder = "gracz 2"
                break
while x == True:
    if BidGracza == "gracza 1":
        while x == True:
            WybórMusek = int(input("Który musek wybierzesz 1 czy 2? [1/2] "))
            if WybórMusek == 1:
                for i in Musek1:
                    TaliaKartG1.append(i)
                break
            if WybórMusek == 2:
                for i in Musek2:
                    TaliaKartG1.append(i)
                break
            else:
                print("zły musek")
    if BidGracza == "gracza 2":
        while x == True:
            WybórMusek = int(input("Który musek wybierzesz 1 czy 2? [1/2] "))
            if WybórMusek == 1:
                for i in Musek1:
                    TaliaKartG2.append(i)
                break
            if WybórMusek == 2:
                for i in Musek2:
                    TaliaKartG2.append(i)
                break
            else:
                print("zły musek")
    break
while x == True:
    if BidGracza == "gracza 1":
        while x == True:
            WybórOddania = input(f"Którą kartę oddasz graczowi 2? {TaliaKartG1} ")
            if WybórOddania in TaliaKartG1:
                TaliaKartG2.append(WybórOddania)
                TaliaKartG1.remove(WybórOddania)
                break
            else:
                print("Nie posiadasz tej karty")
    if BidGracza == "gracza 2":
        while x == True:
            WybórOddania = input(f"Którą kartę oddasz graczowi 1? {TaliaKartG2} ")
            if WybórOddania in TaliaKartG2:
                TaliaKartG1.append(WybórOddania)
                TaliaKartG2.remove(WybórOddania)
                break
            else:
                print("Nie posiadasz tej karty")
    break
TaliaKartG1.sort()
TaliaKartG2.sort()
while x == True:
    if BidGracza == "gracza 1":
        while x == True:
            KartaG1 = input(f"jaką kartę chcesz zagrać? {TaliaKartG1} ")
            if KartaG1 not in TaliaKartG1:
                print("Nie posiadasz Tej Karty")
            else:
                TaliaKartG1.remove(KartaG1)
                ZnakKartyG1 = KartaG1.split()[0]
                KolorKartyG1 = KartaG1.split()[1]
                KartaGG1 = WartościKart[KartaG1.split()[0]]
                os.system("cls")
                break
        while x == True:
            KartaG2 = input(f"jaką kartę chcesz zagrać? {TaliaKartG2} ")
            if KartaG2 not in TaliaKartG2:
                print("Nie posiadasz Tej Karty")
            else:
                TaliaKartG2.remove(KartaG2)
                ZnakKartyG2 = KartaG2.split()[0]
                KolorKartyG2 = KartaG2.split()[1]
                KartaGG2 = WartościKart[KartaG2.split()[0]]
                os.system("cls")
                break
    if BidGracza == "gracza 2":
        while x == True:
            KartaG2 = input(f"jaką kartę chcesz zagrać? {TaliaKartG2} ")
            if KartaG2 not in TaliaKartG2:
                print("Nie posiadasz Tej Karty")
            else:
                TaliaKartG2.remove(KartaG2)
                ZnakKartyG2 = KartaG2.split()[0]
                KolorKartyG2 = KartaG2.split()[1]
                KartaGG2 = WartościKart[KartaG2.split()[0]]
                os.system("cls")
                break
        while x == True:
            KartaG1 = input(f"jaką kartę chcesz zagrać? {TaliaKartG1} ")
            if KartaG1 not in TaliaKartG1:
                print("Nie posiadasz Tej Karty")
            else:
                TaliaKartG1.remove(KartaG1)
                ZnakKartyG1 = KartaG1.split()[0]
                KolorKartyG1 = KartaG1.split()[1]
                KartaGG1 = WartościKart[KartaG1.split()[0]]
                os.system("cls")
                break
    if KartaGG1 == KartaGG2:
        if BidGracza == "gracza 1":
            ZbiórKartG1.append(KartaG1)
            ZbiórKartG1.append(KartaG2)
        if BidGracza == "gracza 2":
            ZbiórKartG2.append(KartaG1)
            ZbiórKartG2.append(KartaG2)
    else:
        if BidGracza == "gracza 1":
            if ZnakKartyG1 == "król" or ZnakKartyG1 == "dama":
                    print("Dobrze")
                    if f"król {KolorKartyG1}" in TaliaKartG1 or f"dama {KolorKartyG1}":
                        if KolorKartyG1 == "kier" and kier == 0:
                            PunktyG1 = PunktyG1 + 100
                            trefl = 1
                            KolorDominujący = "kier"
                        elif KolorKartyG1 == "karo" and karo == 0:
                            PunktyG1 = PunktyG1 + 80
                            trefl = 1
                            KolorDominujący = "karo"
                        elif KolorKartyG1 == "trefl" and trefl == 0:
                            PunktyG1 = PunktyG1 + 60
                            trefl = 1
                            KolorDominujący = "trefl"
                        elif KolorKartyG1 == "pik" and pik == 0:
                            PunktyG1 = PunktyG1 + 40
                            pik = 1
                            KolorDominujący = "pik"
        if BidGracza == "gracza 2":
            if ZnakKartyG2 == "król" or ZnakKartyG2 == "dama":
                    if f"król {KolorKartyG2}" in TaliaKartG2 or f"dama {KolorKartyG2}":
                        if KolorKartyG2 == "kier" and kier == 0:
                            PunktyG2 = PunktyG2 + 100
                            trefl = 1
                            KolorDominujący = "kier"
                        elif KolorKartyG2 == "karo" and karo == 0:
                            PunktyG2 = PunktyG2 + 80
                            trefl = 1
                            KolorDominujący = "karo"
                        elif KolorKartyG2 == "trefl" and trefl == 0:
                            PunktyG2 = PunktyG2 + 60
                            trefl = 1
                            KolorDominujący = "trefl"
                        elif KolorKartyG2 == "pik" and pik == 0:
                            PunktyG2 = PunktyG2 + 40
                            pik = 1
                            KolorDominujący = "pik"
        if BidGracza == "gracza 1":
            if KolorKartyG2 == KolorDominujący:
                ZbiórKartG2.append(KartaG1)
                ZbiórKartG2.append(KartaG2)
                BidGracza = "gracza 2"
        if BidGracza == "gracza 2":
            if KolorKartyG1 == KolorDominujący:
                ZbiórKartG1.append(KartaG1)
                ZbiórKartG1.append(KartaG2)
                BidGracza = "gracza 1"
        if BidGracza == "gracza 1":
            if KolorKartyG2 != KolorKartyG1:
                ZbiórKartG1.append(KartaG1)
                ZbiórKartG1.append(KartaG2)
        if BidGracza == "gracza 2":
            if KolorKartyG1 != KolorKartyG2:
                ZbiórKartG2.append(KartaG1)
                ZbiórKartG2.append(KartaG2)
        if KolorKartyG1 == KolorKartyG2:
            if KartaGG1 > KartaGG2:
                ZbiórKartG1.append(KartaG1)
                ZbiórKartG1.append(KartaG2)
                BidGracza = "gracza 1"
            else:
                ZbiórKartG2.append(KartaG1)
                ZbiórKartG2.append(KartaG2)
                BidGracza = "gracza 2"
        if len(TaliaKartG1) == 0 and len(TaliaKartG2) == 0:
            for i in ZbiórKartG1:
                PunktyG1 = PunktyG1 + WartościKart[i.split()[0]]
            for i in ZbiórKartG2:
                PunktyG2 = PunktyG2 + WartościKart[i.split()[0]]
            print(f"finalna punktacja: G1-{PunktyG1} G2-{PunktyG2}")
            break
    print(f"punkty gracza 1: {PunktyG1}")
    print(f"punkty gracza 2: {PunktyG2}")
    print(f"Kraty gracza 1: {ZbiórKartG1}")
    print(f"Kraty gracza 2: {ZbiórKartG2}")