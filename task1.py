#1
day = input("Введите дату: ")
task = input("Введите задачу: ")

print(day, ": ", task)

#2
todo = {}
i = 0
while i < 3:
  day = input("Введите дату: ")
  task = input("Введите задачу: ")
  todo[day] = task
  i = i + 1

for key,value in todo.items():
	print(key, ':', value)

#3
todo = {}
i = 0
while i < 3:
  day = input("Введите дату: ")
  task = input("Введите задачу: ")
  todo[day] = task
  i = i + 1
