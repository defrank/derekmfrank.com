from django_evolution.mutations import RenameField
from django.db import models


MUTATIONS = [
    RenameField('Education', 'coursework_repository', 'coursework_repository_url')
]
