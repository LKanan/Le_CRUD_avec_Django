from django.db import models


# Create your models here.
# Un modèle est une table dans la base de données qui est composée des colonnes qvec des titre pour chaque colonne
class Student(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)
