from django.db import models

# Create your models here.
class Person(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    endereco = models.CharField(max_length=150)
    pais = models.CharField(max_length=20)
    estado = models.CharField(max_length=20)
    municipio = models.CharField(max_length=20)
    cep = models.IntegerField()
    rua = models.CharField(max_length=20)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=50)
    cpf = models.IntegerField()
    pis = models.IntegerField()
    senha = models.IntegerField()
    foto = models.ImageField(upload_to='usuarios_fotos', null=True, blank=True) #opcional

    def __str__(self) -> str:
        return self.nome