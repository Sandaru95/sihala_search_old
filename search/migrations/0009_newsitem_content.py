# Generated by Django 2.2.4 on 2019-12-11 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0008_remove_newsitem_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsitem',
            name='content',
            field=models.CharField(default='hello world', max_length=5000),
            preserve_default=False,
        ),
    ]
