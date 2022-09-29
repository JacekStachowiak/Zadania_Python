'''
Poproś użytkownika o numer. W zależności od tego, czy liczba jest parzysta, 
czy nieparzysta, wydrukuj odpowiednią wiadomość do użytkownika
'''

l = int(input('Podaj liczbę: '))

if l % 2 == 0 and l % 4 == 0:
    print(f'Twoja liczba {l} jest liczbą parzystą')
    print(f'Twoja liczba {l} jest krotnością 4') 
elif l % 2 == 0:
    print(f'Twoja liczba {l} jest liczbą parzystą')
elif l % 4 == 0:
    print(f'Twoja liczba {l} jest krotnością 4')       
else:    
    print(f'Twoja liczba {l} jest liczbą nieparzystą')    
