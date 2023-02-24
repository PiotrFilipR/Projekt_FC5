
szkola = {
    "uczniowie": [],
    "nauczyciele": [],
    "wychowawcy": [],
}


class Uczen:

    def __init__(self, imie, nazwisko, klasa):
        self.imie = imie
        self.nazwisko = nazwisko
        self.klasa = klasa


class Nauczyciel:

    def __init__(self, imie, nazwisko, przedmiot, klasy):
        self.imie = imie
        self.nazwisko = nazwisko
        self.przedmiot = przedmiot
        self.klasy = klasy


class Wychowawca:

    def __init__(self, imie, nazwisko, klasa):
        self.imie = imie
        self.nazwisko = nazwisko
        self.klasa = klasa


while True:
    wybor = input("1. Utwórz \n"
                  "2. Zarządzaj \n"
                  "3. Koniec \n"
                  "Wciśnij odpowiednią liczbę, aby wybrać polecenie... "
                  )

    # 1. Utwórz

    if wybor == "1":
        wybor_utworz = input("1. Uczeń \n"
                             "2. Nauczyciel \n"
                             "3. Wychowawca \n"
                             "4. Powrót \n"
                             "Wciśnij odpowiednią liczbę, aby wybrać polecenie... "
                             )
        if wybor_utworz == "1":

            print("Podaj imię ucznia... ")
            imie = input()
            print("Podaj nazwisko ucznia... ")
            nazwisko = input()
            print("Podaj klasę do której uczęszcza uczeń... ")
            klasa = input()

            szkola["uczniowie"].append(Uczen(imie, nazwisko, klasa))

        elif wybor_utworz == "2":

            print("Podaj imię nauczyciela... ")
            imie = input()
            print("Podaj nazwisko nauczyciela... ")
            nazwisko = input()
            print("Podaj przedmiot którego uczy... ")
            przedmiot = input()

            klasy = []
            print("Jakie klasy naucza? Po każdej klasie należy nacisnąć enter... ")
            klasa = input()
            while (klasa != ""):
                klasy.append(klasa)
                klasa = input()

            szkola["nauczyciele"].append(Nauczyciel(imie, nazwisko, przedmiot, klasy))

        elif wybor_utworz == "3":
            print("Imie wychowawcy?")
            imie = input()
            print("Nazwisko wychowawcy?")
            nazwisko = input()
            print("Jaka klase prowadzi?")
            klasa = input()

            szkola["wychowawcy"].append(Wychowawca(imie, nazwisko, klasa))

        elif wybor_utworz == "4":
            pass
        else:
            print("Wybrano złe polecenie.")

    # 2. Zarządzaj

    elif wybor == "2":
        wybor_zarzadzaj = input("1. Klasa \n"
                                "2. Uczeń \n"
                                "3. Nauczyciel \n"
                                "4. Wychowawca \n"
                                "5. Powrót \n"
                                "Wciśnij odpowiednią liczbę, aby wybrać polecenie... "
                                )
        if wybor_zarzadzaj == "1":
            print("Podaj klasę... ")
            zadana_klasa = input()
            for uczen in szkola["uczniowie"]:
                if uczen.klasa == zadana_klasa:
                    print(uczen.imie + " " + uczen.nazwisko)
            for wychowawca in szkola["wychowawcy"]:
                if wychowawca.klasa == zadana_klasa:
                    print(f"Wychowawca klasy {zadana_klasa} - {wychowawca.imie} {wychowawca.nazwisko}")

        elif wybor_zarzadzaj == "2":

            print("Podaj imię ucznia: ")
            imie_ucznia = input()
            print("Podaj nazwisko ucznia: ")
            nazwisko_ucznia = input()

            for uczen in szkola["uczniowie"]:
                if uczen.imie == imie_ucznia and uczen.nazwisko == nazwisko_ucznia:
                    for nauczyciel in szkola["nauczyciele"]:
                        if uczen.klasa in nauczyciel.klasy:
                            print(f"Przedmioty ucznia {imie_ucznia} {nazwisko_ucznia}: ")
                            print(f"{nauczyciel.przedmiot}, prowadzony przez {nauczyciel.imie} {nauczyciel.nazwisko}")

        elif wybor_zarzadzaj == "3":
            print("Podaj imię nauczyciela: ")
            imie_nauczyciela = input()
            print("Podaj nazwisko nauczyciela: ")
            nazwisko_nauczyciela = input()

            for nauczyciel in szkola["nauczyciele"]:
                if nauczyciel.imie == imie_nauczyciela and nauczyciel.nazwisko == nazwisko_nauczyciela:
                    print(nauczyciel.klasy)

        elif wybor_zarzadzaj == "4":
            print("Podaj imię wychowawcy: ")
            imie_wychowawcy = input()
            print("Podaj nazwisko wychowawcy: ")
            nazwisko_wychowawcy = input()

            for wychowawca in szkola["wychowawcy"]:
                if wychowawca.imie == imie_wychowawcy and wychowawca.nazwisko == nazwisko_wychowawcy:
                    print(f"{imie_wychowawcy} {nazwisko_wychowawcy} jest wcyhowawcą klasy {wychowawca.klasa}")
                    print("Uczniowie klasy: ")
                    klasa = wychowawca.klasa
                    for uczen in szkola['uczniowie']:
                        if uczen.klasa == klasa:
                            print(f"{uczen.imie} {uczen.nazwisko}")
                else:
                    print("Podano złe imię i nazwisko")

        elif wybor_zarzadzaj == "5":
            pass
        else:
            print("Wybrano złe polecenie.")

    elif wybor == "3":
        break

    else:
        print("Wybrano złe polecenie.")