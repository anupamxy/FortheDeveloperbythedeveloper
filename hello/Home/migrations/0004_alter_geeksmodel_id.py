# Generated by Django 5.0 on 2023-12-28 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_geeksmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geeksmodel',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
