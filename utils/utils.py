import json
from datetime import datetime


def load_operations():
    """загружает все операции из файла"""
    with open('operations.json', encoding="utf-8") as file:
        return json.load(file)


def sorted_operations():
    """оставляет только выполненные операции и сортирует по дате выполнения по убыванию"""
    sort_operations = []
    for operation in load_operations():
        for v in operation.values():
            if v == "EXECUTED":
                sort_operations.append(operation)
    return sorted(sort_operations, key=lambda x: x['date'], reverse=True)


def formatted_operations(n):
    """форматирует дату в списке в ДД.ММ.ГГГГ,
    номер карты в XXXX XX** **** XXXX,
    номер счета в **XXXX
    и оставляет заданное количество последних операций"""
    sort_operations = sorted_operations()
    format_operations = []
    for i in range(n):
        date_i = sort_operations[i]['date'][:10]
        date_object = datetime.strptime(date_i, "%Y-%m-%d")
        sort_operations[i]['date'] = date_object.strftime('%d.%m.%Y')

        if "Счет" in sort_operations[i]['to']:
            sort_operations[i]['to'] = 'Счет **' + sort_operations[i]['to'][-4:]
        else:
            new_to = list(sort_operations[i]['to'])
            new_to.insert(-12, " ")
            new_to[-10:-4] = "** **** "
            sort_operations[i]['to'] = ''.join(new_to)

        if 'from' in sort_operations[i]:
            if "Счет" in sort_operations[i]['from']:
                sort_operations[i]['from'] = 'Счет **' + sort_operations[i]['from'][-4:]
            else:
                new_from = list(sort_operations[i]['from'])
                new_from.insert(-12, " ")
                new_from[-10:-4] = "** **** "
                sort_operations[i]['from'] = ''.join(new_from)

        format_operations.append(sort_operations[i])
    return format_operations
