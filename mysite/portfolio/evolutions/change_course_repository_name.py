from django_evolution.mutations import ChangeField
from django.db import models


MUTATIONS = [
    ChangeField('Course', 'course_repository_name', initial=None, max_length=2),
]
