# Generated by Django 3.2.8 on 2021-12-08 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('writtenexam', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='examquestion',
            old_name='quiz',
            new_name='exam',
        ),
    ]
