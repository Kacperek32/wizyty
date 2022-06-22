import sys
import logging

hello = input("Podaj imię nazwisko: ")



if len(hello) > 0:
    print(len(hello))

class BaseContact:

    __data = []

    def create_contacts(self):
        imię = input("Imię: ")
        nazwisko = input("Nazwisko: ")
        telefon = input("Telefon: ")
        mail = input("Adres mail: ")
        priorytet = input("Typ kontaktu: ")
        stanowisko = input("Stanowisko: ")
        firma = input("Firma: ")

        newWizytówka = wizytówka(imię, nazwisko, telefon, mail, priorytet, stanowisko, firma)
        self.__data.append(newWizytówka)

    def __repr__(self):
        return wizytówka

    def __str__(self):
        return wizytówka
    
    def showwiz(self):
        print("Oto wizytówka: ")
        for i in self.__data:
            if i.typ == "wizytówka":
                print(i)

class BussinessContact(BaseContact):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

from abc import ABC, abstractmethod
class thing(ABC):
    def __init__ (self, typ, priorytet):
        self.typ = typ
        self.priorytet = priorytet
    @abstractmethod
    def __str__(self):
        pass

    def __len__(self):
        return len

class wizytówka(thing):
    
    def __init__(self, imię, nazwisko, telefon, mail, priorytet, stanowisko, firma):
        super().__init__("wizytówka", priorytet)
        self.imię = imię
        self.nazwisko = nazwisko
        self.telefon = telefon
        self.mail = mail
        self.priorytet = priorytet
        self.stanowisko = stanowisko
        self.firma = firma

    def __str__(self):
        info = self.imię + self.nazwisko + "\n"
        info += self.telefon + "\n"
        info += self.mail + "\n"
        info += self.priorytet + "\n"
        info += self.stanowisko + "\n"
        info += self.firma + "\n"
        return  info

number_priv = [+4832123562]
number_firm = [+4831232124]
names = ("Janek ")

baza = BaseContact()

while True:

    z = input()

    print("(1) Dodać wizytówkę, (2) Wyświetlić wizytówki, (3) Dzwoń na prywatny, (4) Dzwoń na firmowy")
    
    if z == "1": baza.create_contacts()
    if z == "2": baza.showwiz()
    if z == "3": print(f"Wybieram number {number_priv} do {names}")
    if z == "4": print(f"Wybieram numer {number_firm} do {names}")
