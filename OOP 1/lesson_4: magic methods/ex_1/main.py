from shop.order import generate_random_order
from shop.apple import Apple
from shop.potato import Potato

if __name__ == '__main__':
    print("Ex_1:")
    print("\nRandom order:\n")
    random_order = generate_random_order()
    print(random_order)

    print("Ex_2:")
    apple_1 = Apple(species="Champion", size="L", price_kg=4.50)
    apple_2 = Apple(species="Lobo", size="M", price_kg=3.99)
    apple_3 = Apple(species="Jonagold", size="XL", price_kg=4.99)
    apple_4 = Apple(species="Granny Smith", size="L", price_kg=6.99)

    print(apple_1)
    print(apple_2)
    print(apple_3)
    print(apple_4)

    potato_1 = Potato(species="Agata", size="M", price_kg=1.99)
    potato_2 = Potato(species="Annabelle", size="L", price_kg=2.49)
    potato_3 = Potato(species="Cecile", size="XL", price_kg=2.99)
    potato_4 = Potato(species="Vivaldi", size="XL", price_kg=3.49)

    print()
    print(potato_1)
    print(potato_2)
    print(potato_3)
    print(potato_4)
