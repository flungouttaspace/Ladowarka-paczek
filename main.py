def main():
    while True:
        try:
            liczba_elementow = int(input("Ile elementów chcesz wysłać? "))
            if liczba_elementow >= 0:
                break
        except ValueError:
            pass
        print("Podaj nieujemną liczbę całkowitą.")

    paczki = []
    aktualna_waga = 0

    for numer in range(1, liczba_elementow + 1):
        while True:
            try:
                waga = float(
                    input(f"Podaj wagę elementu {numer} (1–10 kg): ")
                    .replace(",", ".")
                )
                break
            except ValueError:
                print("Podaj wagę jako liczbę.")

        if not 1 <= waga <= 10:
            print("Waga poza zakresem. Kończę dodawanie i wysyłam paczki.")
            break

        if aktualna_waga + waga > 20:
            paczki.append(aktualna_waga)
            aktualna_waga = 0

        aktualna_waga += waga

    # Wysyłamy ostatnią paczkę tylko wtedy, gdy zawiera towar.
    if aktualna_waga > 0:
        paczki.append(aktualna_waga)

    liczba_paczek = len(paczki)
    suma_wag = sum(paczki)
    puste_kilogramy = liczba_paczek * 20 - suma_wag

    print("\nPodsumowanie:")
    print(f"Liczba wysłanych paczek: {liczba_paczek}")
    print(f"Liczba wysłanych kilogramów: {suma_wag:g} kg")
    print(f"Suma pustych kilogramów: {puste_kilogramy:g} kg")

    if paczki:
        najlzejsza = min(paczki)
        numer_paczki = paczki.index(najlzejsza) + 1
        print(
            f"Najwięcej pustych kilogramów ma paczka {numer_paczki}: "
            f"{20 - najlzejsza:g} kg"
        )
    else:
        print("Nie wysłano żadnej paczki.")


if __name__ == "__main__":
    main()
