from hash_generator import generate_hash
from math_calc import calculate_linear

if __name__ == "__main__":
    test_string = "Python"
    hash_result = generate_hash(test_string)
    print(f"Hash gerada para '{test_string}': {hash_result}")

    x_value = 5
    calc_result = calculate_linear(x_value)
    print(f"Resultado do cálculo linar para X={x_value}: {calc_result}")