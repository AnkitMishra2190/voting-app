# Generated by Django 4.2.4 on 2023-08-10 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VotingApp', '0003_admin2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='userId',
            field=models.EmailField(max_length=50, unique=True),
        ),
    ]
