# Generated by Django 3.1.7 on 2021-04-20 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cs111', '0005_add_youtube2'),
    ]

    operations = [
        migrations.CreateModel(
            name='LabGrade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commit_id', models.CharField(max_length=40)),
                ('late_days', models.IntegerField()),
                ('grade', models.IntegerField()),
                ('lab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cs111.lab')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lab_grades', to='cs111.role')),
            ],
            options={
                'unique_together': {('student', 'lab')},
            },
        ),
    ]