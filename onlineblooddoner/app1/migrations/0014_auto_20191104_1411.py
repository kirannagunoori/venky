# Generated by Django 2.2.4 on 2019-11-04 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0013_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='upass',
            field=models.CharField(default=False, max_length=20),
        ),
    ]
