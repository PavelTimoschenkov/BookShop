# Generated by Django 4.0.2 on 2022-03-06 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_alter_user_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(blank=True, max_length=100, verbose_name='Адрес доставки'),
        ),
        migrations.DeleteModel(
            name='UserLocation',
        ),
    ]
