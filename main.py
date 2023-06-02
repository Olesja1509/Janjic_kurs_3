from utils.utils import formatted_operations


last_operations = formatted_operations(5)

for i in range(len(last_operations)):
    print(f"{last_operations[i]['date']} {last_operations[i]['description']}")

    if "from" in last_operations[i]:
        print(f"{last_operations[i]['from']} -> {last_operations[i]['to']}")
    else:
        print(f"{last_operations[i]['to']}")

    print(f"{last_operations[i]['operationAmount']['amount']} "
          f"{last_operations[i]['operationAmount']['currency']['name']}\n")
