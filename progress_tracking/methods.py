from .models import *


def generate_table_by_stud_lessons(students, lessons) -> list[dict[str, int, list]]:
    table_matrix = []
    for stud in students:
        current_student = {'stud_name': f'{stud.lname} {stud.fname} {stud.mname}', 'stud_id': stud.pk, 'estimates': []}
        for lesson in lessons:
            stud_lesson = StudentEstimates.objects.filter(lesson_ID=lesson.pk)
            try:
                stud_mark = stud_lesson.get(student_ID=stud.pk)
                current_student['estimates'].append({'date': lesson.date, 'mark': stud_mark.mark})
            except Exception:
                current_student['estimates'].append({'date': lesson.date, 'mark': None})
        table_matrix.append(current_student)
    return table_matrix
