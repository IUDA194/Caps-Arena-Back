# Generated by Django 4.2.3 on 2023-07-09 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.TextField()),
                ('user_name', models.TextField()),
                ('photo_url', models.TextField()),
                ('date_of_login', models.DateField()),
            ],
        ),
    ]
