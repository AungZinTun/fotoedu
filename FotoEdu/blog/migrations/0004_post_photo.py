# Generated by Django 2.2.6 on 2019-10-10 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_time_to_read'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='static/img/'),
        ),
    ]
