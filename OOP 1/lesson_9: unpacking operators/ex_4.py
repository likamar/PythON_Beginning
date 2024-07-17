# Utwórz dwa słowniki i połącz je w jeden wykorzystując operator **.
# Tak otrzymany słownik “rozpakuj” wywołując funkcję z zadania drugiego.
from ex_2 import print_self

dict_1 = {
    "name": "Adam",
    "age": 25,
}

dict_2 = {
    "city": "Warsaw",
    "country": "Poland",
}

merged_dicts = {**dict_1, **dict_2}
print(merged_dicts)
print(print_self(**merged_dicts))

