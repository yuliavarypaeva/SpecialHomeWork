import json
import datetime


def load_notes():
    try:
        with open('notes.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


notes = load_notes()


def save_notes(notes):
    with open('notes.json', 'w') as file:
        json.dump(notes, file, indent=4)


def add_note():
    title = input("Введите заголовок заметки: ")
    message = input("Введите текст заметки: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {
        'id': len(notes) + 1,
        'title': title,
        'message': message,
        'timestamp': timestamp
    }
    notes.append(note)
    save_notes(notes)
    print(f"Заметка с номером {note['id']} успешно сохранена")


def delete_note():
    note_id = int(input("Введите номер заметки для удаления: "))
    for note in notes:
        if note['id'] == note_id:
            notes.remove(note)
            save_notes(notes)
            print("Заметка успешно удалена")
            return
    print("Заметка с указанным номером не найдена")


def edit_note():
    note_id = int(input("Введите номер заметки для редактирования: "))
    for note in notes:
        if note['id'] == note_id:
            new_title = input("Введите новый заголовок заметки: ")
            new_message = input("Введите новый текст заметки: ")
            note['title'] = new_title
            note['message'] = new_message
            note['timestamp'] = datetime.datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S")
            save_notes(notes)
            print("Заметка успешно отредактирована")
            return
    print("Заметка с указанным номером не найдена")


def filter_notes_by_date():
    date_str = input("Введите дату в формате (YYYY-MM-DD): ")
    try:
        filter_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        print("Некорректный формат")
        return

    filtered_notes = [note for note in notes if datetime.datetime.strptime(
        note['timestamp'], "%Y-%m-%d %H:%M:%S").date() == filter_date]

    if filtered_notes:
        print("Заметки на указанную дату:")
        for note in filtered_notes:
            print(f"Номер: {note['id']}")
            print(f"Заголовок: {note['title']}")
            print(f"Текст: {note['message']}")
            print(f"Дата/Время последнего изменения: {note['timestamp']}")
            print()
    else:
        print("Заметки на указанную дату отсутствуют")


def print_notes():
    for note in notes:
        print(f"Номер: {note['id']}")
        print(f"Заголовок: {note['title']}")
        print(f"Текст: {note['message']}")
        print(f"Дата/Время последнего изменения: {note['timestamp']}")
        print()


while True:
    print("Доступные команды:")
    print("1 - добавить заметку")
    print("2 - удалить заметку")
    print("3 - редактировать заметку")
    print("4 - отфильтровать заметки по дате")
    print("5 - вывести список заметок")
    print("6 - выйти из программы")
    command = input("Введите номер команды: ")

    if command == "1":
        add_note()
    elif command == "2":
        delete_note()
    elif command == "3":
        edit_note()
    elif command == "4":
        filter_notes_by_date()
    elif command == "5":
        print_notes()
    elif command == "6":
        break
    else:
        print("Команды не существует")
