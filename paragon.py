def Add(storage, name, price):
    storage.append((name, price)) 

def Save_as_File(storage, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        total_price = sum(product_price for _, product_price in storage)
        file.write("Paragon:\n")
        file.write("")
        for product_name, product_price in storage:
            file.write(f"{product_name}: {product_price} zł\n")
        file.write(f"SUMA: {total_price} zł\n")

def Print_receipt(storage):
    print("Paragon:")
    for product_name, product_price in storage:
        print(f"{product_name}: {product_price} zł")


def main():
    list = []
    while True:
        try:
            name = input("Podaj nazwe produktu (wpisz '1' aby zakończyć): ")
            if name.lower() == '1':
                break
            price = float(input("Podaj cenę produktu: "))
            Add(list, name, price)
        except ValueError:
            print("Błędna cena. Podaj liczbę.")

    file_name = input("Podaj nazwę pliku do zapisu paragonu: ")
    Save_as_File(list, file_name)

if __name__ == "__main__":
    main()
