# Generated by Django 5.0.7 on 2025-01-14 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuariopersonalizado',
            name='nome',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='usuariopersonalizado',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]
