# Generated by Django 3.1.4 on 2020-12-04 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_remove_item_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='video_title',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
