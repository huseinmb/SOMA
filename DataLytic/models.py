from django.db import models

class cluster(models.Model):
    Entity = models.CharField(max_length=200)

    def __str__(self):
        return self.Entity

