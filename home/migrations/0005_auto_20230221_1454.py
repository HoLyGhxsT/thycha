# Generated by Django 3.2 on 2023-02-21 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_portfoliomaster_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfoliomaster',
            name='id',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterModelTable(
            name='portfoliomaster',
            table='PORTFOLIOMASTER',
        ),
    ]
