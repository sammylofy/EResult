def get_grade_and_weight(score):
    if score < 40:
        grade = 'F'
        weight = 0.0
    elif 40 <= score < 45:
        grade = 'E'
        weight = 2.00
    elif 45 <= score < 50:
        grade = 'D'
        weight = 2.25
    elif 50 <= score < 55:
        grade = 'CD'
        weight = 2.50
    elif 55 <= score < 60:
        grade = 'C'
        weight = 2.75
    elif 60 <= score < 65:
        grade = 'BC'
        weight = 3.00
    elif 65 <= score < 70:
        grade = 'B'
        weight = 3.25
    elif 70 <= score < 75:
        grade = 'AB'
        weight = 3.5
    else:
        grade = 'A'
        weight = 4.00
    return grade, weight


def get_grade_point(grade):
    if grade == 'F':
        return 0
    elif grade == 'E':
        return 2.00
    elif grade == 'D':
        return 2.25
    elif grade == 'CD':
        return 2.50
    elif grade == 'C':
        return 2.75
    elif grade == 'BC':
        return 3.00
    elif grade == 'B':
        return 3.25
    elif grade == 'AB':
        return 3.5
    else:
        return 4.00


def get_remark(cgpa):
    if 3.50 <= cgpa <= 4.00:
        return "Distinction"
    elif 3.00 <= cgpa < 3.50:
        return "Upper Credit"
    elif 2.50 <= cgpa < 3.00:
        return "Lower Credit"
    elif 2.00 <= cgpa < 2.50:
        return "Pass"
    elif cgpa < 2.00:
        return "Fail"
    else:
        return "Invalid CGPA"


def get_cu_x_weight(credit_unit, grade_point):
    return credit_unit * grade_point


def total_score(a, b):
    return a + b


def get_gpa(tce, tcr):
    result = tce / tcr
    return round(result, 2)