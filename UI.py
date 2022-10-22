import model
def start():
    strt = input('Выберете функцию:\n 1.Внести новую запись \
        \n 2.Редактировать запись\n 3.Загрузить справочник\n 4.Поиск\n 5.Удалить запись \n')
    while not strt.isdigit():
        strt = input('Ошибка ввода, повторите команду')
    strt = int(strt)
    if strt == 1:
        model.enter()
    elif strt == 2:
        id = input('Введите id ')
        data = input('Введите фамилию ')
        model.edit(id, data)
    elif strt == 3:
        model.upload()
    elif strt == 4:
        data = input('Что ищем? \n')
        model.find(data)
    elif strt == 5:
        model.delete
    else:
        print('Команды не уществует')

start()