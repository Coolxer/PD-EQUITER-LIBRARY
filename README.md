# PD-EQUITER-LIBRARY

## Biblioteka języka Python implementująca stacjonarne metody przybliżone rozwiązywania układów równań liniowych.

_Realizacja w ramach pracy dyplomowej "Analiza i realizacja wybranych algorytmów przybliżonego rozwiązywania układów równań liniowych" KRK/13/4028_

**\*Autor:** Łukasz Miłoś 161883\*

---

## Zawartość

Biblioteka implementuje następujące stacjonarne metody przybliżone:

- metoda Jacobiego
- metoda Gaussa-Seidela
- metoda SOR

Każda metoda jest odpowiednio udokomentowana, a implementacja jest ściśle oparta na zagadnieniach teoretycznych. Dla każdej metody sprawdzany jest warunek zbieżności przybliżonych metod stacjonarnych. Nie zabrakło także pełnej walidacji danych wejściowych, gwarantującej poprawność obliczeń.

Korzystanie z biblioteki jest proste i intuicyjne.

Dodatkowo dla każdej z metod przygotowano po 3 przykłady testowe.

**_!UWAGA! :_**
Warto wypróbować także środowisko laboratoryjne wykorzystujące tę bibliotekę. Wspomaga ono proces testowania metod i zawiera wstępną analizę wyników. Środowisko dostępne jest [tutaj](https://github.com/Coolxer/PD-EXPERIMENTOR).

---

## Wymagania

Oprócz samej biblioteki niezbędne jest posiadanie następujących komponentów:

- interpreter [Python](https://www.python.org/downloads/) (zalecana wersja 3.\*)
- biblioteka [NumPy](https://numpy.org/install/) (niekiedy instalowana razem z Python'em)
- dowolny edytor tekstowy (zalecany jednak edytor kodu źródłowego, np. [Visual Studio Code](https://code.visualstudio.com/))

---

## Instalacja

Repozytorium należy pobrać przy pomocy systemu kontroli wersji [git](https://git-scm.com/) albo "ręcznie" w formacie .zip, a następnie wypakować w dowolnym miejscu.

**_UWAGA:_** Biblioteka powinna być podkatalogiem bieżącego projektu, a więc skrypty wykorzystujące bibliotekę powinny być wyżej w hierarchi katalogów. Innymi słowy nie należy umieszczać własnych skryptów wewnątrz katalogu biblioteki!

**_UWAGA:_** Po ściągnięciu biblioteki zalecana jest zmiana nazwy głównego katalogu na **_equiter_** Jest to skrótowa nazwa ułatwiająca korzystanie z biblioteki. Jeśli chcesz podążać dalej za poradnikiem zmiana nazwy jest niezbędna!

Po przygotowaniu biblioteki, we własnym pliku Python (z rozszerzeniem \*.py) o dowolnej nazwie, można przystąpić do importu biblioteki.

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
import numpy as np
import equiter as eq

# Parametry wejściowe
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

Z perspektywy użytkownika najważniejsze jest to w jaki sposób wywoływać poszczególne metody, jakie argumenty są wymagane oraz jakie wartości są zwracane. Pozostałe kwestie nie mają większego znaczenia dla zwykłych użytkowników, zwłaszcza, że biblioteka posiada stosowną walidację i informuje użytkownika o zaistniałych problemach.

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

### Parametry metod

Poniżej prezentowane są opisy poszczególnych argumentów:

- **_A (macierz => np.array)_** - macierz główna układu równań

  - **_Wymagania_**
    - nie może być pusta
    - musi być dwuwymiarowa
    - musi być kwadratowa

- **_b (wektor => np.array)_** - wektor wyrazów wolnych

  - **_Wymagania_**
    - nie może być pusty
    - musi być jednowymiarowy
    - musi mieć rozmiar adekwatny do rozmiaru macierzy A

- **_max_iterations (liczba całkowita => int)_** - maksymalna liczba iteracji, która determinuje koniec, , gdy nie osiągnięto założonej dokładności obliczeń

  - **_Wymagania_**
    - liczba całkowita dodatnia

- **_tolerance (liczba zmiennoprzecinkowa => float)_** - zadana dokładność (tolerancja), która determinuje koniec obliczeń

  - **_Wymagania_**
    - liczba zmiennoprzecinkowa większa od 0

- **_x0 (wektor => np.array) [opcjonalne]_** - początkowy wektor przybliżeń rozwiązania

  - **_Wymagania_**
    - nie może być pusty
    - musi być jednowymiarowy
    - musi mieć rozmiar adekwatny do rozmiaru macierzy A

  **_UWAGA!_** Jeśli argument x0 nie został podany, to jako pierwsze przybliżenie x0 przyjmuje się wektor złożony z samych 0

- **_w (liczba zmiennoprzecinkowa => float)_** - parametr relaksacji (0, 2) dla metody SOR

  - **_Wymagania_**
    - liczba z zakresu (0, 2)

### Wartości zwracane przez poszczególne metody

Każda metoda zwraca 3 wartości:

- **_x_** (np.array) - przybliżenie rozwiązania w postaci wektora
- **_i_** (int) - liczba wykonanych iteracji
- **_t_** (float) - czas obliczeń w sekundach [s]

```python
x, i, t = method(...)
```

---

### Dostępne przykłady

Przykłady dostępne są bezpośrednio z poziomu modułu jako metody, które można wywołać np.

```python
import equiter as eq
eq.sor_example_1()
```

Poniżej znajduje się tabela wszystkich dostępnych przykładów.

|   m. Jacobiego   |   m. Gaussa-Seidela    |    m. SOR     |
| :--------------: | :--------------------: | :-----------: |
| jacobi_example_1 | gauss_seidel_example_1 | sor_example_1 |
| jacobi_example_2 | gauss_seidel_example_2 | sor_example_2 |
| jacobi_example_3 | gauss_seidel_example_3 | sor_example_3 |

## Dodatkowe informacje

Biblioteka dostarcza podstawowych informacji dotyczących rozwiązania układu. Mając na celu lekkość pakietu, nie dostarczono tutaj wstępnej analizy danych, umożliwiającej porównanie poszczególnych metod, a także przedstawienie wyników w postaci graficznej.

Dobra informacja jest taka, że przygotowano specjalne środowisko badawcze wykorzystujące tę bibliotekę i opracowujące dane wynikowe w postaci tekstowej i graficznej. Środowisko badawcze dostępne jest [tutaj](https://github.com/Coolxer/PD-EXPERIMENTOR).
