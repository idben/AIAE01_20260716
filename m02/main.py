from characters import PartyMember
from battle import cast_spell
from battle import SPELL_MP_COSTS

# 主要的檔案
# 建立角色﹑安排戰鬥

hero = PartyMember("勇者", 120)
slim = PartyMember("史萊姆", 10)
print(cast_spell(hero, slim, SPELL_MP_COSTS["基拉"]))