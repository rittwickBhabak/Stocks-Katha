# Generated by Django 3.2.10 on 2022-02-08 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sjvideo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='notes',
            field=models.TextField(default=''),
        ),
    ]
