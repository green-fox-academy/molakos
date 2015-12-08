import re

def filereader():
    with open("proba.txt", "r") as inp:
        text = inp.read()
        v = re.sub(r'is', 'Roland', text)
        print(v)

def find_numbers():
    with open('proba.txt', 'r') as inp:
        text = inp.read()
        

filereader()
