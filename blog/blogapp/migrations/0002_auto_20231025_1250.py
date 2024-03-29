# Generated by Django 3.2.18 on 2023-10-25 09:50

from django.db import migrations, models
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='body',
            field=markdownx.models.MarkdownxField(),
        ),
        migrations.AlterField(
            model_name='blog',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
