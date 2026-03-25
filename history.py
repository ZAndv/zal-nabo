def save_history(operation, result):
    with open("history.txt", "a") as f:
        f.write(f"{operation} = {result}\n")

def show_history():
    try:
        with open("history.txt", "r") as f:
            print("\n--- Historia ---")
            print(f.read())
    except FileNotFoundError:
        print("Brak historii")
