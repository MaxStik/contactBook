from django.db import models


class Contact(models.Model):
    name = models.CharField(verbose_name="Имя", max_length=127, blank=True)
    surname = models.CharField(verbose_name="Фамилия", max_length=127, blank=True)
    middle_name = models.CharField(verbose_name="Отчество", max_length=127, blank=True)
    email = models.CharField(verbose_name="E-Mail", max_length=127, blank=True)
    phone = models.CharField(verbose_name="Телефон", max_length=31, blank=True)
    birthday = models.DateField(verbose_name="День рождения", blank=True)