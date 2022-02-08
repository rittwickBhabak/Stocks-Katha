# Generated by Django 3.2.10 on 2022-02-08 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('edited_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]