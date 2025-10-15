from django.db import models

# Create your models here.
class User(models.Model):
    nome = models.CharField(max_length=20, default='Anônimo')
    mensagem = models.CharField()

    def __str__(self):
        return self.mensagem