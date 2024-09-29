""" W pewnym kraju rząd postanowił uprościć nominały. Wszystkie dotychczasowe zastąpić dwoma nominałami: 2 oraz 3.
Ale czy da się uzyskać wszystkie możliwe kwoty przy pomocy nowych nominałów? Mają to pokazać testy, za które odpowiada
Ministerstwo Informatyki...
Wejście
Wejście składa się z jednej liczby całkowitej 𝑘 (1 ≤ 𝑘 ≤ 1018) oznaczającej kwotę, którą chcemy uzyskać.
Wyjście
Twój program powinien wypisać w jednej linii:
* Tekst:
NO MONEY
jeśli nie da się uzyskać podanej kwoty przy pomocy nominałów 2 oraz 3.
* Jeśli można uzyskać kwotę 𝑘 za pomocą nominałów 2 oraz 3 to Twój program powinien wypisać liczby:
p2 p3
Przy czym p2 to liczba wymaganych nominałów 2, zaś p3 to liczba wymaganych nominałów 3 do uzyskania kwoty 𝑘.
Jeśli istnieje wiele sposobów uzyskania kwoty 𝑘, Twój program powinien wypisać to rozwiązanie które wymaga najmniej
banknotów.
Przykład
Wejście dla testu nom0a:
1
Wyjście dla testu nom0a:
NO MONEY
Wyjaśnienie:
Kwoty 1 nie możemy uzyskać za pomocą nominałów dwa oraz trzy.
Wejście dla testu nom0b:
2
Wyjście dla testu nom0b:
1 0
Wyjaśnienie:
Kwotę 2 możemy uzyskać przy pomocy 1 nominału dwa i 0 nominałów trzy.
Wejście dla testu nom0c:
12
Wyjście dla testu nom0c:
0 4
Wyjaśnienie:
Kwotę 12 możemy uzyskać przy pomocy 0 nominałów dwa i 4 nominałów trzy.
Wejście dla testu nom0d:
23
Wyjście dla testu nom0d:
1 7
Wyjaśnienie:
Kwotę 23 możemy uzyskać na wiele sposobów. Najmniej banknotów zużyjemy przy pomocy 1 nominału dwa i 7 nominałów
trzy. """
money = int(input())

if money == 0 or money == 1:
    print('NO MONEY')

if(money % 3 == 0):
    p2 = 0
    p3 = money // 3
    print(p2, p3)
elif(money % 3 == 1):
    p2 = 2
    p3 = (money - 4) // 3
    print(p2, p3)
else:
    p2 = 1
    p3 = (money - 2) // 3
    print(p2, p3)

print('verification:', p2 * 2 + p3 * 3)