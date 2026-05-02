#numer albumu: s30679
#Data: 02.05.2026

#Krótki opis programu:
#Program służy do generowania, zapisywania i analizy sekwencji DNA z wykorzystaniem formatu Fasta.

import random

def generate_sequence(length:int) -> str:
    """Funkcja zwraca pseudolosową sekwencję DNA o wskazanej długości, która
    jest złożona z nukleotydów A, C, T, G.
    """
    sekwencja=""
    for i in range(length):
        match random.randint(1,4):
            case 1:
                sekwencja+="A"
            case 2:
                sekwencja+="C"
            case 3:
                sekwencja+="T"
            case 4:
                sekwencja+="G"
    return sekwencja

def validate_positive_int(prompt: str = "Jako długość sekwencji podaj liczbę całkowitą z wybranego zakresu (podstawowo od 1 do 100.000): ", min_val: int = 1, max_val: int = 100_000) -> int:
    """Funkcja pobiera od użytkownika długość sekwencji jako liczbę całkowitą z wybranego przez użytkownika zakresu, który wynosi początkowo od 1 do 100.000"""
    slowa_uzytkownika=input(prompt)
    try:
        dlugosc = int(slowa_uzytkownika)
        return dlugosc
    except ValueError:
        print("Miałeś/aś podać liczbę całkowitą z zakresu od 1 do 100.000 a nie to: ")
        print(slowa_uzytkownika)
        return validate_positive_int()

def fasta_ID(ID: str, description:str = "") -> tuple[str,str]:
    """Funkcja pobiera od użytkownika ID pliku fasta (bez białych znaków co jest sprawdzane w funkcji) oraz opis."""
    for i in ID:
        if ID[i]==' ' or ID[i]=='\t' or ID[i]=='\n':
            raise ValueError("ID nie może zawierać znaków białych!")
    return ID, description

#def calculate_stats(sequence: str) -> dict:
#    """"""

#def insert_name(sequence: str, name: str) -> str:
#    """"""

#def format_fasta(seq_id: str, description: str, sequence: str, line_width: int = 80) -> str:
#    """"""