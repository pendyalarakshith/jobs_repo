# Generated by Django 4.1 on 2024-09-20 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0003_alter_hydjobs_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hydjobs',
            name='address',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='hydjobs',
            name='company',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='hydjobs',
            name='eligibility',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='hydjobs',
            name='title',
            field=models.CharField(max_length=120),
        ),
    ]
