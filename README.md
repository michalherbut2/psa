# binpack

Oprogramowanie do eksperymentalnego porównania algorytmów rozmieszczania kontenerów w klastrze obliczeniowym o ograniczonych zasobach CPU i RAM.

## Problem

Klaster składa się z węzłów, a każdy węzeł oferuje ograniczoną liczbę rdzeni CPU oraz ograniczoną pamięć RAM.
Do rozmieszczenia zgłaszany jest zbiór kontenerów; każdy kontener wymaga określonej ilości CPU i RAM oraz ma priorytet na skali od 1 do 5.
Łączne zapotrzebowanie przewyższa pojemność klastra, więc solver wybiera kontenery do uruchomienia i wskazuje dla nich węzły.

Rozwiązanie musi spełniać warunki:

- kontener trafia najwyżej na jeden węzeł,
- uruchomiony kontener otrzymuje pełne zapotrzebowanie CPU i RAM,
- suma zapotrzebowania kontenerów przypisanych do węzła nie przekracza jego pojemności CPU ani RAM,
- kontenery, dla których brakuje zasobów, pozostają nieuruchomione.

### Funkcja celu

Jakość rozwiązania opisuje jedna suma ważona: człon liczby uruchomionych kontenerów z wagą `B` oraz suma priorytetów kontenerów uruchomionych.
Waga `B = 5|K| + 1`, gdzie `K` to zbiór zgłoszonych kontenerów, więc jeden dodatkowy uruchomiony kontener przewyższa każdą różnicę priorytetów.
Priorytety rozstrzygają wyłącznie pomiędzy rozwiązaniami o tej samej liczbie uruchomionych kontenerów.
Koszt rozwiązania to liczba kontenerów, których nie udało się uruchomić.

### Wskaźniki jakości

- liczba uruchomionych kontenerów,
- suma priorytetów uruchomionych kontenerów,
- odsetek obsłużonych kontenerów,
- wykorzystanie CPU i RAM klastra,
- czas wykonania,
- stabilność wyników mierzona odchyleniem standardowym liczby uruchomionych kontenerów i wartości funkcji celu.

### Algorytmy

- First Fit Decreasing (FFD) — zachłanny punkt odniesienia,
- algorytm genetyczny (GA) — populacja, selekcja, krzyżowanie i mutacja,
- symulowane wyżarzanie (SA) — iteracyjne modyfikacje z akceptacją gorszych rozwiązań,
- optymalizacja kolonią mrówek (ACO) — konstrukcja rozwiązań na podstawie śladów feromonowych.

## Wymagania

- `uv`,
- `make`,
- katalog z plikami `uv` (domyślnie `~/.local/bin`) w `PATH`,
- Docker z działającym demonem, opcjonalnie — wyłącznie dla testów integracyjnych.

Interpreter CPython 3.12 pobiera `uv`; systemowy Python nie jest potrzebny.
Instalację `uv` opisuje [dokumentacja uv](https://docs.astral.sh/uv/getting-started/installation/).

## Instalacja

```
uv sync
```

Polecenie pobiera interpreter, instaluje zależności runtime i grupę deweloperską oraz instaluje pakiet `binpack` w trybie edytowalnym.

## Sprawdzenia

```
make fmt
make lint
make test
```

`make fmt` formatuje kod i jest idempotentny.
`make lint` uruchamia analizę statyczną i sprawdza formatowanie.
`make test` uruchamia testy jednostkowe oraz integracyjne; test wymagający demona kontenerów jest pomijany, gdy demon nie odpowiada.

## Dokumentacja

- [CONTRIBUTING.md](CONTRIBUTING.md) — przygotowanie środowiska, sprawdzenia i konwencja commitów,
- [AGENTS.md](AGENTS.md) — te same zasady dla agentów automatycznych.
