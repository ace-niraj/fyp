# Generated by Django 3.2.8 on 2021-12-04 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0003_alter_studentscore_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentscore',
            name='exam_type',
            field=models.CharField(default='None', max_length=50),
        ),
    ]
