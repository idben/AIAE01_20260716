from characters import PartMamber
from battle import cast_spell

h1 = PartMamber("小明", 100)
h2 = PartMamber("小華", 100)
# h1.take_damage(h2, 10)
cast_spell(h1, h2, 10)