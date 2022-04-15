print(2 ** 3) #возведение в стпень
s1 = "12"
s2 = "+"
s3 = "5"

print(s1 + s2 + s3)

l = len(s1)
print("len = ", l)

#список хранит все, даже не уникальные элемнты
# индексы с 0
strings = ["Руддщ", ", привет"]
data = ["fff", 7]

print(strings)
print(data)

summa = strings + data
print(data) 

data.append(9)

print(data)
numbers = [7, 1, 4] 
s = sum(numbers)
print(s)
numbers.sort()
print(numbers)
#словари
#ключ: значение

dict = {
  "cat": "кошка",
  "dog":"собака"
}

print(dict)

print(dict["cat"])

contries = {
  "Африка": ["Египет", "Конго"],
  "Aзия": ["Китай", "Тайланд"]
}

print(contries["Африка"])

contries ["Европа"] = ["Россия", "Италия"]

print(contries)

africa = contries["Африка"]
print(africa)

africa.append("ЮАР")
print(africa)
print(contries["Африка"])
contries["Африка"].append("Эфиопия")
print(africa)
print(contries["Африка"])

#ввод данных
name = input("Введите имя: ")
print("Привет, ", name)

print(17/2) #обычное деление - результат 8.5
print(17//2) #целочисленное деление - результат 8, целая часть при делении
print(17%2) #деление с остатком - результат 1, остаток при делении

str1 = "5"
print(str1*5)

#мы считываем данные с помощью функции input( ), мы считываем именно строковый тип. 
#a = int(input())
#b = float(input()) 

