# Generated by Django 3.2.7 on 2021-10-05 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notepost',
            name='subject',
            field=models.CharField(default='...', max_length=200),
        ),
    ]
