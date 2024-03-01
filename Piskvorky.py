def vyhodnot(pole):
    if ('xxx' in pole) == True:
        return 'x'
    elif ('ooo' in pole) == True:
        return 'o'
    elif ('-' not in pole) == True:
        return '!'
    else:
        return '-'


def tah(pole, cislo_policka, symbol):
    """
    Vrátí pouze nové herní pole s daným symbolem umístěným na danou pozici
    """
    return pole[:cislo_policka] + symbol + pole[cislo_policka + 1:]


def tah_hrace(pole, hrac):
    """
    Přebírá herní pole a symbol hráče
    """
    while True:
        pozice = int(input("Zadej pozici, na kterou chceš hrát: "))    # otázka na jakou pozici hrát
        if (pozice < 0) or (pozice > 19):   # kontrola zadané pozice od/do
            print("Pozice musí být v rozmezí 0 až 19, zadej znovu.")
        elif (pole[pozice] != "-"):    # kontrola, zda pozice není již obsazená
            print(f"Pozice {pozice} už je obsazená, zadej znovu.")
        else:   # v případě, že pozice není obsazená, zavolá funkci tah()
            return tah(pole, pozice, hrac)




pole = 20 * "-"
pole = tah_hrace(pole, "x")
# tah_pocitace(pole, "o")
print(pole)