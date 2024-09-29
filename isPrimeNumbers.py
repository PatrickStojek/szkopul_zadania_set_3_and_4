""" Liczbą pierwszą nazywamy liczbę naturalną, która ma dokładnie dwa dzielniki: jedynkę i nią samą. Liczby
naturalne większe od 1, które nie są liczbami pierwszymi, nazywamy liczbami złożonymi.
W tym zadaniu Twój program powinien stwierdzić, czy wczytana na wejściu liczba naturalna jest pierwsza,
czy złożona.
Wejście
W jedynym wierszu wejścia znajduje się jedna liczba całkowita n (2 ≤ n ≤ 1 000 000).
Wyjście
Twój program powinien wypisać jedno słowo pierwsza lub zlozona, określające liczbę n.
Przykład
Dla danych wejściowych:
11
poprawnym wynikiem jest:
pierwsza
a dla danych wejściowych:
12
poprawnym wynikiem jest:
zlozona """
number = int(input())
IsPrime = True

for i in range(2, number):
    if number % i == 0:
        IsPrime = False
        break
    i = i + 1

if IsPrime:
    print('pierwsza')
else:
    print('zlozona')