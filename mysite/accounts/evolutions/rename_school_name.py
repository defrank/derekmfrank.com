from django_evolution.mutations import RenameField
from django.db import models


MUTATIONS = [
    RenameField('Education', 'school_name', 'name')
]
