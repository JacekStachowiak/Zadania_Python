#  wypisz wszystkie elementy listy, które są mniejsze niż 5
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for l in a:
    if l < 5:
        print(int(l))

print('=========================================')
print([l for l in a if l < 5])
print('==============================================')

# Dodatki:
# Zamiast drukować elementy jeden po drugim, stwórz nową listę zawierającą wszystkie elementy 
# mniejsze niż 5 z tej listy i wydrukuj tę nową listę. Napisz to w jednym wierszu Pythona.
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
n = []

for l in a:
    if l < 5:
        n.append(l)
        print(n)

# Poproś użytkownika o numer i zwróć listę zawierającą tylko elementy z oryginalnej listy a, 
# które są mniejsze niż liczba podana przez użytkownika.
print('================================================')
liczba = int(input('Podaj dowolną liczbę z zakresu 1 - 100: '))
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for l in a:
    if l < liczba:
        print(l, end=' ')
