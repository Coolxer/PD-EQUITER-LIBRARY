# PD-EQUITER-LIBRARY

Biblioteka języka Python implementująca stacjonarne metody przybliżone rozwiązywania układów równań liniowych.
---

*Realizacja w ramach pracy dyplomowej "Analiza i realizacja wybranych algorytmów przybliżonego rozwiązywania układów równań liniowych" KRK/13/4028*

***Autor:** Łukasz Miłoś 161883*

---
 
## Zawartość 

W bibliotece można znaleźć wiele wyjaśnień teoretycznych dotyczących tematu rozwiązywania URL.

Biblioteka implementuje następujące stacjonarne metody przybliżone:
- metoda Jacobiego (iteracji prostej)
- metoda Gaussa-Seidela
- metoda SOR

Każda metoda jest odpowiednio udokomentowana, a implementacja jest ściśle oparta na zagadnieniach teoretycznych. Dla każdej metody sprawdzany jest warunek zbieżności przybliżonych metod stacjonarnych. Nie zabrakło także pełnej walidacji danych wejściowych gwarantujących poprawność obliczeń.

Korzystanie z biblioteki jest proste i intuicyjne.


***!UWAGA! :***
Warto wypróbować także środowisko laboratoryjne wykorzystujące wspomnianą bibliotekę. Wspomaga ono proces testowania metod i zawiera wstępną analizę wyników. Środowisko dostępne jest [tutaj](https://github.com/Coolxer/PD-EXPERIMENTOR).

---

## Wymagania

Oprócz samej biblioteki niezbędne jest posiadanie:
- interpreter [Python](https://www.python.org/downloads/) (zalecana wersja 3.*)
- biblioteka [NumPy](https://numpy.org/install/) (niekiedy instalowana razem z Python'em)
- dowolny edytor tekstowy (zalecany edytor kodu źródłowego, np. [Visual Studio Code](https://code.visualstudio.com/))

---

## Instalacja

Repozytorium należy pobrać przy pomocy systemu kontroli wersji [git](https://git-scm.com/) albo "ręcznie" w formacie .zip, a następnie wypakować.

***UWAGA:*** Biblioteka powinna być podkatalogiem bieżącego projektu, a więc skrypty wykorzystujące bibliotekę powinny być wyżej w hierarchi katalogów. Innymi słowy nie należy umieszczać własnych skryptów wewnątrz katalogu biblioteki !

***UWAGA:*** Po ściągnięciu biblioteki zalecana jest zmiana nazwy głównego katalogu na ***equiter*** Jest to skrótowa nazwa ułatwiająca korzystanie z biblioteki. Jeśli chcesz podążać dalej za poradnikiem zmiana nazwy jest niezbędna !

Po przygotowaniu biblioteki, we własnym pliku Python (z rozszerzeniem *.py) można przystąpić do importu biblioteki.

```python
import equiter as eq
```

---

## Szybkie Uruchomienie

### Gotowy przykład

W celu zapoznania się z biblioteką zalecane jest uruchomienie dowolnego przykładu, np.


```python
import equiter as eq

eq.jacobi_example_1()
```

Efektem wykonania powyższego kodu będzie wyświetlenie następujących informacji w konsoli / terminalu:

```console
##### Metoda iteracyjna stacjonarna - Jacobi - Przyklad 1 #####
Rozwiazanie: [ 0.76666667  2.03333333 -1.32916667]
Liczba wykonanych iteracji: 3
Czas obliczen: 0.0s
```

### Własny Przykład

Poniżej prezentowany jest sposób w jaki najprawdopodobniej będziesz korzystać z biblioteki.

```python
import equiter as eq
import numpy as np

# Parametry wejściowe:
A = np.array([[3, 1, -1], [-1, 5, -1], [2, 4, 8]])
b = np.array([6, 10, 2])
max_iterations = 3
tolerance = 0.0001

print("##### Wlasny przyklad #####")

x, i, t = eq.jacobi(A, b, max_iterations, tolerance)

print(f"Rozwiazanie: {x}")
print(f"Liczba wykonanych iteracji: {i}")
print(f"Czas obliczen: {t}s")
```

---

## Jak używać?

Z perspektywy użytkownika najważnejsze jest to w jaki sposób wywoływać poszczególne metody, jakie argumenty są wymagane orraz jakie wartości są zwracane. Pozostałe kwestie nie mają większego znaczenia dla zwykłych użytkowników, zwłaszcza, że biblioteka posiada stosowną walidację i informuje użytkownika o zaistniałych problemach.

### Metody
Dostępne są następujące interfejsy metod:
- metoda Jacobiego:

```python
def jacobi(
    A: np.array,
    b: np.array,
    max_iterations: int,
    tolerance: float,
    x0: np.array = None,
)
```

- metoda Gaussa-Seidela:

```python
def gauss_seidel(
    A: np.array,
    b: np.array,
    max_iterations: int,
    tolerance: float,
    x0: np.array = None,
):
```

- metoda SOR:
```python
def sor(
    A: np.array,
    b: np.array,
    max_iterations: int,
    tolerance: float,
    w: float,
    x0: np.array = None,
)
```

### Argumenty
Poniżej prezentowane są opisy poszczególnych argumentów:
- A (macierz) - kwadratowa dwuwymiarowa macierz układu równań
    - ***Wymagania***
      - nie może być pusta
      - powinna być dwuwymiarowa
      - musi być kwadratowa

- b (wektor)- wektor wartości po prawej stronie równiania Ax = b
	- ***Wymagania***
      - musi być wektorem
      - nie może być pusty
      - musi mieć rozmiar adekwatny do macierzy A
  
- max_iterations (liczba całkowita) - maksymalna liczba iteracji, która determinuje koniec operacji
	- ***Wymagania***
      - Liczba całkowita dodatnia

- tolerance (liczba zmiennoprzecinkowa, podwójnej precyzji) - zadana dokładność (tolerancja), która determinuje koniec operacji
	- ***Wymagania***
      - Liczba zmiennoprzecinkowa większa od 0

- w (liczba zmiennoprzecinkowa) - parametr relaksacji (0, 2)
	- ***Wymagania***
      - Liczba z zakresu (0, 2)

- x0 (wektor) [opcjonalne] - Początkowe przybliżenie niewiadomych układu
	- ***Wymagania***
      - musi być wektorem (1 wymiar)
      - nie może być pusty
      - musi mieć rozmiar adekwatny do macierzy A

  ***UWAGA!*** Jeśli argument x0 nie został podany, to jako pierwsze przybliżenie x0 przyjmuje się wektor złożony z samych 0

### Wartości zwracane przez poszczególne metody

Każda metoda zwraca 3 wartości:
- ***x*** - przybliżenie rozwiązania w postaci wektora
- ***i*** - liczba wykonanych iteracji
- ***t*** - czas obliczeń w sekundach [s]

```python
x, i, t = method(...)
```
