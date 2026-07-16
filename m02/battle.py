from characters import PartyMember

SPELL_MP_COSTS: dict[str, int] = {
    "荷依米": 3,
    "基拉": 4,
}

def cast_spell(caster: PartyMember, target: PartyMember, damage: int) -> str:
    target.take_damage(damage)
    return f"{caster.name} 施放咒文，{target.name} 剩下 {target.hp} HP"


def main():
    ch01 = PartyMember("小美", 100)
    ch02 = PartyMember("骨頭怪", 20)
    print(cast_spell(ch01, ch02, SPELL_MP_COSTS["荷依米"]))


if __name__ == "__main__":
    main()