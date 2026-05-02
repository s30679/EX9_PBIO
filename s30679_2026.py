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
    while True:
        user_input=input(prompt)
        try:
            length = int(user_input)
            if(min_val<=length<=max_val):
                return length
            else:
                print(f"Miałeś/aś podać liczbę całkowitą z zakresu od {min_val} do {max_val} a nie to: ")
                print(user_input)
                print()
        except ValueError:
            print(f"Miałeś/aś podać liczbę całkowitą z zakresu od {min_val} do {max_val} a nie to: ")
            print(user_input)
            print()

def validate_fasta_ID(prompt: str ="Podaj ID pliku fasta. ID nie może zawierać znaków białych!") -> str:
    """Funkcja waliduje ID pliku fasta (bez białych znaków co jest sprawdzane w funkcji)."""
    while True:
        ID_fasta = input(prompt)
        counter=0
        for i in ID_fasta:
            if i==' ' or i=='\t' or i=='\n':
                counter+=1
        if counter!=0:
            print("ID nie może zawierać znaków białych!")
            print()
        else:
            return ID_fasta
    
def format_fasta(seq_id: str, sequence: str, description: str="", line_width: int = 80) -> str:
    """Funkcja zwraca tekst string do pliku fasta z podanym przez użytkownika ID oraz opisem."""
    header=">"+seq_id+" "+description
    spot_in_seq=0
    text=header+"\n"
    for i in range(len(sequence)):
        if(spot_in_seq%line_width==0):
            text+="\n"
        text+=sequence[i]
        spot_in_seq+=1
    return text


#def calculate_stats(sequence: str) -> dict:
#    """"""

#def insert_name(sequence: str, name: str) -> str:
#    """"""
