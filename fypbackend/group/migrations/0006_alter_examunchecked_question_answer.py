# Generated by Django 3.2.8 on 2021-12-11 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0005_examunchecked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examunchecked',
            name='question_answer',
            field=models.JSONField(verbose_name={}),
        ),
    ]