# Generated by Django 3.1.7 on 2021-05-11 02:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cs111', '0006_add_lab_grades'),
    ]

    operations = [
        migrations.CreateModel(
            name='MidtermGrade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.FloatField()),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='midterm_grade', to='cs111.role')),
            ],
        ),
    ]