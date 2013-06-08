from django_evolution.mutations import AddField
from django.db import models


MUTATIONS = [
    AddField('Education', 'coursework_repository_name', models.CharField, max_length=2, null=True),
]
