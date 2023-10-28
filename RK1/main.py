from collections import Counter
from collections import defaultdict

class Pupil:
    """Ученик"""
    def __init__(self, id, fio, rate, form_id):
        self.id = id
        self.fio = fio
        self.rate = rate
        self.form_id = form_id
class Form:
    """Класс"""
    def __init__(self, id, name):
        self.id = id
        self.name = name
class PupilAndForm:
    def __init__(self, pupil_id, form_id):
        self.pupil_id = pupil_id
        self.form_id = form_id
     
forms_data = [
    Form(1, '9А'),
    Form(2, '9Б'),
    Form(3, '10А'),
    Form(4, '10Б'),
    Form(5, '11А'),
    Form(6, '11Б'),

    Form(7, '(другой)9А'),
    Form(8, '(другой)9Б'),
    Form(9, '(другой)10А'),
    Form(10, '(другой)10Б'),
    Form(11, '(другой)11А'),
    Form(12, '(другой)11Б'),
]

pupils = [
    Pupil(1, 'Попова', 5, 1),
    Pupil(2, 'Соколов', 4, 1),
    Pupil(3, 'Алексеев', 4, 1),

    Pupil(4, 'Орлов', 3, 2),
    Pupil(5, 'Кузьмин', 4, 2),
    Pupil(6, 'Егорова', 5, 2),

    Pupil(7, 'Белов', 4, 3),
    Pupil(8, 'Козлова', 5, 3),
    Pupil(9, 'Жукова', 5, 3),

    Pupil(10, 'Титов', 3, 4),
    Pupil(11, 'Смирнова', 4, 4),
    Pupil(12, 'Ефимов', 4, 4),

    Pupil(13, 'Соловьев', 3, 5),
    Pupil(14, 'Осипова', 5, 5),
    Pupil(15, 'Комаров', 5, 5),

    Pupil(16, 'Крылов', 4, 6),
    Pupil(17, 'Кузнецов', 4, 6),
    Pupil(18, 'Попов', 4, 6),
]

pupil_and_form_data = [
    PupilAndForm(1, 1),
    PupilAndForm(1, 7),
    PupilAndForm(2, 1),
    PupilAndForm(2, 7),
    PupilAndForm(3, 1),
    PupilAndForm(4, 2),
    PupilAndForm(4, 8),
    PupilAndForm(5, 2),
    PupilAndForm(5, 8),
    PupilAndForm(6, 2),
    PupilAndForm(7, 3),
    PupilAndForm(7, 9),
    PupilAndForm(8, 3),
    PupilAndForm(9, 3),
    PupilAndForm(10, 4),
    PupilAndForm(11, 4),
    PupilAndForm(12, 4),
    PupilAndForm(12, 10),
    PupilAndForm(13, 5),
    PupilAndForm(14, 5),
    PupilAndForm(15, 5),
    PupilAndForm(15, 11),
    PupilAndForm(16, 6),
    PupilAndForm(17, 6),
    PupilAndForm(18, 6),
    PupilAndForm(18, 12),
]

def main():
    """Основная функция"""

    print('[ИУ5-32Б] 2.Бокатуев Максмим Сергеевич')
    print('РК-1 Вариант-2 ПиКЯП')
    #Запрос 1: список всех школьников и их классов, отсортированный по имени ученика
    print('Запрос 1:')
    sorted_pupils = sorted(pupils, key=lambda x: x.fio)
    forms_dict = {forms.id: forms.name for forms in forms_data}
    [print(f"Школьник: {pupils.fio}, Класс: {forms_dict.get(pupils.form_id, 'Неизвестный класс')}") for pupils in sorted_pupils]

    #Запрос 2: список классов и количесвта в учеников в них, отсортированный по количеству учеников
    print('\nЗапрос 2:')
    num_pupils = Counter(d.form_id for d in pupil_and_form_data)
    sorted_forms = sorted(forms_data, key=lambda x: num_pupils[x.id], reverse=True)
    [print(f"Класс: {form.name}, Количество учеников: {num_pupils[form.id]}") for form in sorted_forms]

    #Запрос 3: список школьников, фамилия которых заканчивается на "ов" и их классов
    print('\nЗапрос 3:')
    pupil_form_dict = defaultdict(list)
    for cd in pupil_and_form_data:
        pupil_form_dict[cd.pupil_id].append(cd.form_id)
    filtered_pupils = [pupil for pupil in pupils if pupil.fio.endswith("ов")]
    [print(f"Школьник: {pupils.fio}, Класс(ы): {', '.join(forms_dict[id] for id in pupil_form_dict.get(pupils.id, []))}") for pupils in filtered_pupils]

if __name__ == '__main__':
    main()