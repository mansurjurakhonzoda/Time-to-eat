# # 1
# a = 0


# def add(money):
#     global a
#     a += money
#     print(f"Ваш счёт успешно пополнен! Теперь он составляет - {a}$")


# def give(money):
#     global a
#     if money <= a:
#         a -= money
#         print(f"С вашего счёта успешно снято {money}$ и ваш баланс составляет - {a}$")
#     else:
#         print("Недостаточно средств!")
#         while money > a:
#             print("Попробуйте ввести ещё раз: ")
#             money = float(input("Введите размер денег для снятия с баланса: "))
#         a -= money
#         print(f"С вашего счёта успешно снято {money}$ и ваш баланс составляет - {a}$")


# def balance():
#     print(f"Баланс: {a}$")


# while True:
#     print("""       --- Menu ---
# 1. Пополнить
# 2. Снять
# 3. Баланс
# 4. Выход""")
#     b = int(input("Введите номер операции = "))
#     match b:
#         case 1:
#             c = float(input("Введите количество, которым хотите пополнить = "))
#             add(c)
#         case 2:
#             c = float(input("Введите количество, которым хотите снять = "))
#             give(c)
#         case 3:
#             balance()
#         case 4:
#             break

# # 2
# small = (
#     "a",
#     "b",
#     "c",
#     "d",
#     "e",
#     "f",
#     "g",
#     "h",
#     "i",
#     "j",
#     "k",
#     "l",
#     "m",
#     "n",
#     "o",
#     "p",
#     "q",
#     "r",
#     "s",
#     "t",
#     "u",
#     "v",
#     "w",
#     "x",
#     "y",
#     "z",
# )
# big = (
#     "A",
#     "B",
#     "C",
#     "D",
#     "E",
#     "F",
#     "G",
#     "H",
#     "I",
#     "J",
#     "K",
#     "L",
#     "M",
#     "N",
#     "O",
#     "P",
#     "Q",
#     "R",
#     "S",
#     "T",
#     "U",
#     "V",
#     "W",
#     "X",
#     "Y",
#     "Z",
# )
# a = input()
# b = int(input())
# c = str()
# for i in a:
#     if i in small:
#         j = ((small.index(i)) + b) % 26
#         k = small[j]
#         c += k
#     elif i in big:
#         j = ((big.index(i)) + b) % 26
#         k = big[j]
#         c += k
#     else: c+=i
# print(c)

# # 3
# a = int(input())
# for i in range(1, a + 1):
#     for j in range(1, a + 1):
#         print(j * i, end=" ")
#     print()


# # 4
# def all_words(a: str):
#     cnt = a.count(" ") + 1
#     print(f"Слов: {cnt}")


# def letters(a: str):
#     cnt = 0
#     for i in a:
#         if i.isalpha():
#             cnt += 1
#     print(f"Букв: {cnt}")


# def maxlen(a: str):
#     all = tuple(a.split())
#     word = max(all, key=len)
#     print(f"Самое длинное: {word} (но {len(word)} буквы)")


# def minlen(a: str):
#     all = tuple(a.split())
#     word = min(all, key=len)
#     print(f"Самое короткое: {word}")


# def words(a: str):
#     word = tuple(a.split())
#     wored = tuple(set(word))
#     for i in wored:
#         print(f"{i}: {word.count(i)}")


# a = input()
# print("Вывод: ")
# all_words(a)
# letters(a)
# maxlen(a)
# minlen(a)
# words(a)


# # 5
# def sort_numbers(a: list):
#     b = []
#     while a:
#         c = min(a)
#         b.append(c)
#         d = a.index(c)
#         a.pop(d)
#     return b


# a = int(input())
# b = []
# for i in range(a):
#     c = int(input())
#     b.append(c)
# print(*(sort_numbers(b)))

# # 6
# import random
# import string


# def generate_password(
#     length=8, digits="True", letters="True", symbols="True", upper="True"
# ):
#     chars = ""
#     if digits == "True":
#         chars += string.digits
#     if letters == "True":
#         if upper == "True":
#             chars += string.ascii_letters
#         else:
#             chars += string.ascii_lowercase
#     if symbols == "True":
#         chars += string.punctuation
#     password = ""
#     for i in range(length):
#         password += random.choice(chars)
#     return password


# a = int(input("Length = "))
# b = input("Digits = ")
# c = input("Letters = ")
# d = input("Symbols = ")
# e = input("Upper = ")
# print(generate_password(a, b, c, d, e))

# # 7
# students = []
# while True:
#     text = input()
#     if text == "стоп":
#         break
#     else:
#         name, score = text.split()
#         score = int(score)
#         students.append((name, score))
# students = sorted(students, key=lambda x: x[1], reverse=True)
# print("Топ 3: ")
# for i in range(1, 4):
#     student = students[i - 1]
#     name, score = student
#     print(f"{i}. {name} - {score}")
# total = 0
# for i in students:
#     total += i[1]
# print(f"Средний балл класса: {total/len(students)}")


# # 8
# def plus(a, b):
#     return a + b


# def minus(a, b):
#     return a - b


# def multiply(a, b):
#     return a * b


# def division(a, b):
#     if b != 0:
#         return a / b
#     else:
#         return "Division by zero"


# history = []
# while True:
#     a = input()
#     if a != "история":
#         b, c, d = a.split()
#         b = int(b)
#         d = int(d)
#         e = ""
#         if c == "+":
#             e += str(plus(b, d))
#         elif c == "-":
#             e += str(minus(b, d))
#         elif c == "*":
#             e += str(multiply(b, d))
#         elif c == "/":
#             e += str(division(b, d))
#         a += " = "
#         a += e
#         history.append(a)
#         print(a)
#     else:
#         if history:
#             for i in range(len(history)):
#                 print(f"{i+1}. {history[i]}")
#             break
#         else:
#             print("История пуста!!! 📜")
#             break

# # 9
# import asyncio
# import random

# words = (
#     "Ты можешь больше, чем думаешь! 💪",
#     "Каждый маленький шаг приближает тебя к цели! 🚀",
#     "Не сдавайся, у тебя всё получится! 🌟",
#     "Ошибки — это часть пути к успеху! 📚",
#     "Сегодня отличный день, чтобы стать лучше! ☀️",
#     "Твои усилия обязательно дадут результат! 💎",
#     "Продолжай двигаться вперед! 🏃",
#     "Верь в себя и свои возможности! 🌈",
#     "Успех начинается с первого шага! 👣",
#     "Ты способен достигать больших целей! 🏆",
#     "Каждый день — новая возможность! 🌱",
#     "Твои мечты заслуживают того, чтобы их воплотить! ✨",
#     "Не бойся трудностей, они делают тебя сильнее! 💪",
#     "Учись, развивайся и становись лучше! 📖",
#     "Твои старания не проходят зря! ⭐",
#     "Сделай сегодня то, чем будешь гордиться завтра! 🔥",
#     "Даже медленный прогресс — это прогресс! 🐢",
#     "Ты уже сделал первый шаг — продолжай! 🚶",
#     "Большие победы начинаются с маленьких действий! 🏅",
#     "Терпение и труд приведут тебя к успеху! 🛠️",
#     "Ты способен преодолеть любые препятствия! 🏔️",
#     "Каждая попытка делает тебя опытнее! 🎯",
#     "Твоя настойчивость — твоя сила! ⚡",
#     "Не останавливайся на достигнутом! 🚀",
#     "Будущее создаётся твоими действиями сегодня! 🌍",
#     "Ты становишься лучше с каждым днем! 🌟",
#     "Продолжай учиться и открывать новое! 🔍",
#     "У тебя есть всё необходимое для успеха! 🎓",
#     "Смелость начинается с веры в себя! 🦁",
#     "Твои цели ближе, чем кажется! 🎯",
#     "Пробуй, ошибайся, учись и расти! 🌱",
#     "Каждый новый навык делает тебя сильнее! 💡",
#     "Ты способен удивить самого себя! ✨",
#     "Не сравнивай себя с другими — развивай себя! 🌿",
#     "Твои идеи могут изменить мир! 🌎",
#     "Сохраняй любопытство и стремись к знаниям! 📚",
#     "Успех любит тех, кто не сдаётся! 🏆",
#     "Сегодня ты можешь сделать что-то важное! 🔥",
#     "Твои мечты стоят твоих усилий! 🌠",
#     "Продолжай идти, даже если путь сложный! 🛤️",
#     "Ты сильнее своих сомнений! 💪",
#     "Каждая минута обучения приближает тебя к цели! ⏳",
#     "Будь терпеливым — великие вещи требуют времени! 🕰️",
#     "Твои старания создают твоё будущее! 🌅",
#     "Не бойся начинать сначала! 🔄",
#     "Ты способен создавать удивительные вещи! 🛠️",
#     "Твой потенциал огромен! 🌌",
#     "Продолжай развивать свои таланты! 🎨",
#     "Каждый день делай хотя бы один шаг вперёд! 👣",
#     "Твои мечты могут стать реальностью! 🌟",
#     "Будь смелее, чем вчера! 🦋",
#     "Сложности делают победы ценнее! 🏆",
#     "Ты можешь научиться чему угодно! 📘",
#     "Не прекращай искать новые возможности! 🔑",
#     "Твои знания — твоя сила! 🧠",
#     "Двигайся к цели с уверенностью! 🚀",
#     "Успех строится из маленьких побед! 🧱",
#     "Каждая новая попытка приближает успех! 🎯",
#     "Ты уже на пути к своей лучшей версии! 🌱",
#     "Развивайся каждый день! 📈",
#     "Твоя решимость поможет тебе победить! ⚔️",
#     "Сохраняй позитив и двигайся вперед! 😊",
#     "Ты способен на великие достижения! 🌟",
#     "Не позволяй страху остановить тебя! 🛡️",
#     "Твой труд обязательно окупится! 💰",
#     "Продолжай мечтать и действовать! 🌠",
#     "Каждый день — шанс стать лучше! ☀️",
#     "Твоя сила внутри тебя! 🔥",
#     "Ты создаёшь своё будущее сам! 🏗️",
#     "У тебя есть талант и возможности! 🎯",
#     "Доверяй своему пути! 🛤️",
#     "Твои усилия приближают победу! 🏅",
#     "Будь настойчивым и уверенным! 💎",
#     "Каждая проблема — это новый урок! 📖",
#     "Твоё развитие не имеет границ! 🌌",
#     "Не останавливайся, когда становится трудно! 💪",
#     "Ты способен сделать невозможное возможным! ✨",
#     "С каждым днём ты становишься мудрее! 🧠",
#     "Твои действия сегодня создают завтра! 🌅",
#     "Продолжай верить в свою цель! 🎯",
#     "Ты заслуживаешь успеха за свои старания! 🏆",
#     "Каждый опыт делает тебя сильнее! ⚡",
#     "Будь человеком, которым хочешь стать! 🌱",
#     "Твои мечты ждут твоих действий! 🚀",
#     "Никогда не прекращай учиться! 📚",
#     "Ты можешь добиться многого! 🌟",
#     "Каждый новый день — новый шанс! 🌞",
#     "Твой путь уникален и важен! 🛤️",
#     "Развивай свои способности и верь в себя! 💡",
#     "Ты ближе к цели, чем вчера! 🚶",
#     "Не сдавайся после первой попытки! 🔥",
#     "Твои усилия формируют твой успех! 🏗️",
#     "Будь любопытным и открывай новое! 🔎",
#     "У тебя есть сила менять свою жизнь! 🌍",
#     "Продолжай работать над собой! 💪",
#     "Маленькие шаги приводят к большим результатам! 🏆",
#     "Твой успех начинается с решения действовать! 🚀",
#     "Ты способен достигать своих целей! 🎯",
#     "Сегодня ты можешь стать лучше, чем вчера! 🌟",
#     "Вперёд к новым достижениям! 🔥",
# )


# async def timer(a):
#     for i in range(a, 0, -1):
#         print(f"Осталось: {i} сек")
#         await asyncio.sleep(1)
#     print("Время вышло!!! ⌛")


# async def motivation():
#     global words
#     while True:
#         await asyncio.sleep(2)
#         print(random.choice(words))


# async def main(a):
#     task1 = asyncio.create_task(timer(a))
#     task2 = asyncio.create_task(motivation())
#     await task1
#     task2.cancel()


# a = int(input())
# asyncio.run(main(a))

# # 10
# students = [
#     {"name": "Нилуфар", "grade": 97},
#     {"name": "Али", "grade": 89},
#     {"name": "Саша", "grade": 76},
#     {"name": "Рустам", "grade": 61},
#     {"name": "Малика", "grade": 92},
#     {"name": "Давид", "grade": 85},
#     {"name": "Анна", "grade": 80},
#     {"name": "Илья", "grade": 96},
# ]


# def add_student(**kwargs):
#     students.append(kwargs)
#     print(f"Студент {kwargs['name']} успешно добавлен!!! 😊")


# def get_top(*args):
#     count = args[0]
#     top_students = sorted(students, key=lambda x: x["grade"], reverse=True)
#     print(f"Топ {count}:")
#     for student in top_students[:count]:
#         print(f"{student['name']} — {student['grade']}")


# def filter_students(condition):
#     result = list(filter(condition, students))
#     print("Результат фильтра:")
#     for student in result:
#         print(f"{student['name']} — {student['grade']}")


# def stats():
#     grades = []
#     for i in students:
#         grades.append(i["grade"])
#     average = sum(grades) / len(grades)
#     best = max(students, key=lambda x: x["grade"])
#     bad = min(students, key=lambda x: x["grade"])
#     print(f"""Статистика:
# Средний: {average}
# Лучший: {best['name']} - {best['grade']}
# Худший: {bad['name']} - {bad['grade']}
# Всего студентов: {len(students)}""")


# while True:
#     print(f"""      === Система студентов ===
# 1. Добавить студента
# 2. Топ студентов
# 3. Фильтр (только отличники >90)
# 4. Статистика
# 5. Выход""")
#     choice = int(
#         input("Выберите номер операции, которую хотели, чтобы была выполнена  = ")
#     )
#     if choice == 1:
#         name = input("Имя студента: ")
#         grade = int(input("Оценка: "))
#         add_student(name=name, grade=grade)
#     elif choice == 2:
#         number = int(input("Сколько лучших студентов показать: "))
#         get_top(number)
#     elif choice == 3:
#         filter_students(lambda student: student["grade"] > 90)
#     elif choice == 4:
#         stats()
#     elif choice == 5:
#         print("Программа завершена. 🫡")
#         break
#     else:
#         print("Неверный выбор!!! 👿")
