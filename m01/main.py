import spell_tools
# import pokestop_tools
from pokestop_tools import get_reward_label

result = spell_tools.get_spell_label("荷伊米", 3)
print(result)

result2 = get_reward_label("大師球", 1)
print(result2)