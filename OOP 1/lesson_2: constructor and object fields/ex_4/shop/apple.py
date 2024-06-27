class Apple:
    def __init__(self, species, size, price_kg):
        self.species = species
        self.size = size
        self.price_kg = price_kg


apple_1 = Apple(species="Champion", size="L", price_kg=4.50,)
apple_2 = Apple(species="Lobo", size="M", price_kg=3.99)
apple_3 = Apple(species="Jonagold", size="XL", price_kg=4.99)
apple_4 = Apple(species="Granny Smith", size="L", price_kg=6.99)

print(f"apple_1: species: {apple_1.species}, size: {apple_1.size}, price/kg: {apple_1.price_kg}")
print(f"apple_2: species: {apple_2.species}, size: {apple_2.size}, price/kg: {apple_2.price_kg}")
print(f"apple_3: species: {apple_3.species}, size: {apple_3.size}, price/kg: {apple_3.price_kg}")
print(f"apple_4: species: {apple_4.species}, size: {apple_4.size}, price/kg: {apple_4.price_kg}")
