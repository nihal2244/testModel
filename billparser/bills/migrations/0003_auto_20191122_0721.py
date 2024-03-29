# Generated by Django 2.2.7 on 2019-11-22 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0002_auto_20191122_0655'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='created_at',
            new_name='createdAt',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='user_name',
            new_name='userName',
        ),
        migrations.AlterField(
            model_name='bills',
            name='buyer',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='bills',
            name='vender',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
