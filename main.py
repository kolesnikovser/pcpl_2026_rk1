"""Рубежный контроль №1 по ПиК ЯП, вариант Б-11.

Предметная область: «Программа - Компьютер».
"""

from operator import itemgetter
from pprint import pprint


class Program:
    """Программа; находится на стороне «много» связи с компьютером."""

    def __init__(self, id: int, name: str, size_mb: int, computer_id: int):
        self.id = id
        self.name = name
        self.size_mb = size_mb
        self.computer_id = computer_id


class Computer:
    """Компьютер."""

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name


class ProgramComputer:
    """Связь «многие-ко-многим» между программами и компьютерами."""

    def __init__(self, program_id: int, computer_id: int):
        self.program_id = program_id
        self.computer_id = computer_id


# Компьютеры
computers = [
    Computer(1, "Офисный ПК"),
    Computer(2, "ПК разработчика"),
    Computer(3, "Учебный ПК"),
    Computer(4, "Сервер"),
]

# Программы. size_mb - количественный признак программы.
programs = [
    Program(1, "Редактор текстов", 180, 1),
    Program(2, "Менеджер файлов", 95, 2),
    Program(3, "Просмотрщик логов", 60, 3),
    Program(4, "Калькулятор", 12, 1),
    Program(5, "Тестировщик", 240, 4),
]

# Установки программ на компьютерах для связи «многие-ко-многим».
programs_computers = [
    ProgramComputer(1, 1),
    ProgramComputer(1, 4),
    ProgramComputer(2, 2),
    ProgramComputer(2, 3),
    ProgramComputer(3, 3),
    ProgramComputer(4, 1),
    ProgramComputer(4, 2),
    ProgramComputer(5, 4),
]


def main() -> None:
    """Выполнить запросы варианта Б."""
    # Соединение данных «один-ко-многим».
    one_to_many = [
        (program.name, program.size_mb, computer.name)
        for computer in computers
        for program in programs
        if program.computer_id == computer.id
    ]

    # Соединение данных «многие-ко-многим».
    many_to_many_temp = [
        (computer.name, relation.program_id)
        for computer in computers
        for relation in programs_computers
        if computer.id == relation.computer_id
    ]
    many_to_many = [
        (program.name, program.size_mb, computer_name)
        for computer_name, program_id in many_to_many_temp
        for program in programs
        if program.id == program_id
    ]

    print("Задание Б1")
    # Все связанные программы и компьютеры, сортировка по названию программы.
    result_b1 = sorted(one_to_many, key=itemgetter(0))
    pprint(result_b1)

    print("\nЗадание Б2")
    # Все компьютеры с количеством программ; сортировка по убыванию количества.
    result_b2_unsorted = [
        (
            computer.name,
            len([row for row in one_to_many if row[2] == computer.name]),
        )
        for computer in computers
    ]
    result_b2 = sorted(result_b2_unsorted, key=itemgetter(1), reverse=True)
    pprint(result_b2)

    print("\nЗадание Б3")
    # Программы, названия которых оканчиваются на «ов», и компьютеры с ними.
    result_b3 = {
        program.name: [
            computer_name
            for program_name, _, computer_name in many_to_many
            if program_name == program.name
        ]
        for program in programs
        if program.name.casefold().endswith("ов")
    }
    pprint(result_b3)


if __name__ == "__main__":
    main()
