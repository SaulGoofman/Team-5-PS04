# Generated by Django 4.1.1 on 2022-09-17 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_alter_allotedhall_allotid_alter_feedback_fbid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='permLetter',
            field=models.FileField(blank=True, upload_to='permissionLetters/'),
        ),
        migrations.AlterField(
            model_name='request',
            name='poster',
            field=models.ImageField(blank=True, upload_to='posters/'),
        ),
    ]
