from todo import Todo

class Todolist:
    def __init__(self, title: str) -> None:
        self.title = title
        self.todos: list[Todo] = []
    # 建立待辦事項
    def add(self, title: str) -> None:
        self.todos.append(Todo(title))
    # 刪除待辦事項 (真的刪除)
    # 顯示所有的待辦事項
    #   [ ] 買雞蛋
    #   [v] 買雞蛋
    # 打叉的方法
    # 去掉打叉的方法
    # 存檔
    # 讀檔

def main():
    pass

if __name__ == "__main__":
    main()