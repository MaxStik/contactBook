# Generated by Django 2.1 on 2018-08-08 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=127, verbose_name='Имя')),
                ('surname', models.CharField(blank=True, max_length=127, verbose_name='Имя')),
                ('middle_name', models.CharField(blank=True, max_length=127, verbose_name='Имя')),
                ('email', models.CharField(blank=True, max_length=127, verbose_name='Имя')),
                ('phone', models.CharField(blank=True, max_length=31, verbose_name='Имя')),
                ('birthday', models.DateField(blank=True, verbose_name='Имя')),
            ],
        ),
    ]
