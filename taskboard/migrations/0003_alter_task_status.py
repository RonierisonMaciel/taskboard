# Generated by Django 4.0.6 on 2022-07-28 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskboard', '0002_alter_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Doing', 'Doing'), ('Done', 'Done')], default='Pending', max_length=20),
        ),
    ]
