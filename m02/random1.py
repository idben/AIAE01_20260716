import random

# 測試隨機模組

def choose_monster_drop(drops: list[str]) -> str:
    return random.choice(drops)

def random_damage(basic_damage: int, bonus_int: int):
    bonus_damage = random.randint(1, bonus_int)
    return basic_damage + bonus_damage

available_drops = ["藥草", "金幣", "短劍"]
print(choose_monster_drop(available_drops))
print(f"短劍攻擊，造成傷害 {random_damage(30, 6)}")
print(f"短劍攻擊，造成傷害 {random_damage(30, 6)}")
print(f"短劍攻擊，造成傷害 {random_damage(30, 6)}")
print(f"短劍攻擊，造成傷害 {random_damage(30, 6)}")

daily_tasks = [
    "伏地挺身 50 個",
    "仰臥起坐 100 個",
    "長跑 10 公里",
    "擊殺怪物 10 隻",
    "和朋友對練 2 小時",
]

new_tasks = daily_tasks.copy()
random.shuffle(new_tasks)
print(f"你已經收到每日任務 {new_tasks[:3]}")

new_tasks = daily_tasks.copy()
random.shuffle(new_tasks)
print(f"你已經收到每日任務 {new_tasks[:3]}")


new_tasks = daily_tasks.copy()
random.shuffle(new_tasks)
print(f"你已經收到每日任務 {new_tasks[:3]}")


new_tasks = daily_tasks.copy()
random.shuffle(new_tasks)
print(f"你已經收到每日任務 {new_tasks[:3]}")