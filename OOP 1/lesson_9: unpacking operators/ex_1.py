# Napisz funkcję która przyjmie dowolną liczbę argumentów pozycyjnych
# i zwróci napis powstały z połączenia ich z wykorzystaniem myślnika
# jako łącznika pomiędzy poszczególnymi argumentami.

def merge_strings(*args):
    return "-".join(args)


result = merge_strings("apple", "banana", "kiwi")
print(result)
