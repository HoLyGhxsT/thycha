# Generated by Django 3.2 on 2023-02-21 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfoliomaster',
            name='category',
            field=models.CharField(choices=[('all', 'all'), ('print', 'print'), ('packaging', 'packaging'), ('illust', 'illust'), ('digi', 'digi'), ('brands', 'brands')], default='all', max_length=15),
        ),
    ]
