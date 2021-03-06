# Generated by Django 3.1.7 on 2021-06-21 17:30

from django.db import migrations, models
import django.db.models.deletion

def create_spring21(apps, schema_editor):
    Offering = apps.get_model('cs111', 'Offering')
    offering = Offering(id=1, slug='spring21')
    offering.save()

class Migration(migrations.Migration):

    dependencies = [
        ('cs111', '0009_add_course_grades'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offering',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.RunPython(create_spring21),
        migrations.AddField(
            model_name='lab',
            name='offering',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='labs', to='cs111.offering'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lecture',
            name='offering',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='lectures', to='cs111.offering'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='role',
            name='offering',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='roles', to='cs111.offering'),
            preserve_default=False,
        ),
    ]
