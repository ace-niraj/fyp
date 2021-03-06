# Generated by Django 3.2.8 on 2021-11-15 07:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_alter_user_usertype'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='studenttype',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='authentication.studenttype'),
        ),
        migrations.AlterField(
            model_name='user',
            name='usertype',
            field=models.CharField(choices=[('admin', 'admin'), ('teacher', 'teacher'), ('student', 'student')], default='student', max_length=255),
        ),
    ]
