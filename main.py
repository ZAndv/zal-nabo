from operations import multiply, divide, add, subtract, power, square_root
from history import save_history, show_history

from utils import get_number


def menu():
    print("\n--- Kalkulator CLI ---")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")
    print("5. Potęga")
    print("6. Pierwiastek")
    print("7. Historia")
    print("0. Wyjście")

def main():
    while True:
        menu()
        choice = input("Wybierz opcję: ")

        if choice == "0":
            break
        elif choice in ("1", "2", "3", "4", "5"):
            a = get_number("Podaj pierwszą liczbę: ")
            b = get_number("Podaj drugą liczbę: ")

            if choice == "1":
                result = add(a, b)
                operation = f"{a}+{b}"
            elif choice == "2":
                result = subtract(a, b)
                operation = f"{a}-{b}"
            elif choice == "3":
                result = multiply(a, b)
                operation = f"{a}*{b}"
            elif choice == "4":
                result = divide(a, b)
                operation = f"{a}/{b}"
            else:
                result = power(a, b)
                operation = f"{a}^{b}"
        elif choice == "6":
            a = get_number("Podaj pierwszą liczbę: ")
            result = square_root(a)
            operation = f"sqrt({a})"
        elif choice == "7":
            show_history()
            continue
        else:
            print("Nieprawidłowa opcja")
            continue

        print("Wynik:", result)
        save_history(operation, result)


if __name__ == "__main__":
    main()