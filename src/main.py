from simple_chemistry_element import ChemistryElementLookup


if __name__ == "__main__":
    lookup = ChemistryElementLookup()
    try:
        symbol = input("Enter an element symbol: ").strip()
        element = lookup.get_element_by(symbol)
        print(f"{element['name']}: Atomic Number: {element['atomic_number']}")
    except KeyError as e:
        print(e)
