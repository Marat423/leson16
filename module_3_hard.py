def calculate_structure_sum(data): # Создаем функцию
    stock = 0  # Создаем переменную для суммирования
    def sum(element): # Создаем функцибю
        nonlocal stock # даем переменой связь
        if isinstance(element, (int, float)): # Проверяем на числовой тип
            stock += element # добавляем в переменную
        elif isinstance(element, str): # Проверяем на строковый тип
            stock += len(element) # Проходим по длине строки
        elif isinstance(element, (list, tuple, set)): # иначе если это список или кортеж
            for i in element: # Проходим по каждому элементу
                sum(i)
        elif isinstance(element, dict): # Иначе если словарь
            for key, value in element.items(): # возвраещаем улюч значение
                sum(key)
                sum(value)

    sum(data)
    return stock

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)
print(result)