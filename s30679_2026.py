#numer albumu: s30679
#Data: 03.05.2026

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
        if counter!=0 or ID_fasta=="":
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
        if(spot_in_seq%line_width==0 and spot_in_seq!=0):
            text+="\n"
        text+=sequence[i]
        spot_in_seq+=1
    return text

def calculate_stats(sequence: str) -> dict:
    """Funkcja zwraca słownik statystyk sekwencji, procent występowania nukleotydów oraz GC."""
    dict_count={'A':0,'C':0,'G':0,'T':0,'ALL':0}
    for i in sequence:
        match i:
            case 'A':
                dict_count["A"]+=1
                dict_count["ALL"]+=1
            case 'C':
                dict_count["C"]+=1
                dict_count["ALL"]+=1
            case 'G':
                dict_count["G"]+=1
                dict_count["ALL"]+=1
            case 'T':
                dict_count["T"]+=1
                dict_count["ALL"]+=1
    
    dict_ans={
        'A': round(dict_count['A']/dict_count["ALL"]*100,2),
        'C':round(dict_count['C']/dict_count["ALL"]*100,2),
        'G':round(dict_count['G']/dict_count["ALL"]*100,2),
        'T':round(dict_count['T']/dict_count["ALL"]*100,2),
        "GC":round((dict_count['G']+dict_count['C'])/dict_count["ALL"]*100,2)
        }
    return dict_ans

def insert_name(sequence: str, name: str) -> str:
    """Funkcja wstawia imię w losową pozycję sekwencji, zapisane małymi literami."""
    name=name.lower()
    pos=random.randint(0, len(sequence))
    seq_left=sequence[:pos]
    seq_right=sequence[pos:]
    return seq_left+name+seq_right

#1
def butch_mode():
    """Generuje x sekwencji w pętli, każdą z unikalnym ID (Seq_001, Seq _002, itd.) i zapisuje wszystkie do jednego pliku FASTA (multi-FASTA)."""
    state=True
    while state:
        no_of_seq=input("Podaj liczbę generowanych sekwencji: ")
        try:
            number = int(no_of_seq)
            if(number<=0):
                print(f"Miałeś/aś podać liczbę całkowitą większą od zera!")
                print()
            else:
                state=False
        except ValueError:
            print(f"Miałeś/aś podać liczbę całkowitą większą od zera!")
            print()

    fasta_content=""
    for i in range(number):
        length=validate_positive_int()
        if(i<9):
            seq_id="Seq_00"+str(i+1)
        elif(i<99):
            seq_id="Seq_0"+str(i+1)
        else:
            seq_id="Seq_"+str(i+1)
        sequence=generate_sequence(length)
        fasta_content+=format_fasta(seq_id=seq_id,sequence=sequence)+"\n"
    fasta_filename="multi_seq.fasta"
    with open(fasta_filename, "w", encoding="utf-8") as f:
        f.write(fasta_content)

#4
def generate_complement_sequence(sequence:str) -> str:
    """Funkcja zwraca komplementarną sekwencję DNA do wskazanej."""
    sekwencja=""
    for i in sequence:
        match i:
            case 'A':
                sekwencja+="T"
            case 'C':
                sekwencja+="G"
            case 'T':
                sekwencja+="A"
            case 'G':
                sekwencja+="C"
    return sekwencja

def generate__rev_comp_seq(sequence:str) -> str:
    """Funkcja zwraca odwrotnie komplementarną sekwencję DNA do wskazanej."""
    sekwencja=generate_complement_sequence(sequence)
    return "".join(reversed(sekwencja))

#3
def motive_search(sequence:str)-> tuple:
    """"""

#5
def gen_trans_in_silic(sequence:str)-> str:
    """"""

def main():
    """Główne wywoływanie funkcjonalności programu."""
    length=validate_positive_int()
    seq_id=validate_fasta_ID()
    description=input("Podaj opis sekwencji (opcjonalnie, Enter aby pominąć): ").strip()
    name=input("Podaj imię: ").strip()
    sequence=generate_sequence(length)
    stats=calculate_stats(sequence)
    sequence_with_name=insert_name(sequence, name)
    fasta_content=format_fasta(seq_id, sequence_with_name, description)
    fasta_filename=seq_id+".fasta"
    with open(fasta_filename, "w", encoding="utf-8") as f:
        f.write(fasta_content)
    
    print("")
    print("Sekwencja z imieniem: "+sequence_with_name)
    print("")
    print("Sekwencja zapisana do pliku: "+fasta_filename)
    print("Statystyki sekwencji (n="+str(length)+"):")
    print("A:          "+str(stats["A"])+"%")
    print("C:          "+str(stats["C"])+"%")
    print("G:          "+str(stats["G"])+"%")
    print("T:          "+str(stats["T"])+"%")
    print("GC-content: "+str(stats["GC"])+"%")

    print("Bonus functions:")
    print("1:")
    butch_mode()

    print("4:")
    print("Podstawowa sekwencja:")
    print(sequence)
    print("Komplementarna sekwencja:")
    comp_seq=generate_complement_sequence(sequence=sequence)
    print(comp_seq)
    print("Odwrotnie komplementarna sekwencja:")
    rev_comp_seq=generate__rev_comp_seq(sequence=sequence)
    print(rev_comp_seq)


if __name__ == "__main__":
    main()
