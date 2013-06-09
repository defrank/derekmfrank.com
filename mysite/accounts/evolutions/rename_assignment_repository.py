from django_evolution.mutations import RenameField
from django.db import models


MUTATIONS = [
    RenameField('Assignment', 'assignment_repository', 'assignment_repository_url'),
]
