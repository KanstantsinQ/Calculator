# Calculator

Prosty kalkulator w Pythonie z systemem licznika użycia i poziomu baterii.
Każde działanie zmniejsza baterię o 0.5% i zwiększa licznik użycia.

## Funkcje

- Dodawanie (`sum`)
- Odejmowanie (`sub`)
- Mnożenie (`mul`)
- Dzielenie (`div`)
- Potęgowanie (`pow`)

## Atrybuty

- `brand` – marka kalkulatora
- `price` – cena
- `serial_number` – numer seryjny
- prywatne: licznik użycia, poziom baterii

## Użycie
```python

from calculator import Calculator

my_calc = Calculator("Casio", 150, "XDC-1A23")

print(my_calc)  # pokazuje informacje o kalkulatorze

# przykładowe działania
print(my_calc.sum(2, 3))   # 5
print(my_calc.mul(4, 6))   # 24

# sprawdzenie statystyk
odometer, battery = my_calc.get_stats
print(f"Licznik: {odometer}, Bateria: {battery}%")