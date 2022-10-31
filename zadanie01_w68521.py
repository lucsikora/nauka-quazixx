#!/usr/bin/env python3
def zadanie01():
    # Funkcja wypisuje dowolny komunikat
    message = "Zadanie domowe w68521"
    return message

def zadanie01a(tresc):
    # Funkcja wypisuje przekazany jej komunikat
    if tresc == '': 
        message = "Nie wpisano treści"
    else:
        message = "Zadanie 01a. Wypisywanie podanej treści: " + tresc
    return message

def zadanie02(liczba1, liczba2):
     # Opisac ladnie co robi ta funkcja, ale najlepiej po angielsku
    wynik = l1+l2 /2
    return wynik


# OUTPUT
print("==== Zadanie 01 - Wypisz komunikat")
print(zadanie01())

print("==== Zadanie 01a - Wypisz podany przez użytkownika komunikat")
# Pewnie pasowało by tu sprawdzać czy ktoś wpisał tekst, jeśli nie, to zeby prosiło go jeszcze raz o wpisanie.
t = input("Podaj dowolne słowo: ")
print(zadanie01a(t))

print("==== Zadanie 02 - Oblicz średnią z dwóch liczb naturalnych")
# Brakuje ci tu funkcji sprawdzajacych czy ktos nie wprowadzi np. stringa 
l1 = int(input("Podaj 1 liczbę "))
l2 = int(input("Podaj 2 liczbę "))
print("średni liczba wynosi", zadanie02(l1,l2))