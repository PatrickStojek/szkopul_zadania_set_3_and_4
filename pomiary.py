""" Wstęp do programowania 2, lekcja 5. Dostępna pamięć: 256 MB. 01.01.2017
Czujnik w muzeum w ciągu dnia wykonał serię regularnych pomiarów poziomu zanieczyszczenia powietrza
w pomieszczeniu. Wiadomo, że wizyta każdego zwiedzającego powoduje wzrost zanieczyszczenia powietrza.
Dyrektor muzeum chciałby oszacować, ilu zwiedzających było tego dnia w muzeum. Napisz program, który
obliczy, ile istotnie różnych pomiarów o dodatnim poziomie zanieczyszczenia zarejestrował czujnik.
Wejście
Wejście składa się z co najmniej dwóch wierszy. Każdy wiersz zawiera jedną liczbę całkowitą. Pierwszy wiersz
zawiera liczbę 0 – wynik pierwszego pomiaru czujnika. Kolejne wiersze zawierają kolejne wyniki pomiarów,
będące nieujemnymi liczbami całkowitymi. Wyniki pomiarów są podane w porządku niemalejącym. Ostatni
wiersz zawiera liczbę −1, oznaczającą koniec wejścia.
Wejście będzie zawierać co najwyżej 100 000 liczb. Żadna liczba na wejściu nie przekroczy 1 000 000 000.
Wyjście
Jedyny wiersz wyjścia powinien zawierać liczbę różnych liczb dodatnich występujących na wejściu. Jeśli wejście
nie zawiera żadnej liczby dodatniej, poprawnym wynikiem jest 0.
Przykład
Dla danych wejściowych:
0
0
4
7
7
9
10
10
-1
poprawnym wynikiem jest:
4 """
ShouldContinue = True
positive_distinctive_meassurements = []
counter = 0
while ShouldContinue:
    number = int(input())
    if number == -1:
        ShouldContinue = False
    else:
        if number > 0:
            if positive_distinctive_meassurements.count(number) == 0:
                positive_distinctive_meassurements.append(number)
                counter += 1

print(counter)

