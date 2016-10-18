from django.contrib.auth.models import User


def get_followers(user):
    # devuelve una lista con los pk de los usuarios de las relaciones en las que el usuario user es relationship_target
    followers_pks = user.relationship_target.all().values_list('origin__pk', flat=True)
    return list(User.objects.filter(pk__in=followers_pks))

def get_following(user):
    pass