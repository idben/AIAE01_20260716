# Python 的互動模式

MENU = [
    {"id": "1", "title": "新增資料"},
    {"id": "2", "title": "查詢資料"},
    {"id": "3", "title": "離開"},
]

def show_menu():
    """
    目的: 印出選單
    資料來源: 全域常數 MENU
    """
    for item in MENU:
        print(f"{item["id"]}. {item["title"]}")
    
def find_item(choice) -> dict | None:
    for item in MENU:
        if item["id"] == choice:
            return item
    return None

def say(msg):
    print(f"AI 說: {msg}")

while True:
    show_menu()
    choice = input("請選擇: ")

    # print(f"你的選擇是: {choice}")
    item = find_item(choice)
    if item is None:
        say("沒有這個選項")
        continue

    say(f"你的選擇是 {item["title"]}")

    if item["title"] == "離開":
        break
