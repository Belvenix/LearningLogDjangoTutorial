# Generated by Django 3.1.7 on 2021-03-03 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0002_entry'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='is_edited',
            field=models.BooleanField(default=False),
        ),
    ]