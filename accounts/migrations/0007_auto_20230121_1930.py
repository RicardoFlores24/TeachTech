# Generated by Django 3.1 on 2023-01-22 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20230121_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='languages_choice',
            field=models.SlugField(choices=[('Python', 'Python'), ('Java', 'Java'), ('Javascript', 'Javascript'), ('Css', 'Css'), ('Html', 'Html'), ('React', 'React'), ('C++', 'C++'), ('C#', 'C#')], default=False),
        ),
    ]