HELP = """help - напечатать справку по программе
add - добавить задачу в список
show - показать все добавленные задачи
"""
todo = {}
command = input("Введите команду: ")

if command == "help":
  print(HELP)
elif command == "show":
  print(todo)
elif command == "add":
  day = input("Введите дату: ")
  task = input("Введите задачу: ")
  todo[day] = task
  print("Задача добавленна")
else:
  print("Неизвестная команда")
