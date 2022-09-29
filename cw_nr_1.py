'''
Utwórz program, który prosi użytkownika o podanie swojego imienia i wieku. 
Wydrukuj wiadomość zaadresowaną do nich, która mówi im rok, w którym skończą 100 lat
'''
import datetime

imie = input('Podaj swoje imię: ')
wiek = int(input('Podaj swój wiek: '))

today = datetime.date.today()
t = today.year 

rok = int(t) + (100 - wiek)
print(f'{imie} w {rok} ukończysz 100 lat')