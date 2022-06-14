# Tekstinėse bylose yra surašyti abiturientų vardai. Grupės kuratorė sugalvojo mokyklos baigimo
# proga padovanoti abiturientams vardinius ženkliukus. Ženkliukus gaminanti įmonė paprašė mokinių
# sąrašo, kuriame būtų surašyti mokinių vardai ir ženkliukų kiekis, kuriuos reikia pagaminti su šiuo vardu.

# 1 užduotis. Parašykite programą, kuri sukurtų bylą sarasas.txt, kurioje būtų saugomi duomenys (duomenis
# saugoti programoje  naudokite map duomenų tipą, kur indeksas yra mokinio vardas, o reikšmė – ženkliukų,
# kurios reikia pagaminti su šiuo vardu, kiekis. Duomenims išrinkti naudokite set tipą. Taip pat galite
# naudoti ir list tipo duomenis.).


def nuskaityti_duomenis(failo_adresas):
    """Funkcija skirta nuskaityti tekstini dokumenta, kuri perduodame kaip parametra ir grazinti jame
    buvusi teksta kaip sarasa"""
    with open (failo_adresas, mode="r") as failas:
        vardai = []
        sarasas = failas.readlines()
        for vardas in sarasas:
            vardai.append(vardas.strip("\n"))
        return vardai


a_klases_mokiniai = nuskaityti_duomenis("12a.txt")
b_klases_mokiniai = nuskaityti_duomenis("12b.txt")
c_klases_mokiniai = nuskaityti_duomenis("12c.txt")
d_klases_mokiniai = nuskaityti_duomenis("12d.txt")
e_klases_mokiniai = nuskaityti_duomenis("12e.txt")
f_klases_mokiniai = nuskaityti_duomenis("12f.txt")
g_klases_mokiniai = nuskaityti_duomenis("12g.txt")

bendras_sarasas = tuple(a_klases_mokiniai + b_klases_mokiniai + c_klases_mokiniai + d_klases_mokiniai +
                        e_klases_mokiniai + f_klases_mokiniai + g_klases_mokiniai)

unikalus_vardai = tuple(set(bendras_sarasas))

# atspausdinam sarasa vardu ir to vardo zenkliuku kieki sarasas.txt
vardiniai_zenkliukai = {}
with open ("sarasas.txt", mode="w") as failas_2:
    for unikalus_vardas in unikalus_vardai:
        vardinis_zenkliukas = bendras_sarasas.count(unikalus_vardas)
        failas_2.write(f"{unikalus_vardas} - {vardinis_zenkliukas} vnt.\n")
        vardiniai_zenkliukai[unikalus_vardas] = vardinis_zenkliukas


# 2 užduotis. Programa dar turi suformuoti bylą saskaita.txt, kurioje pateikiamas ženkliukų kiekis ir
# kaina, kai žinoma, kad vienas ženkliukas kainuoja 5 eur. Jei moksleivių tuo pačiu vardu yra daugiau nei
# trys, tai  ketvirtas ženkliukas kainuoja 4 eur., penktas – 3 eur., šeštas – 2 eur., ir visi kiti
# ženkliukai po 1 eur. (pvz. Jonas  8, tai mokėti reikia 5 + 5 + 5 + 4 + 3 + 2 + 1 + 1 = 26)


def sarasas_is_int (duotas_kiekis, pradine_kaina):
    """Funkcija grazinanti sarasa, kurio ilgis lygus perduodam per parametra skaiciui "duotas_kiekis", o elementai
    lygus, per parametra perduodamam kitam skaiciui "pradine_kaina" - nuolaida"""
    sarasas_su_nuolaida = []
    for i in range(duotas_kiekis):
        if i < 3:
            sarasas_su_nuolaida.append(pradine_kaina)
        elif i < 4:
            sarasas_su_nuolaida.append(pradine_kaina - 1)
        elif i < 5:
            sarasas_su_nuolaida.append(pradine_kaina - 2)
        elif i < 6:
            sarasas_su_nuolaida.append(pradine_kaina - 3)
        else:
            sarasas_su_nuolaida.append(pradine_kaina - 4)

    return sarasas_su_nuolaida


zenkliuku_kainos = {}
bendra_suma = 0
with open("saskaita.txt", mode="w") as failas_3:
    for key in vardiniai_zenkliukai:
        kaina = sum(sarasas_is_int(vardiniai_zenkliukai[key], 5))
        zenkliuku_kainos[key] = kaina
        bendra_suma += kaina
        failas_3.write(f"{key} - {vardiniai_zenkliukai[key]} vnt - {kaina} Eur\n")
    failas_3.write(f"\nviso: {bendra_suma} Eur")
