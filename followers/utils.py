from django.contrib.auth.models import User


def get_followers(user):
    # devuelve una lista con los pk de los usuarios de las relaciones en las que el usuario user es relationship_target
    followers_pks = user.relationship_target.all().values_list('origin__pk', flat=True)
    return list(User.objects.filter(pk__in=followers_pks))

    # Metodo 2
    # relationships = Relationship.objects.filter(target=user).select_related('origin')
    # followers = list()
    # for relationship in relationships:
    #     followers.append(relationship.origin)
    # return followers


def get_following(user):
    following_pks = user.relationship_origin.all().values_list('target__pk', flat=True)
    return list(User.objects.filter(pk__in=following_pks))
