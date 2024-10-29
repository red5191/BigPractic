students = [
    {'name': 'Harry', 'grades': [80, 90, 78]},
    {'name': 'Hermione', 'grades': [95, 90, 97]},
    {'name': 'Ron', 'grades': [60, 70, 64]},
    {'name': 'Draco', 'grades': [60, 75, 70]}
]

correct = ['да', 'нет']


def calculate_average(grades):
    average = sum(grades) / len(grades)
    return average


def students_card_list():
    list_average = []
    for n, stud in enumerate(students):
        grades = students[n].get('grades')
        average = calculate_average(grades)
        list_average.append(average)
        print(f'''Студент: {students[n].get('name')}
Средний балл: {average}''')
        if average >= 75:
            print(f'Cтатус: Успешен \n')
        else:
            print(f'Cтатус: Отстающий \n')
    global loser
    loser = list_average.index(min(list_average))
    print(f'Общий средний балл: {calculate_average(list_average)} \n')
    return loser


def delete_loser():
    answer = input('Хотите избавиться от самого отстающего? ').lower()
    while answer not in correct:
        print('Пожалуйста используйте для ответа \"да\" или \"нет\"', '\n')
        answer = input('Хотите избавиться от самого отстающего? ').lower()
    if answer == 'да':
        students.pop(loser)
        students_card_list()


def add_student():
    answer = input('Хотите добавить нового студента? ').lower()
    while answer not in correct:
        print('Пожалуйста используйте для ответа \"да\" или \"нет\"')
        answer = input('Хотите добавить нового студента? ').lower()
    if answer == 'да':
        input_name = input('Введите имя студента ')
        while True:
            try:
                input_grades = [int(g) for g in input('Введите оценки через пробел ').split()]
                break
            except  ValueError:
                print('Пожалуйста используйте числа')
        new_stud = {'name': input_name, 'grades': input_grades}
        students.append(new_stud)
        students_card_list()


print('Проверим список студентов')

students_card_list()

while True:
    answer = input('Хотите изменить список? ')
    while answer not in correct:
        print('Пожалуйста используйте для ответа \"да\" или \"нет\"')
        answer = input('Хотите изменить список? ').lower()
    if answer == 'да':
        delete_loser()
        add_student()
    else:
        print('Список утвержден')
        break
