import json

data_file = "animals.json"

def load_data():
    try:
        with open(data_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data():
    with open(data_file, "w") as file:
        json.dump(animals, file, indent=4)

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
    save_data()
    print("Animal added successfully!")

def add_consultation(animal_name, date, description):
    for animal in animals:
        if animal["name"] == animal_name:
            animal["consultation_history"].append({"date": date, "description": description})
            save_data()
            print("Consultation added successfully for", animal_name)
            return
    print("Animal not found!")

def add_vaccine(animal_name, vaccine_name, date):
    for animal in animals:
        if animal["name"] == animal_name:
            animal["vaccine_history"].append({"vaccine_name": vaccine_name, "date": date})
            save_data()
            print("Vaccine added successfully for", animal_name)
            return
    print("Animal not found!")

def display_all_animals():
    if not animals:
        print("No animals found.")
    else:
        print("\nList of Animals:")
        for index, animal in enumerate(animals, start=1):
            print(f"{index}. {animal['name']}")

def display_animal_details(animal_index):
    animal = animals[animal_index]
    print(f"\nAnimal: {animal['name']}")
    print(f"Age: {animal['age']}")
    print(f"Breed: {animal['breed']}")
    print(f"Owner Name: {animal['owner_name']}")
    print("\nConsultation History:")
    for consultation in animal["consultation_history"]:
        print(f"- Date: {consultation['date']}, Description: {consultation['description']}")
    print("\nVaccine History:")
    for vaccine in animal["vaccine_history"]:
        print(f"- Vaccine: {vaccine['vaccine_name']}, Date: {vaccine['date']}")

def main():
    global animals
    animals = load_data()

    while True:
        print("\n### Veterinary Clinic Management System ###")
        print("1. Add Animal")
        print("2. Add Consultation")
        print("3. Add Vaccine")
        print("4. Show All Animals")
        print("5. Exit")

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
            display_all_animals()
            animal_index = int(input("Enter the number of the animal to view details (0 to cancel): ")) - 1
            if 0 <= animal_index < len(animals):
                display_animal_details(animal_index)
        elif option == "5":
            print("Exiting the program...")
            break
        else:
            print("Invalid option!")


if __name__ == "__main__":
    main()
