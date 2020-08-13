from django.db import models


# Create your models here.
class Disco(models.Model):
    """docstring for disco"""

    nome = models.CharField('disco', max_length=50)


class Musica(models.Model):
    disco = models.ForeignKey(Disco, on_delete=models.CASCADE)
    nome = models.CharField('nome do disco', max_length=50)

