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
     
def query_1(forms_data, pupils):
    sorted_pupils = sorted(pupils, key=lambda x: x.fio)
    forms_dict = {forms.id: forms.name for forms in forms_data}
    result = []
    for pupils in sorted_pupils:
        result.append(f"Школьник: {pupils.fio}, Класс: {forms_dict.get(pupils.form_id, 'Неизвестный класс')}")
    return result

def query_2(forms_data, pupil_and_form_data):
    num_pupils = Counter(d.form_id for d in pupil_and_form_data)
    sorted_forms = sorted(forms_data, key=lambda x: num_pupils[x.id], reverse=True)
    result = []
    for form in sorted_forms:
        result.append(f"Класс: {form.name}, Количество учеников: {num_pupils[form.id]}")
    return result

def query_3(forms_data, pupils, pupil_and_form_data):
    pupil_form_dict = defaultdict(list)
    forms_dict = {forms.id: forms.name for forms in forms_data}
    result = []
    for cd in pupil_and_form_data:
        pupil_form_dict[cd.pupil_id].append(cd.form_id)
    filtered_pupils = [pupil for pupil in pupils if pupil.fio.endswith("ов")]
    for pupils in filtered_pupils:
        result.append(f"Школьник: {pupils.fio}, Класс(ы): {', '.join(forms_dict[id] for id in pupil_form_dict.get(pupils.id, []))}")
    return result