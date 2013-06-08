from django_evolution.mutations import DeleteField, AddField, ChangeField
from django.db import models
from limn.models import UserProfile

def get_user():
    return UserProfile.objects.get(pk=1)


MUTATIONS = [
    #DeleteField('UserSource', 'user'),
    ChangeField('UserSource', 'user', models.ForeignKey, related_model=UserProfile),
    #DeleteField('UserImage', 'user'),
    ChangeField('UserImage', 'user', models.ForeignKey, related_model=UserProfile),
    #DeleteField('UserDocument', 'user'),
    ChangeField('UserDocument', 'user', models.ForeignKey, related_model=UserProfile),
]
