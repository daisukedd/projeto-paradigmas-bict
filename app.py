animals = []

def add_animal(name, age, breed, owner_name):
    animal = {
        "name": name,
        "age": age,
        "breed": breed,
        "owner_name": owner_name,
        "consultation_history": [],
        "vaccine_history": []
    }
    animals.append(animal)
    print("Animal added successfully!")

def add_consultation(animal_name, date, description):
    for animal in animals:
        if animal["name"] == animal_name:
            animal["consultation_history"].append({"date": date, "description": description})
            print("Consultation added successfully for", animal_name)
            return
    print("Animal not found!")

def add_vaccine(animal_name, vaccine_name, date):
    for animal in animals:
        if animal["name"] == animal_name:
            animal["vaccine_history"].append({"vaccine_name": vaccine_name, "date": date})
            print("Vaccine added successfully for", animal_name)
            return
    print("Animal not found!")

def main():
    while True:
        print("\n### Veterinary Clinic Management System ###")
        print("1. Add Animal")
        print("2. Add Consultation")
        print("3. Add Vaccine")
        print("4. Exit")

        option = input("Choose an option: ")

        if option == "1":
            name = input("Animal name: ")
            age = input("Animal age: ")
            breed = input("Animal breed: ")
            owner_name = input("Owner name: ")
            add_animal(name, age, breed, owner_name)
        elif option == "2":
            animal_name = input("Animal name: ")
            date = input("Consultation date (dd/mm/yyyy): ")
            description = input("Consultation description: ")
            add_consultation(animal_name, date, description)
        elif option == "3":
            animal_name = input("Animal name: ")
            vaccine_name = input("Vaccine name: ")
            date = input("Date of application (dd/mm/yyyy): ")
            add_vaccine(animal_name, vaccine_name, date)
        elif option == "4":
            print("Exiting the program...")
            break
        else:
            print("Invalid option!")

if __name__ == "__main__":
    main()
