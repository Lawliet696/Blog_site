# Generated by Django 5.1.1 on 2024-09-22 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
