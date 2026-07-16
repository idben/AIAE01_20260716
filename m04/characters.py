# from battle import cast_spell
# 造成循環匯入的主因

class PartMamber:
    def __init__(self, name: str, hp: int) -> None:
        self.name = name
        self.hp = hp
    def take_damage(self, damage: int):
        self.hp -= damage