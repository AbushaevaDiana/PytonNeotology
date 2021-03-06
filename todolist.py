import random
HELP = """help - напечатать справку по программе
add - добавить задачу в список
show - показать все добавленные задачи
random - добавление случайной задачи на сегодня
"""
todo = {}
endOfProgramm = False
randomTasks = ["Записаться на курс Неотологии", "Потренироваться в коде", "Вышивать", "Приготовить десерт"]

def addTask(todo, day, task):
  if not (day in todo):
    todo[day] = []
  todo[day].append(task)
  print("Задача", task,  "добавленна на дату: ", day)
  return todo


while not endOfProgramm:
  command = input("Введите команду: ")
  if command == "help":
    print(HELP)
  elif command == "random":
    task = random.choice(randomTasks)
    todo = addTask(todo, "Today", task)
  elif command == "show":
    day = input("Введите дату для отображения списка задач: ")
    if day in todo:
      for task in todo[day]:
        print("- ", task)
    else:
      print("На эту дату нет задач")
  elif command == "add":
    day = input("Введите дату: ")
    task = input("Введите задачу: ")
    todo = addTask(todo, day, task)
  else:
    print("Неизвестная команда")
    break

print("До свидания")
