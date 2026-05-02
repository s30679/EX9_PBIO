#numer albumu: s30679
#Data: 01.05.2026

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

#def calculate_stats(sequence: str) -> dict:
#    """"""

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

#def insert_name(sequence: str, name: str) -> str:
#    """"""

#def format_fasta(seq_id: str, description: str, sequence: str, line_width: int = 80) -> str:
#    """"""

validate_positive_int()