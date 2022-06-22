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
    def __init__(self, company, firm, place, *args, **kwargs):
        super().__init__(*args, **kwargs)

from abc import ABC, abstractmethod
class przedmiot(ABC):
    def __init__ (self, typ, priorytet):
        self.typ = typ
        self.priorytet = priorytet
    @abstractmethod
    def __str__(self):
        pass

    def __len__(self):
        return len
