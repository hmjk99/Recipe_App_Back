# Generated by Django 4.2 on 2023-04-11 23:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_api', '0006_alter_recipe_recipes_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='recipes_id',
            new_name='user_profile',
        ),
    ]
