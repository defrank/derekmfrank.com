from django_evolution.mutations import ChangeField
from django.db import models


MUTATIONS = [
    ChangeField('Assignment', 'description', initial=None, null=True)
]
