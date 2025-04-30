from crew import *

MAX_CREW_SIZE = 10


class Spaceship:

    def __init__(self, name, ship_type, crew=[], condition="opérationnel"):
        self.__name = name
        self.__ship_type = ship_type
        self.__crew = crew
        self.__condition = condition

    @property
    def _name(self):
        return self.__name

    @_name.setter
    def _name(self, value):
        self.__name = value

    @property
    def _ship_type(self):
        return self.__ship_type

    @_ship_type.setter
    def _ship_type(self, value):
        self.__ship_type = value

    @property
    def _crew(self):
        return self.__crew

    @_crew.setter
    def _crew(self, value):
        self.__crew = value

    @property
    def _condition(self):
        return self.__condition

    @_condition.setter
    def _condition(self, value):
        self.__condition = value

    def add_member(self, member):
        if len(self.__crew) < MAX_CREW_SIZE:
            if isinstance(member, Member):
                self.__crew.append(member)
                print(
                    f"{member.get_first_name()} {member.get_last_name()} a été ajouté à l'équipage du vaisseau {self.__name}."
                )
            else:
                print("Le membre n'est pas valide")
        else:
            print(
                f"Le vaisseau {self.__name} a atteint sa capacité maximale de 10 membres d'équipage."
            )

    def remove_member(self, member):
        if member in self.__crew:
            self.__crew.remove(member)
            print(
                f"{member.get_first_name()} {member.get_last_name()} a été retiré de l'équipage du vaisseau {self.__name}."
            )
        else:
            print(
                f"{member.get_first_name()} {member.get_last_name()} n'est pas dans l'équipage."
            )

    def introduce_ship(self):
        return f"Le vaisseau {self.__name} de type {self.__ship_type} est actuellement {self.__condition}."

    def check_preparation(self):
        has_pilot = any(member.get_role() == "pilote" for member in self.__crew)
        has_technician = any(
            member.get_role() == "technicien" for member in self.__crew
        )

        return has_pilot and has_technician

    def is_ready(self):
        if self.check_preparation():
            return f"Le vaisseau {self.__name} de type {self.__ship_type} est opérationnel."
        else:
            return f"Le vaisseau {self.__name} n'est pas prêt, il manque un pilote ou un technicien."
