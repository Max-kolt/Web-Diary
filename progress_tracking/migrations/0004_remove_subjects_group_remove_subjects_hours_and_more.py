# Generated by Django 4.2 on 2023-04-08 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('progress_tracking', '0003_remove_studyevents_date_studyevents_time_create_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subjects',
            name='group',
        ),
        migrations.RemoveField(
            model_name='subjects',
            name='hours',
        ),
        migrations.RemoveField(
            model_name='subjects',
            name='teacher',
        ),
        migrations.AddField(
            model_name='subjects',
            name='MDK',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='subjects',
            name='slug',
            field=models.SlugField(max_length=255, null=True, unique=True, verbose_name='URL'),
        ),
        migrations.CreateModel(
            name='GroupSubjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hours', models.IntegerField()),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='progress_tracking.groups')),
                ('subject_ID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='progress_tracking.subjects')),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='progress_tracking.teachers')),
            ],
        ),
    ]