from django.db import models

class Regle(models.Model):
    nom = models.CharField(max_length=200)
    typeregle = models.CharField(max_length=50)
    corps = models.TextField()
    libparam1 = models.CharField(max_length=50)
    libparam2 = models.CharField(max_length=50)
    libparam3 = models.CharField(max_length=50)
    libparam4 = models.CharField(max_length=50)
    libparam5 = models.CharField(max_length=50)
    libparam6 = models.CharField(max_length=50)
    libparam7 = models.CharField(max_length=50)
    libparam8 = models.CharField(max_length=50)
    libparam9 = models.CharField(max_length=50)
    libparam10 = models.CharField(max_length=50)

    def __str__(self):
        return self.nom

    class Meta:
        managed = False
        db_table = 'regle'


class Abonne(models.Model):
    codeabonne = models.CharField(max_length=10)
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.codeabonne

    class Meta:
        managed = False
        db_table = 'abonne'

class RegleAbonne(models.Model):
    idregle = models.IntegerField()
    idabonne = models.IntegerField()
    ordre = models.SmallIntegerField()
    valparam1 = models.CharField(max_length=50)
    valparam2 = models.CharField(max_length=50)
    valparam3 = models.CharField(max_length=50)
    valparam4 = models.CharField(max_length=50)
    valparam5 = models.CharField(max_length=50)
    valparam6 = models.CharField(max_length=50)
    valparam7 = models.CharField(max_length=50)
    valparam8 = models.CharField(max_length=50)
    valparam9 = models.CharField(max_length=50)
    valparam10 = models.CharField(max_length=50)


    class Meta:
        managed = False
        db_table = 'regleabonne'
