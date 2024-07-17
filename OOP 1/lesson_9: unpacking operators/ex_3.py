# Wygeneruj dwie listy zawierające losowe liczby całkowite
# i połącz je w jedną wykorzystując operator *.

import random


def generate_random_list_of_integers():
    integers_list = []
    for _ in range(random.randint(1, 11)):
        integers_list.append(random.randint(1, 100))
    return integers_list


if __name__ == '__main__':
    list_1 = generate_random_list_of_integers()
    list_2 = generate_random_list_of_integers()

    print("List 1:", list_1)
    print("List 2:", list_2)
    # merged_lists = list_1 + list_2
    merged_lists = [*list_1, *list_2]
    print("Mergde lists:", merged_lists)
