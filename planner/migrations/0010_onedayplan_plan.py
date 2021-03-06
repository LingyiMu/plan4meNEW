# Generated by Django 3.1 on 2020-09-01 22:29

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('planner', '0009_auto_20200901_0055'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_from', models.DateField()),
                ('date_to', models.DateField()),
                ('city', models.CharField(max_length=300)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OneDayPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('theme', models.CharField(default='unthemed', max_length=30)),
                ('places', django.contrib.postgres.fields.ArrayField(base_field=models.JSONField(), size=None)),
                ('foods', django.contrib.postgres.fields.ArrayField(base_field=models.JSONField(), size=None)),
                ('belongs_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planner.plan')),
            ],
        ),
    ]
