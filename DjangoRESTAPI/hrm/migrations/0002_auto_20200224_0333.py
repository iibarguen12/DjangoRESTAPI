# Generated by Django 3.0.3 on 2020-02-24 02:33

from django.db import migrations, models
import hrm.models


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to=hrm.models.Users.upload_file),
        ),
    ]