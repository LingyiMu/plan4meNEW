# Generated by Django 3.1 on 2020-09-01 23:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('planner', '0011_auto_20200901_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='belongs_to_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.profile'),
        ),
    ]
