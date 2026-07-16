from characters import PartMamber

def cast_spell(main_char: PartMamber, target_char: PartMamber, damage: int):
    # target_char.hp -= damage
    print(f"{main_char.name} 攻擊了 {target_char.name}")