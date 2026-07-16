class Todo:
    # title: 待辦事項的文字
    # isFinished: 是否完成待辦事項
    # createAt: 建立日期
    # isDel: 軟刪除用的屬性
    def __init__(self, title: str) -> None:
        self.title = title
        self.isFinished = False
        self.isDel = False
    def __str__(self) -> str:
        mark = " "
        if self.isFinished:
            mark = "v"
        return f"[{mark}] {self.title}"

def main():
    todo01 = Todo("買雞胸肉")
    todo01.isFinished = True
    print(todo01)

if __name__ == "__main__":
    main()