# Generated by Django 4.1.4 on 2023-01-24 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0002_remove_employer_changed_count_alter_employer_boss'),
    ]

    operations = [
        migrations.AddField(
            model_name='employer',
            name='changed_count',
            field=models.IntegerField(default=0, editable=False),
        ),
    ]
