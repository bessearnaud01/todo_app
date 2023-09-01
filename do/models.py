from django.db import models

# Create your models here.

class Task(models.Model):
    tache = models.CharField(max_length=150)

    # cette fontion permetr affiche que le nom de chaque tâche
    def __str__(self):
        return self.tache