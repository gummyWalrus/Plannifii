# Generated by Django 3.1.7 on 2021-03-27 22:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('planning', '0009_auto_20210327_2252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='doer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='planning.profile'),
        ),
    ]
