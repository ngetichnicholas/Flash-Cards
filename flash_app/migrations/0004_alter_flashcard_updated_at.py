# Generated by Django 3.2.5 on 2021-07-21 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flash_app', '0003_alter_flashcard_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flashcard',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]