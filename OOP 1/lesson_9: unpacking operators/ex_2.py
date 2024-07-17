# Napisz funkcję, która przyjmie dowolną liczbę argumentów nazwanych
# i wypisze sposób w jaki została wywołana, tzn. poszczególne nazwy argumentów,
# znak równa się i wartość (np. first_name=Mikołaj, age=134).

def print_self(**kwargs):
    arguments = "Arguments: "
    for key, value in kwargs.items():
        arguments += f"{key}: {value}, "
    # remove last comma and space:
    result = arguments[:-2]
    return result


example = print_self(
    name="Marcin",
    age=18,
    city="San Francisco",
)

print(example)
