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

courses.to_sql('courses', con, if_exists='replace', index=False)
assessments.to_sql('assessments', con, if_exists='replace', index=False)
vle.to_sql('vle', con, if_exists='replace', index=False)
students.to_sql('students', con, if_exists='replace', index=False)
student_registration.to_sql('student_registration', con, if_exists='replace', index=False)
student_assessments.to_sql('student_assessments', con, if_exists='replace', index=False)
student_vle.to_sql('student_vle', con, if_exists='replace', index=False)
