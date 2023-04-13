# Generated by Django 4.2 on 2023-04-10 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('progress_tracking', '0004_remove_subjects_group_remove_subjects_hours_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentestimates',
            name='mark',
            field=models.CharField(choices=[('1', 'Poor'), ('2', 'Unsatisfactory'), ('3', 'Satisfactory'), ('4', 'Good'), ('5', 'Excellent'), ('n', 'Absent')], max_length=1, null=True),
        ),
    ]