# Generated by Django 4.0.2 on 2022-03-06 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_user_admin_alter_user_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(default='Минск', max_length=64, verbose_name='city')),
                ('street', models.CharField(default='Есенина', max_length=64, verbose_name='street')),
                ('house', models.CharField(default='19Б', max_length=64, verbose_name='house')),
                ('flat', models.CharField(default='49', max_length=64, verbose_name='flat')),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='address',
        ),
    ]
