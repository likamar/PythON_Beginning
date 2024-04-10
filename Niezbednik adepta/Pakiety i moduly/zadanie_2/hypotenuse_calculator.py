from math import sqrt, pow

print("Welcome to hypotenuse calculator!")
print("Enter the length of: ")
length_a = float(input("a: "))
length_b = float(input("b: "))


def calculate_c_len(a_len, b_len):
    return sqrt(pow(a_len, 2) + pow(b_len, 2))


length_c = calculate_c_len(length_a, length_b)

print(f"The length of c is equal to {length_c}")
