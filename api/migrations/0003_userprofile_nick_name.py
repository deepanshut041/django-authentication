# Generated by Django 3.1 on 2020-08-26 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_userprofile_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='nick_name',
            field=models.CharField(blank=True, default='', max_length=40, null=True),
        ),
    ]