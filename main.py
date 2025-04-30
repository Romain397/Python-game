import json
import ast
import random
from crew import *
from spaceship import *
from fleet import *


def load_data(file_name):
    try:
        with open(file_name, "r") as file:
            data = json.load(file)

        fleet_name = data["_Fleet__name"]
        fleet = Fleet(fleet_name)

        for ship_data in data["_Fleet__spaceships"]:
            ship_name = ship_data["_Spaceship__name"]
            ship_type = ship_data["_Spaceship__ship_type"]
            ship_condition = ship_data["_Spaceship__condition"]
            ship = Spaceship(ship_name, ship_type, condition=ship_condition)

            for member_data in ship_data["_Spaceship__crew"]:
                first_name = member_data["_Member__first_name"]
                last_name = member_data["_Member__last_name"]
                gender = member_data["_Member__gender"]
                age = member_data["_Member__age"]

                if "_Operator__role" in member_data:
                    role = member_data["_Operator__role"]
                    experience = member_data["_Operator__experience"]
                    member = Operator(
                        first_name, last_name, gender, age, role, experience
                    )
                elif "_Mentalist__mana" in member_data:
                    mana = member_data["_Mentalist__mana"]
                    member = Mentalist(first_name, last_name, gender, age, mana)

                ship.add_member(member)

            fleet.append_spaceship(ship)

        return fleet

    except Exception as e:
        print(f"Erreur lors du chargement des données : {e}")
        return None


def save_data(fleet, file_name):
    try:
        json_string = json.dumps(
            fleet, default=lambda o: o.__dict__, sort_keys=True, indent=4
        )

        json_dict = ast.literal_eval(json_string)

        with open(file_name, "w") as file:
            json.dump(json_dict, file, indent=4)
        print(f"Données sauvegardées dans le fichier {file_name}")
    except Exception as e:
        print(f"Erreur lors de la sauvegarde : {e}")


def get_valid_age():
    while True:
        try:
            age = int(input("Entrez l'âge du membre : "))
            return age
        except ValueError:
            print("Erreur : L'âge doit être un nombre entier 🚩")


def random_event(fleet):
    events = ["attaque ennemie", "renforts"]
    event = random.choice(events)

    if event == "attaque_ennemie":
        if fleet._spaceships:
            damaged_ship = random.choice(fleet._spaceships)
            damaged_ship._condition -= 10
            print(
                f"Attaque ennemie ! Le vaisseau {damaged_ship._name} a été endommagé. 🛸"
            )
        else:
            print("Aucun vaisseau disponible pour être attaqué. 🚩")
    elif event == "renforts":
        if fleet._spaceships:
            new_member = Operator(
                "Renforts",
                "Member",
                "Unknown",
                random.randint(20, 50),
                "Technician",
                random.randint(1, 10),
            )
            assigned_ship = random.choice(fleet._spaceships)
            assigned_ship.add_member(new_member)
            print(
                f"Renforts ! {new_member.get_first_name()} {new_member.get_last_name()} a été ajouté au vaisseau {assigned_ship._name}. 🚀"
            )
        else:
            print("Aucun vaisseau disponible pour recevoir des renforts. 🚩")


def display_statistics(fleet):
    total_ships = len(fleet._spaceships)
    roles_count = {"pilote": 0, "technicien": 0, "mentaliste": 0}
    operational_ships = 0
    damaged_ships = 0

    for ship in fleet._spaceships:
        condition = ship._condition.lower()
        if condition == "opérationnel":
            operational_ships += 1
        else:
            damaged_ships += 1

        for member in ship._crew:
            if isinstance(member, Operator):
                role = member.get_role().lower()
                if role == "pilote":
                    roles_count["pilote"] += 1
                elif role == "technicien":
                    roles_count["technicien"] += 1
            elif isinstance(member, Mentalist):
                roles_count["mentaliste"] += 1

    print(f"\n=== Statistiques de la flotte : {fleet._name} ===")
    print(f"Nombre total de vaisseaux : {total_ships}")
    print(f"Nombre de membres par rôle :")
    for role, count in roles_count.items():
        print(f"  {role.capitalize()} : {count}")
    print(f"Nombre de vaisseaux opérationnels : {operational_ships}")
    print(f"Nombre de vaisseaux endommagés : {damaged_ships}")


def menu():
    fleet_name = input("Entrez le nom de votre flotte : ")
    fleet = Fleet(fleet_name)

    while True:
        print(f"\n=== Gestion de la flotte : {fleet._name} ===")
        print("1. Renommer la flotte 🔍")
        print("2. Ajouter un Vaisseau à la flotte 🛸")
        print("3. Ajouter un membre d'équipage 🚀")
        print("4. Supprimer un membre d'équipage ❌")
        print("5. Afficher les informations d'un équipage 🗒️")
        print("6. Vérifier la préparation d'un vaisseau 🛠️")
        print("7. Afficher les statistiques de la flotte 📈")
        print("8. Afficher les statistiques 📈")
        print("9. Sauvegarder ✅")
        print("10. Charger une flotte 🧷")
        print("11. Quitter 🚩")

        choice = input("Choisissez une option : ")

        if choice == "1":
            new_name = input("Entrez le nouveau nom de la flotte : ")
            fleet.name = new_name
            print(f"La flotte a été renommé en : {fleet._name} ✅")
        elif choice == "2":
            ship_name = input("Entrez le nom du vaisseau : ")
            ship_type = input("Entrez le type du vaisseau (ex: guerre, transport) : ")
            new_ship = Spaceship(ship_name, ship_type)
            fleet.append_spaceship(new_ship)
            print(
                f"Le vaisseau {new_ship._name} de type {new_ship._ship_type} a été ajouté à la flotte."
            )
        elif choice == "3":
            first_name = input("Entrez le prénom du membre : ")
            last_name = input("Entrez le nom du membre : ")
            gender = input("Entrez le genre du membre : ")

            age = get_valid_age()

            role = input(
                "Entrez le rôle du membre (pilote, technicien, mentaliste, etc.) : "
            )

            if role.lower() == "mentaliste":
                new_member = Mentalist(first_name, last_name, gender, age)
            else:
                new_member = Operator(first_name, last_name, gender, age, role)

            spaceship_name = input(
                "Entrez le nom du vaisseau auquel ajouter ce membre : "
            )

            found_ship = next(
                (ship for ship in fleet._spaceships if ship_name == spaceship_name),
                None,
            )
            if found_ship:
                found_ship.add_member(new_member)
                print(
                    f"{first_name} {last_name} a été ajouté à l'équipage du vaisseau {found_ship._name}."
                )
            else:
                print("Vaisseau introuvable.")

        elif choice == "4":
            first_name = input("Entrez le prénom du membre à supprimer : ")
            last_name = input("Entrez le nom du membre à supprimer : ")

            member_to_remove = next(
                (
                    member
                    for member in fleet.get_all_members()
                    if member.get_first_name() == first_name
                    and member.get_last_name() == last_name
                ),
                None,
            )
            if member_to_remove:
                spaceship_name = input("Entrez le nom du vaisseau du membre : ")
                found_ship = next(
                    (
                        ship
                        for ship in fleet._spaceships
                        if ship._name == spaceship_name
                    ),
                    None,
                )
                if found_ship:
                    found_ship.remove_member(member_to_remove)
                else:
                    print("Vaisseau introuvable. 🚩")
            else:
                print("Membre introuvable. 🚩")

        elif choice == "5":
            spaceship_name = input(
                "Entrez le nom du vaisseau pour afficher les informations de l'équipage : "
            )
            found_ship = next(
                (ship for ship in fleet._spaceships if ship._name == spaceship_name),
                None,
            )

            if found_ship:
                print(f"Équipage du vaisseau {found_ship._name} :")
                for member in found_ship._crew:
                    print(f"- {member.get_first_name()} {member.get_last_name()})")
                    if isinstance(member, Mentalist):
                        print(f"  Mana: {member._mana}")
                    elif isinstance(member, Operator):
                        print(f"  Expérience: {member._experience}")

            else:
                print("Vaisseau introuvable. 🚩")

        elif choice == "6":
            spaceship_name = input("Entrez le nom du vaisseau à vérifier : ")
            found_ship = next(
                (ship for ship in fleet._spaceships if ship._name == spaceship_name),
                None,
            )
            if found_ship:
                if found_ship.check_preparation():
                    print(f"Le vaisseau {found_ship._name} est prêt.")
                else:
                    print(f"Le vaisseau {found_ship._name} n'est pas prêt. 🚩")
            else:
                print("Vaisseau introuvable. 🚩")

        elif choice == "7":
            fleet.statistics()

        elif choice == "8":
            display_statistics(fleet)

        elif choice == "9":
            file_name = input("Entrez le nom du fichier json : ")
            save_data(fleet, file_name)

        elif choice == "10":
            file_name = input("Entrez le nom du fichier json : ")
            loaded_fleet = load_data(file_name)
            if loaded_fleet:
                fleet = loaded_fleet
                print(f"Flotte {fleet._name} chargée avec succès.")

        elif choice == "11":
            print("Quitter le programme. 🏁")
            break

        else:
            print("Choix invalide, veuillez essayer de nouveau. 🚩")

        random_event(fleet)


menu()
