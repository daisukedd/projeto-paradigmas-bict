from functions import load_data, add_animal, add_consultation, add_vaccine, display_all_animals, display_animal_details
from terminaltables import AsciiTable

def main():
    animals = load_data()

    while True:
        print("\n### Veterinary Clinic Management System ###")
        menu_options = [
            ['1', 'Add Animal'],
            ['2', 'Add Consultation'],
            ['3', 'Add Vaccine'],
            ['4', 'Show All Animals'],
            ['5', 'Exit']
        ]
        menu_table = AsciiTable(menu_options, 'Menu Options')
        print(menu_table.table)

        option = input("Choose an option: ")

        if option == "1":
            name = input("Animal name: ")
            age = input("Animal age: ")
            breed = input("Animal breed: ")
            owner_name = input("Owner name: ")
            add_animal(animals, name, age, breed, owner_name)
        elif option == "2":
            animal_name = input("Animal name: ")
            date = input("Consultation date (dd/mm/yyyy): ")
            description = input("Consultation description: ")
            add_consultation(animals, animal_name, date, description)
        elif option == "3":
            animal_name = input("Animal name: ")
            vaccine_name = input("Vaccine name: ")
            date = input("Date of application (dd/mm/yyyy): ")
            add_vaccine(animals, animal_name, vaccine_name, date)
        elif option == "4":
            display_all_animals(animals)
        elif option == "5":
            print("Exiting the program...")
            break
        else:
            print("Invalid option!")

if __name__ == "__main__":
    main()
