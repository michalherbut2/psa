# Współtworzenie

## Przygotowanie środowiska

```
uv sync
```

Polecenie pobiera interpreter CPython 3.12, instaluje zależności z grup runtime i deweloperskiej oraz pakiet `binpack` w trybie edytowalnym.
Jeśli pliki `uv` nie są w `PATH`, `Makefile` pozwala wskazać narzędzie zmienną `UV`.

## Język

Kod, nazwy i komentarze piszemy po angielsku.
Komunikaty commitów piszemy po angielsku.
Dokumentacja publiczna, czyli `README.md` i ten dokument, jest po polsku.
Plik `AGENTS.md` jest po angielsku, ponieważ adresujemy go do narzędzi.

## Sprawdzenia

Każde sprawdzenie ma jeden punkt wejścia w `Makefile`.

```
make fmt
make lint
make test
```

Zmiana trafia do przeglądu dopiero wtedy, gdy `make lint` i `make test` kończą się powodzeniem.
`make fmt` uruchamiamy przed lintowaniem, ponieważ lint sprawdza również formatowanie.

## Testy

Testy jednostkowe w `tests/unit` odwzorowują strukturę `src/binpack` tam, gdzie moduł ma własne testy; testy obejmujące kilka modułów leżą w katalogu głównym tego poziomu.
Nowe zachowanie wymaga testu jednostkowego; test opisuje kontrakt punktu wejścia, a nie jego implementację.
Testy integracyjne w `tests/integration` uruchamiamy tylko wtedy, gdy sprawdzenie wymaga działającego kontenera.
Noszą one marker `docker` i są pomijane, gdy demon kontenerów nie odpowiada; brak demona nie jest błędem.

## Commity

Format komunikatu:

```
type(zakres): opis
```

`type` opisuje rodzaj zmiany:

| Typ | Znaczenie |
|---|---|
| `feat` | nowa funkcjonalność |
| `fix` | poprawka błędu |
| `refactor` | zmiana bez zmiany zachowania |
| `test` | dodanie lub poprawka testów |
| `docs` | dokumentacja |
| `chore` | konfiguracja, narzędzia i pliki pomocnicze |
| `spec` | zmiana specyfikacji |
| `plan` | zmiana planu |

`zakres` wskazuje moduł projektu:

| Zakres | Obszar |
|---|---|
| `ENV` | środowisko, repozytorium i konfiguracja |
| `UTL` | wspólne narzędzia: losowość, pomiar czasu, walidacja i serializacja |
| `MOD` | model domenowy, rozwiązanie, funkcja celu i metryki |
| `ALG` | algorytmy alokacji |
| `EXP` | generowanie instancji oraz uruchamianie i raportowanie eksperymentów |

Przykłady: `feat(ALG): add tournament selection` i `docs(ENV): describe the commit convention`.

Opis mówi, co robi zmiana, i mieści się w 72 znakach pierwszej linii.

## Przebieg pracy

1. Zaimplementuj zmianę wraz z testami.
2. Uruchom `make fmt`, `make lint` i `make test`.
3. Zapisz zmianę w jednym commicie w przyjętej konwencji.
4. Poproś o przegląd; recenzent ocenia kontrakt i zielone sprawdzenia.

## Dokumentacja dla agentów

Zasady dla narzędzi automatycznych znajdują się w [AGENTS.md](AGENTS.md).
