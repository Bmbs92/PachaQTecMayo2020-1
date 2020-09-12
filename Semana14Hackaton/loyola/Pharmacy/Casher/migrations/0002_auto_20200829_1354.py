# Generated by Django 3.1 on 2020-08-29 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Casher', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='productStock',
        ),
        migrations.AddField(
            model_name='products',
            name='stock',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='stock',
        ),
    ]