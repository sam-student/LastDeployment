# Generated by Django 2.0 on 2019-04-05 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Populrity_Score',
            field=models.FloatField(default=0.0),
        ),
    ]