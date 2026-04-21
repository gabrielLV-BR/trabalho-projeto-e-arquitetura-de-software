import pandas as pd
import sqlite3
import time

from model.course import CourseModality
from model.institution import AdministrativeCategory

connection = sqlite3.connect('database.sqlite')

State='Estado'
City='Cidade'
InstitutionName='IES'
Acronym='Sigla'
Organization='Organização'
Category='Categoria Administrativa'
CourseName='Nome do Curso'
DetailedCourseName='Nome Detalhado do Curso'
Modality='Modalidade'
Degree='Grau'
Years=['2014','2015','2016','2017','2018','2019','2020','2021','2022']

print('Begin processing')
start_process_time = time.time()

modality_type_df = pd.DataFrame({
    'modality_name': ['Presencial', 'EaD'],
    'modality_type': [CourseModality.PRESENTIAL.value, CourseModality.EAD.value]
})

administrative_category_df = pd.DataFrame({
    'category_name': [
        'Privada sem fins lucrativos',
        'Privada sem fins lucrativos ',
        'Privada com fins lucrativos',
        'Privada com fins lucrativos ',
        'Pública Estadual',
        'Pública Federal',
        'Pública Municipal',
        'Especial'
    ],
    'category_type': [
        AdministrativeCategory.PRIVATE.value,
        AdministrativeCategory.PRIVATE.value,
        AdministrativeCategory.PRIVATE.value,
        AdministrativeCategory.PRIVATE.value,
        AdministrativeCategory.PUBLIC.value,
        AdministrativeCategory.PUBLIC.value,
        AdministrativeCategory.PUBLIC.value,
        AdministrativeCategory.SPECIAL.value
    ]
})

matriculas_df = pd.read_csv("matriculas.csv", sep=';')

stats_df = matriculas_df.melt(
    [InstitutionName, Acronym,
     Organization, Category,
     CourseName, DetailedCourseName,
     State, City,
     Modality, Degree],
    value_vars=Years,
    var_name='year',
    value_name='student_count'
).dropna()

stats_df = stats_df[
    [InstitutionName, CourseName, State, City, Modality, Degree, 'year', 'student_count']
].drop_duplicates()
stats_df.columns = [
    'ies', 'course_name', 'state',
    'city', 'modality', 'degree',
    'year', 'student_count']

institutions_df = matriculas_df[
    [InstitutionName, Acronym, Organization, Category]
].drop_duplicates()
institutions_df.columns = ['ies', 'acronym', 'organization', 'category']
institutions_df = institutions_df.merge(administrative_category_df, left_on='category', right_on='category_name', how='inner')
institutions_df = institutions_df.drop(columns=['category_name'])
institutions_df['institution_id'] = institutions_df.index + 1

courses_df = matriculas_df[
    [CourseName, DetailedCourseName, State, City, Modality, InstitutionName, Degree]
].drop_duplicates()

courses_df.columns = ['name', 'detailed_name', 'state', 'city', 'modality', 'institution_name', 'degree']
courses_df = courses_df.merge(institutions_df, left_on='institution_name', right_on='ies', how='left', suffixes=['', '_right'])
courses_df = courses_df.merge(modality_type_df, left_on='modality', right_on='modality_name', how='inner')
courses_df = courses_df.drop(columns=['acronym', 'organization', 'category', 'institution_name', 'modality_name'])
courses_df['course_id'] = courses_df.index + 1;

stats_df = stats_df.merge(
    courses_df,
    left_on=['course_name', 'ies', 'state', 'city', 'modality', 'degree'],
    right_on=['name', 'ies', 'state', 'city', 'modality', 'degree'],
    how='left',
    suffixes=['', '_right'])
stats_df = stats_df.drop(columns=['course_name', 'name', 'ies', 'detailed_name', 'institution_id', 'degree', 'state', 'city', 'degree', 'modality'])
stats_df['stats_id'] = stats_df.index + 1;

institutions_df = institutions_df.rename(
    columns={
        'institution_id': 'id'
    }
).set_index(keys='id')

courses_df = courses_df.rename(
    columns={
        'course_id': 'id',
        # 'institution_id': 'institution'
    }
).set_index(keys='id')

stats_df = stats_df.rename(
    columns={
        'stats_id': 'id',
        # 'course_id': 'course'
    }
).set_index(keys='id')

end_process_time = time.time()

print('Processing finished. Took {:.2f} seconds'.format(end_process_time - start_process_time))

print('Institutions:', institutions_df.columns)
print('Courses:', courses_df.columns)
print('Stats:', stats_df.columns)

print('Begin saving')
start_save_time = time.time()

# gera tabelas corretamente
# ele só gera chave primárias pra sqlite por enquanto
# tô vendo como fazer pra ele gerar pro postgres também
institutions_df.to_sql('institution', connection, if_exists='replace', dtype={'id': 'INTEGER PRIMARY KEY'})
courses_df.to_sql('course', connection, if_exists='replace', dtype={'id': 'INTEGER PRIMARY KEY'})
stats_df.to_sql('registration', connection, if_exists='replace', dtype={'id': 'INTEGER PRIMARY KEY'})
connection.close()

end_save_time = time.time()

print('Saving finished. Took {:.2f} seconds'.format(end_save_time - start_save_time))
