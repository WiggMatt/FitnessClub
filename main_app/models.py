from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    bio = models.CharField("ФИО", max_length=100)
    GENDER_CHOICES = [
        ('M', 'Мужской'),
        ('F', 'Женский'),
        ('O', 'Другой'),
    ]
    username = models.EmailField("Электронная почта", max_length=100, unique=True)

    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return self.username


class ClientProfile(CustomUser):
    birth_date = models.DateField()
    phone_number = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return self.username


class Administrator(CustomUser):
    additional_info = models.TextField()  # Дополнительная информация об администраторе

    def __str__(self):
        return self.username


class Tariff(models.Model):
    TYPE_CHOICES = (
        ('monthly', 'Monthly'),
        ('annual', 'Annual'),
        ('daily', 'Daily'),
    )
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Subscription(models.Model):
    client = models.ForeignKey(ClientProfile, on_delete=models.CASCADE)
    tariff = models.ForeignKey(Tariff, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.client.username} - {self.tariff.name}"
