# Generated by Django 2.1 on 2018-08-19 07:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('word_count', '0001_initial_squashed_0004_auto_20180818_1742'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='wordcount',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='wordcount',
            name='page',
        ),
        migrations.DeleteModel(
            name='Page',
        ),
        migrations.DeleteModel(
            name='WordCount',
        ),
    ]
