import sqlite3

import pandas as pd

con = sqlite3.connect("data/ou.db")
cur = con.cursor()

courses = pd.read_csv('data/courses.csv')
assessments = pd.read_csv('data/assessments.csv')
vle = pd.read_csv('data/vle.csv')
students = pd.read_csv('data/studentInfo.csv')
student_registration = pd.read_csv('data/studentRegistration.csv')
student_assessments = pd.read_csv('data/studentAssessment.csv')
student_vle = pd.read_csv('data/studentVle.csv')

i = 0

code_modules = {}

for row in assessments.itertuples():
    if row.code_module in code_modules:
        if row.code_presentation in code_modules[row.code_module]:
            code_modules[row.code_module][row.code_presentation].append(row)
        else:
            code_modules[row.code_module][row.code_presentation] = [row]
    else:
        code_modules[row.code_module] = {}

id_assessments = []
i = 0
# Finds the closest assessment to the vle usage date and assigns that assessment as the one currently being worked on
for row in student_vle.itertuples():
    possible_assessments = code_modules[row.code_module][row.code_presentation]

    min_date_difference = -1000
    best_assessment_id = None
    for assessment in possible_assessments:
        if 0 >= row.date - assessment.date > min_date_difference:
            min_date_difference = row.date - assessment.date
            best_assessment_id = assessment.id_assessment
    id_assessments.append(best_assessment_id)
    if i % 100000 == 0:
        print(i, row, best_assessment_id)
    i += 1


student_vle['id_assessment'] = id_assessments

courses.to_sql('courses', con, if_exists='replace', index=False)
assessments.to_sql('assessments', con, if_exists='replace', index=False)
vle.to_sql('vle', con, if_exists='replace', index=False)
students.to_sql('students', con, if_exists='replace', index=False)
student_registration.to_sql('student_registration', con, if_exists='replace', index=False)
student_assessments.to_sql('student_assessments', con, if_exists='replace', index=False)
student_vle.to_sql('student_vle', con, if_exists='replace', index=False)
