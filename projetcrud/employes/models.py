from django.db import models

#Class employés
class Employe(models.Model):
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    adresse = models.TextField()
    telephone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.prenom} {self.nom}"
