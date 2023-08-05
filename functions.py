import operFile
import Notes
import UserInt as ui

number = 6  # сколько знаков МИНИМУМ может быть в тексте заметки


def add():
    note = ui.create_note(number)
    array = operFile.read_file()
    for notes in array:
        if Notes.Notes.get_id(note) == Notes.Notes.get_id(notes):
            Notes.Notes.set_id(note)
    array.append(note)
    operFile.write_file(array, 'a')
    print('Заметка добавлена')


def show(text):
    logic = True
    array = operFile.read_file()
    if text == 'date':
        date = input('Введите дату в формате dd.mm.yyyy: ')
    for notes in array:
        if text == 'all':
            logic = False
            print(Notes.Notes.map_note(notes))
        if text == 'id':
            logic = False
            print('ID: ' + Notes.Notes.get_id(notes))
        if text == 'date':
            logic = False
            if date in Notes.Notes.get_date(notes):
                print(Notes.Notes.map_note(notes))
    if logic == True:
        print('Нет ни одной заметки...')


def id_edit_del_show(text):
    id = input('Введите id необходимой заметки: ')
    array = operFile.read_file()
    logic = True
    for notes in array:
        if id == Notes.Notes.get_id(notes):
            logic = False
            if text == 'edit':
                note = ui.create_note(number)
                Notes.Notes.set_title(notes, note.get_title())
                Notes.Notes.set_body(notes, note.get_body())
                Notes.Notes.set_date(notes)
                print('Заметка изменена...')
            if text == 'del':
                array.remove(notes)
                print('Заметка удалена...')
            if text == 'show':
                print(Notes.Notes.map_note(notes))
    if logic == True:
        print('Такой заметки нет, возможно, вы ввели неверный id')
    operFile.write_file(array, 'a')