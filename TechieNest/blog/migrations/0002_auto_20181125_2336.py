# Generated by Django 2.0.5 on 2018-11-25 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.CharField(help_text='Your username', max_length=26),
        ),
    ]
