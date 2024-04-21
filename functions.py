import json
from terminaltables import AsciiTable

data_file = "animals.json"

def load_data():
    try:
        with open(data_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data(animals):
    with open(data_file, "w") as file:
        json.dump(animals, file, indent=4)

def add_animal(animals, name, age, breed, owner_name):
    animal = {
        "name": name,
        "age": age,
        "breed": breed,
        "owner_name": owner_name,
        "consultation_history": [],
        "vaccine_history": []
    }
    animals.append(animal)
    save_data(animals)
    print("Animal added successfully!")

def add_consultation(animals, animal_name, date, description):
    for animal in animals:
        if animal['name'] == animal_name:
            animal['consultation_history'].append({"date": date, "description": description})
            save_data(animals)
            print(f"Consultation added successfully for {animal_name}")
            return
    print("Animal not found!")

def add_vaccine(animals, animal_name, vaccine_name, date):
    for animal in animals:
        if animal['name'] == animal_name:
            animal['vaccine_history'].append({"vaccine_name": vaccine_name, "date": date})
            save_data(animals)
            print(f"Vaccine added successfully for {animal_name}")
            return
    print("Animal not found!")

def display_all_animals(animals):
    if not animals:
        print("No animals found.")
    else:
        table_data = [['Index', 'Name']] + [[index + 1, animal["name"]] for index, animal in enumerate(animals)]
        table = AsciiTable(table_data)
        print(table.table)

def display_animal_details(animal):
    animal_data = [
        ['Animal', animal['name']],
        ['Age', animal['age']],
        ['Breed', animal['breed']],
        ['Owner Name', animal['owner_name']],
        ['Consultation History', len(animal['consultation_history'])],
        ['Vaccine History', len(animal['vaccine_history'])]
    ]
    table = AsciiTable(animal_data, 'Animal Details')
    print(table.table)
