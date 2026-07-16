class PartyMember:
    def __init__(self, name: str, hp: int) -> None:
        self.name = name
        self.hp = hp

    def take_damage(self, damage: int) -> None:
        self.hp -= damage
