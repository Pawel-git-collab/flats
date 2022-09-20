from csv import writer


def save_to_CSV(content, file_name="housing.csv"):
    with open(file_name, "a", encoding='utf8', newline='') as f:
        header = ['Tytul ogloszenia', 'Lokalizacja', 'Cena', 'Wynajem/Sprzedaz', 'Link', 'Cena do negocjacji']
        writer(f).writerow(header)
        for element in content:
            writer(f).writerow(element)


