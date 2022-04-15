HELP = """help - напечатать справку по программе
add - добавить задачу в список
show - показать все добавленные задачи
"""
todo = {}


endOfProgramm = False

while not endOfProgramm:
  command = input("Введите команду: ")
  if command == "help":
    print(HELP)
  elif command == "show":
    print(todo)
  elif command == "add":
    day = input("Введите дату: ")
    task = input("Введите задачу: ")
    if not (day in todo):
      todo[day] = []
    todo[day].append(task)
    print("Задача", task,  "добавленна на дату: ", day)
  else:
    print("Неизвестная команда")
    break

print("До свидания")
