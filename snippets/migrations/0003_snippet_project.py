# Generated by Django 4.1 on 2022-08-30 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0002_snippet_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='project',
            field=models.CharField(default='null', max_length=100),
            preserve_default=False,
        ),
    ]
