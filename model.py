BASE = "base.csv"

def enter():
    id = input('Введите ID\n')
    while not id.isdigit():
        print('Ошибка ввода')
        id = input('Введите ID\n')
    name = input('Введите ФИО ')
    while name.isdigit():
        print('Ошибка ввода')
        name = input('Введите имя\n')
    phone = input('Введите номер телефона ')
    while not phone.isdigit():
        print('Ошибка ввода')
        phone = input('Введите номер телефона ')
    while len(phone) > 11:
        print('Слишком длинный номер')
        phone = input('Введите номер телефона ')
    while len(phone) < 11:
        print('слишком короткий номер')
        phone = input('Введите номер телефона ')
    status = input('Введите статус сотрудника ')
    while status.isdigit():
        print('Ошибка ввода')
        status = input('Введите статус сотрудника ')
    with open(BASE, "a") as file:
        file.writelines(f'id:{id} ;Name:{name} ;Phone:{phone} ;Status {status}\n')
    

def edit(id, data):
    res = []
    with open(BASE, "r") as file:
        base = file.read().split('\n') 
        for item in base:
            line = item.split(';')
            if line[0] == id:
                line = data
                res.append(line)
            else:
                res.append(line)
    with open(BASE, "w") as file:
        for data in res:
            file.writelines(f'{data}\n')
    return "Success"

def upload(upload):
    with open(BASE, "a") as file:
        for data in upload:
            file.writelines(f'{data[0]};{data[1]};{data[2]};{data[3]};{data[4]};{data[5]};{data[6]};{data[7]}\n')
    return "Запись сохранена"

def find(data):
    res = []
    with open(BASE, "r") as file:
        base = file.read().split('\n') 
        for item in base:
            line = item.split(';')
            lists = list(filter(None, data))
            if set(lists).issubset(line) and len(line) > 1:
                res.append(line)
    return res

def delete(data):
    res = []
    with open(BASE, "r") as file:
        base = file.read().split('\n') 
        for item in base:
            line = item.split(';')
            lists = list(filter(None, data))
            if not set(lists).issubset(line) and len(line) > 1:
                res.append(line)