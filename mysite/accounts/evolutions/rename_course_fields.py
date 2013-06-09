from django_evolution.mutations import RenameField
from django.db import models


MUTATIONS = [
    RenameField('Course', 'course_name', 'name'),
    RenameField('Course', 'course_number', 'number'),
    RenameField('Course', 'course_lab_letter', 'lab_letter'),
    RenameField('Course', 'course_lab_url', 'lab_url'),
    RenameField('Course', 'course_repository_url', 'repository_url'),
    RenameField('Course', 'course_repository_name', 'repository_name'),
]
