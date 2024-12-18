# module_3_6

salarii = [11000, 11170, 22000, 33400, 41050, 6000]
print(salarii)
print(len(salarii))
print(sum(salarii) / len(salarii), 'СРЕДНЯЯ ЗАРПЛАТА')
print(max(salarii), 'МАКСИМАЛЬНАЯ ЗАРПЛАТА')
print(min(salarii), 'МИНИМАЛЬНАЯ ЗАРПЛАТА')

names = ['Денис', 'Антон', 'Анна', 'Иван', 'Светлана', 'Вероника']
zipped = dict(zip(names, salarii))

# Вводим имя через input()
name = input("Введите имя сотрудника: ")
if name in zipped:
    print(zipped[name], f'Зарплата {name}')
else:
    print(f"Сотрудник с именем '{name}' не найден.")











