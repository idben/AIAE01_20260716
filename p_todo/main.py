from todo_item.todolist import Todolist

# 建立待辦事項列表
list01 = Todolist("去日本必買")
# 由待辦事項列表建立待辦事項
list01.add("眼藥水")
list01.add("任天堂點數卡")
list01.add("鹽崑布")
# 顯示目前待辦事項
print(list01)
# 由待辦事項列表存檔
# 由待辦事項列表讀檔