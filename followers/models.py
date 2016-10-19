from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Relationship(models.Model):

    # Solo funciona en postgresql o mysql
    # unique_together = ("origin", "target")  # asegura que la relacion origin-target es unica y no repetida

    origin = models.ForeignKey(User, related_name="relationship_origin")  # usuario que sigue
    target = models.ForeignKey(User, related_name="relationship_target")  # usuario al que sigue
    created_at = models.DateTimeField(auto_now_add=True)
