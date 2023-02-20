# Generated by Django 3.1 on 2023-01-22 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20230122_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='languages_choice',
            field=models.SlugField(choices=[('PY', 'Python'), ('JV', 'Java'), ('JS', 'Javascript'), ('CS', 'Css'), ('HT', 'Html'), ('RC', 'React'), ('CPP', 'C++'), ('CSS', 'C#')], default=False),
        ),
    ]