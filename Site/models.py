from django.db import models

# Create your models here.




class Balance(models.Model):
    balance = models.DecimalField(verbose_name='Saldo', max_digits=100, decimal_places=2)
    


class Profile(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')
    cpf = models.IntegerField()
    email = models.CharField(max_length=100)
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=100, verbose_name='Senha')
    picture = models.ImageField(upload_to='uploads', verbose_name='Imagem')
    age = models.IntegerField(verbose_name='Idade')
    rating = models.IntegerField(verbose_name='Avaliação')
    balance = models.OneToOneField(Balance, verbose_name='Saldo', on_delete=models.CASCADE)

class MotoTaxi(Profile, models.Model):
    cnh = models.IntegerField()
    status = models.BooleanField()


class Rating(models.Model):
    title = models.CharField(max_length=50, verbose_name='Titulo')
    text = models.TextField()
    rating = models.DecimalField(verbose_name='Nota', max_digits=100, decimal_places=2)


