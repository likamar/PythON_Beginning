class Potato:
    def __init__(self, species, size, price_kg):
        self.species = species
        self.size = size
        self.price_kg = price_kg

    def total_price(self, amount_kg):
        return self.price_kg * amount_kg

    def __repr__(self):
        return f"{self.species} | {self.size} | {self.price_kg:.2f}/kg"


if __name__ == '__main__':
    potato_1 = Potato(species="Agata", size="M", price_kg=1.99)
    potato_2 = Potato(species="Annabelle", size="L", price_kg=2.49)
    potato_3 = Potato(species="Cecile", size="XL", price_kg=2.99)
    potato_4 = Potato(species="Vivaldi", size="XL", price_kg=3.49)

    print(f"potato_1: species: {potato_1.species}, size: {potato_1.size}, price/kg: {potato_1.price_kg}")
    print(f"potato_2: species: {potato_2.species}, size: {potato_2.size}, price/kg: {potato_2.price_kg}")
    print(f"potato_1: species: {potato_3.species}, size: {potato_3.size}, price/kg: {potato_3.price_kg}")
    print(f"potato_1: species: {potato_4.species}, size: {potato_4.size}, price/kg: {potato_4.price_kg}")

    print(f"Price for 5 kg of Agata: {potato_1.total_price(5):.2f}")