# Generated by Django 3.2.8 on 2021-11-15 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_auto_20211115_1325'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='studenttype',
            new_name='student',
        ),
        migrations.AlterField(
            model_name='user',
            name='usertype',
            field=models.CharField(choices=[('admin', 'admin'), ('teacher', 'teacher'), (models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='authentication.studenttype'), 'student')], default=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='authentication.studenttype'), max_length=255),
        ),
    ]