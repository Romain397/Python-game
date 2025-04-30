class Member:
    def __init__(self, first_name, last_name, gender, age):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__gender = gender
        self.__age = age

    def introduce_yourself(self):
        return f"Je m'appelle {self.__first_name} {self.__last_name}, je suis une(e) {self.__gender} de {self.__age} ans."

    def get_first_name(self):
        return self.__first_name

    def set_first_name(self, value):
        self.__first_name = value

    def get_last_name(self):
        return self.__last_name

    def set_last_name(self, value):
        self.__last_name = value

    def get_gender(self):
        return self.__gender

    def set_gender(self, value):
        self.__gender = value

    def get_age(self):
        return self.__age

    def set_age(self, value):
        self.__age = value


class Operator(Member):
    def __init__(self, first_name, last_name, gender, age, role, experience=0):
        super().__init__(first_name, last_name, gender, age)
        self.__role = role
        self.__experience = experience

    def increase_experience(self, points):
        self.__experience += points

    def gain_experience(self):
        self.__experience += 1
        print(
            f"{self.get_first_name()} {self.get_last_name()} gagne en expérience. Niveau actuel : {self.__experience}."
        )

    def get_role(self):
        return self.__role

    def set_role(self, value):
        self.__role = value

    @property
    def _experience(self):
        return self.__experience

    @_experience.setter
    def _experience(self, value):
        if value < 0:
            raise ValueError("Expérience ne peut pas être négative")
        self.__experience = value

    def act(self):
        if self.__role == "technicien":
            print(
                f"{self.get_first_name()} {self.get_last_name()} nettoie le vaisseau."
            )
        elif self.__role == "pilote":
            print(f"{self.get_first_name()} {self.get_last_name()} pilote le vaisseau.")
        else:
            print(
                f"{self.get_first_name()} {self.get_last_name()} effectue une action en tant que {self.__role}."
            )


class Mentalist(Member):
    def __init__(self, first_name, last_name, gender, age, mana=0):
        super().__init__(first_name, last_name, gender, age)
        self.__mana = mana

    def get_role(self):
        return "mentaliste"

    def get_experience(self):
        return self.__experience

    def increase_experience(self, points):
        self.__experience += points

    def act(self, operator):
        if self.__mana >= 20:
            self.__mana -= 20
            print(
                f"{self.__first_name} {self.__last_name} influence {operator.__first_name} {operator.__last_name}"
            )
            operator.act()
        else:
            print(
                f"{self.__first_name} {self.__last_name} n'a pas assez de mana pour agir."
            )

    def recharge_mana(self):
        if self.__mana + 50 > 100:
            self.__mana = 100
        else:
            self.__mana += 50
        print(
            f"{self.__first_name} {self.__last_name} a rechargé son mana. Mana actuel : {self.__mana}."
        )

    @property
    def _mana(self):
        return self.__mana
