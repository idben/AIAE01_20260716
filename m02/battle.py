from characters import PartyMember

def cast_spell(caster: PartyMember, target: PartyMember, damage: int) -> str:
    target.take_damage(damage)
    return f"{caster.name} 施放咒文，{target.name} 剩下 {target.hp} HP"