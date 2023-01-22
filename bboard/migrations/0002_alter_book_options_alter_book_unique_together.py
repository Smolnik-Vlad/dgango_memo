# Generated by Django 4.1.4 on 2023-01-20 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ('-title',), 'verbose_name': 'Книга', 'verbose_name_plural': 'Книги'},
        ),
        migrations.AlterUniqueTogether(
            name='book',
            unique_together={('title', 'published_date')},
        ),
    ]