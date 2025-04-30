from spaceship import *
from crew import *


class Fleet:
    def __init__(self, name, spaceships=[]):
        self.__name = name
        self.__spaceships = spaceships

    @property
    def _name(self):
        return self.__name

    @_name.setter
    def _name(self, value):
        self.__name = value

    @property
    def _spaceships(self):
        return self.__spaceships

    @_spaceships.setter
    def _spaceships(self, value):
        self.__spaceships = value

    def append_spaceship(self, spaceship):
        if len(self.__spaceships) < 15:
            self.__spaceships.append(spaceship)
            print(
                f"Le vaisseau {spaceship._name} a été ajouté à la flotte {self.__name}."
            )
        else:
            print("Capacité max de 15 vaisseaux atteinte.")

    def statistics(self):
        total_members = 0
        role_count = {"pilote": 0, "technicien": 0, "mentalist": 0, "operator": 0}
        total_experience = 0
        total_operators = 0
        total_mentalist = 0

        total_ships = len(self.__spaceships)
        ship_names = [spaceship._name for spaceship in self.__spaceships]

        for spaceship in self.__spaceships:
            for member in spaceship._crew:
                total_members += 1
                if isinstance(member, Operator):
                    total_operators += 1
                    role_count["operator"] += 1
                    total_experience += member._experience
                elif isinstance(member, Mentalist):
                    total_mentalist += 1
                    role_count["mentalist"] += 1

        if total_operators > 0:
            average_experience = total_experience / total_operators
        else:
            average_experience = 0

        print(f"Statistiques de la flotte {self.__name}:")
        print(f"Nombre total de vaisseaux : {total_ships}")
        print(f"Liste de vaisseaux : {', '.join(ship_names)}")
        print(f"Nombre total de membres : {total_members}")
        print(f"Répartition des rôles : {role_count}")
        print(f"Niveau moyen d'expérience des opérateurs : {average_experience:.2f}")
        print(f"Nombre total de Mentalist : {total_mentalist}")

    def check_ready(self):
        for spaceship in self.__spaceships:
            if spaceship.check_preparation():
                print(f"Le vaisseau {spaceship._name} est prêt à partir.")
            else:
                print(
                    f"Le vaisseau {spaceship._name} n'est pas prêt, il manque un pilote ou un technicien."
                )

    def get_all_members(self):
        members = []
        for spaceship in self.__spaceships:
            members.extend(spaceship.crew)
        return members
