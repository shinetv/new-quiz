# Generated by Django 3.2.3 on 2021-12-29 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0006_result'),
    ]

    operations = [
        migrations.RenameField(
            model_name='result',
            old_name='percentage',
            new_name='percent',
        ),
    ]
