# Generated by Django 3.2.4 on 2021-06-30 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movierecord',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]