from django_evolution.mutations import RenameField
from django.db import models


MUTATIONS = [
    RenameField('Course', 'course_repository', 'course_repository_url')
]
