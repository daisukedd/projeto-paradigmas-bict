import json
from tabulate import tabulate

# Defining the filename for storing data
data_file = "animals.json"

# Function to load data from JSON file
def load_data():
    try:
        with open(data_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Function to save data to JSON file
def save_data():
    with open(data_file, "w") as file:
        json.dump(animals, file, indent=4)

# Function to add a new animal to the list of animals
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

# Function to add a consultation to the consultation history of an animal
def add_consultation(animal_name, date, description):
    for animal in animals:
        if animal["name"] == animal_name:
            animal["consultation_history"].append({"date": date, "description": description})
            save_data()
            print("Consultation added successfully for", animal_name)
            return
    print("Animal not found!")

# Function to add a vaccine to the vaccine history of an animal
def add_vaccine(animal_name, vaccine_name, date):
    for animal in animals:
        if animal["name"] == animal_name:
            animal["vaccine_history"].append({"vaccine_name": vaccine_name, "date": date})
            save_data()
            print("Vaccine added successfully for", animal_name)
            return
    print("Animal not found!")

# Function to display all animals
def display_all_animals():
    if not animals:
        print("No animals found.")
    else:
        headers = ["Index", "Name"]
        animals_table = [[index + 1, animal["name"]] for index, animal in enumerate(animals)]
        print(tabulate(animals_table, headers=headers, tablefmt="grid"))

# Function to display detailed information of a specific animal
def display_animal_details(animal_index):
    animal = animals[animal_index]
    headers = ["Attribute", "Value"]
    animal_data = [
        ["Animal", animal["name"]],
        ["Age", animal["age"]],
        ["Breed", animal["breed"]],
        ["Owner Name", animal["owner_name"]]
    ]
    consultation_history = [[consultation["date"], consultation["description"]] for consultation in animal["consultation_history"]]
    vaccine_history = [[vaccine["vaccine_name"], vaccine["date"]] for vaccine in animal["vaccine_history"]]
    print("\nAnimal Details:")
    print(tabulate(animal_data, headers=headers, tablefmt="grid"))
    print("\nConsultation History:")
    if consultation_history:
        print(tabulate(consultation_history, headers=["Date", "Description"], tablefmt="grid"))
    else:
        print("No consultation history available.")
    print("\nVaccine History:")
    if vaccine_history:
        print(tabulate(vaccine_history, headers=["Vaccine Name", "Date"], tablefmt="grid"))
    else:
        print("No vaccine history available.")

# Main function
def main():
    global animals
    animals = load_data()

    while True:
        print("\n### Veterinary Clinic Management System ###")
        menu_options = [
            ["1", "Add Animal"],
            ["2", "Add Consultation"],
            ["3", "Add Vaccine"],
            ["4", "Show All Animals"],
            ["5", "Exit"]
        ]
        print(tabulate(menu_options, headers=["Option", "Description"], tablefmt="grid"))

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

# Starting the program
if __name__ == "__main__":
    main()
